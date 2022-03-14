import requests
from bs4 import BeautifulSoup
from datetime import date


def parse_bday(birthday):
	months = {'1':'January', '2':'Febuary', '3':'March', '4':'April', 
			  '5':'May', '6':'June', '7':'July', '8':'August', 
			  '9':'September', '10':'October', '11':'November', '12':'December'}
	print("---------------------------------------------------------------------------")
	url = 'https://nookipedia.com/wiki/Villagers/New_Horizons'

	try:
		page = requests.get(url)
	except Exception as e:
		print(e)
		return "0"

	soup = BeautifulSoup(page.text, "html.parser")

	links = soup.find_all('td')
	bDayLinks = []

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
			bDayDict[link.text] = [link['data-sort-value']]
		else:
			bDayDict[link.text].append(link['data-sort-value'])

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
	date = ''
	date = date.join([months[m], " ", v, "\n"])
	if date in bDayDict:
		print("IT IS: ", bDayDict[date])


	print("---------------------------------------------------------------------------")
	bdata = 'hey'
	message = {'data': bdata}
	return message