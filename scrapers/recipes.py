import requests
from lxml import html 
import os
import pandas as pd
import csv



url="http://allrecipes.com/recipe/241165"


def scrape(url):
	target=open('recipes.csv', 'w')
	csvwriter=csv.writer(target)
	headers=["Tile", "Ingrediants", "steps", "time"]
	csvwriter.writerow(headers)

	for i in xrange(10):
		print i
		url ="http://allrecipes.com/recipe/%d" % (241165+i)
		print url
		page=requests.get(url)
		recipe_row=[]
		data=html.fromstring(page.content)
		title = data.xpath('/html/body/div[1]/div[2]/div/div[3]/section/div[1]/div/section[2]/h1')[0].text
		ingrediants=data.xpath("//*[@id='lst_ingredients_1']/li")
		print title
		ingrediant_list= "" 
		for ingr_num in range(1,10):
			ingr_name =  "//*[@id='lst_ingredients_%s']/li" % ingr_num
			ingr_set = data.xpath(ingr_name)
			if len(ingr_set)>0:
				for ingr in ingr_set:
					ingrediant_list=ingrediant_list+ ingr.xpath("label/span")[0].text + " ;\n "
		time = data.xpath("/html/body/div[1]/div[2]/div/div[3]/section/section[2]/div/div[1]/ul/li[2]/time/span")[0].text
		steps=data.xpath("/html/body/div[1]/div[2]/div/div[3]/section/section[2]/div/div[1]/ol/li")
		step_text = "" 
		for step in steps:
			step_text=step_text+ step.xpath("span")[0].text +"n;\n "
		recipe_row=[title, ingrediant_list, step_text, time]
		csvwriter.writerow(recipe_row)


scrape(url)