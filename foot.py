import requests
from bs4 import BeautifulSoup

# get L1 results since season 2012/2013
# print XML data containing match results and scores


# links = soup.find_all("a")
# for link in links:
# 	print("<a href='%s'>%s</a>" %(link.get("href"), link.text))
urls = ["http://fr.soccerstats.com/results.asp?league=france",
		"http://fr.soccerstats.com/results.asp?league=france_2015",
		"http://fr.soccerstats.com/results.asp?league=france_2014",
		"http://fr.soccerstats.com/results.asp?league=france_2013"
		]
print("<matches>")
for i in range(4):
	url = urls[i]
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	#body = soup.find_all("table")
	tab = soup.find("table", {"id": "btable"})
	data = tab.find_all("tr", {"class" : "odd"})

	try:
		for fixture in data:
			print("    <match>")
			td = fixture.find_all("td")
			i = 0
			for element in td:
				if i == 2:
					teams = str(element).split(" - ")
					teams[0] = teams[0].replace(" ", "")
					teams[1] = teams[1].replace(" ", "")
					print("        <home>",teams[0].split("\xa0")[1],"</home>", sep="")
					print("        <away>",teams[1].split("<")[0],"</away>", sep="")
				if  i == 3:
					scores = str(element).split("-")
					scores[0] = scores[0].replace(" ","")
					scores[1] = scores[1].replace(" ","")
					print("        <homeGoals>",scores[0][-1],"</homeGoals>", sep="")
					print("        <awayGoals>",scores[1][0],"</awayGoals>", sep="")

				i += 1
			print("    </match>")
			
		#print(data)
	except:
		pass
print("</matches>")

