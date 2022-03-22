'''
TODO:
	- Get each row, pick out name & birthday, place data in dictionary:
		{ date : [Name, Species, Gender, Personality, Birthday, Catchphrase] }

'''

import requests
from bs4 import BeautifulSoup
from datetime import date


def parse_bday(birthday):
	months = {'1':'January', '2':'February', '3':'March', '4':'April', 
			  '5':'May', '6':'June', '7':'July', '8':'August', 
			  '9':'September', '10':'October', '11':'November', '12':'December'}
	print("---------------------------------------------------------------------------")
	url = 'https://nookipedia.com/wiki/Villagers/New_Horizons'

	# Access URL
	try:
		page = requests.get(url)
	except Exception as e:
		print(e)
		return "0"

	soup = BeautifulSoup(page.text, "html.parser")

	# Find all table tags
	links = soup.find_all('td')
	bDayLinks = []

	# Get tags specifically relating to the birthday date
	for link in links:
		try:
			if link['data-sort-value'] != None:
				bDayLinks.append(link)
		except:
			pass

	# Keep dictionary { date : data-sort-value }
	bDayDict = {}
	for link in bDayLinks:
		if link not in bDayDict:
			bDayDict[link.text] = [link]
		else:
			bDayDict[link.text].append(link)

	# birthday: "2022-03-08", 1 = month, 2 = date
	bvals = birthday.split("-")

	# Remove leading 0s
	m = 0
	day = 0
	for i, v in enumerate(bvals):
		while v[0] == "0":
			v = v[1:]
		if i == 1:
			m = v
		elif i == 2:
			day = v
	
	# Get date similar to that from nookiepedia
	date = ''.join([months[m], " ", day, "\n"])

	# If there is a villager w/ the same birthday get the parent to parse data
	parent = None
	name = None
	species = None
	personality = None
	print(date)
	if date in bDayDict:
		parent = bDayDict[date][0].parent
		imgLinks = parent.find('img')['srcset']
		imgLinks = imgLinks.split(',')
		bigImg = imgLinks[1].split()[0]
		
		# Extract villager name/species/attitude
		characteristics = parent.find_all('a')
		name = characteristics[1].text
		species = characteristics[2].text
		personality = characteristics[3].text

	print("---------------------------------------------------------------------------")
	data = {'name': name, 'species': species, 'personality': personality, 'img':bigImg}
	return data