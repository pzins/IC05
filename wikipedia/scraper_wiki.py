import requests
from bs4 import BeautifulSoup
import time
from random import randint

from lxml import etree


# get data from Wikipedia : start with keywrod(s) and visit all links in the pages

keywords = ["clavier", "souris", "cpu", "Mémoire_(informatique)", "Apprentissage_automatique", "Traitement_d'images", "Disque_dur",
			"ordinateur", "big_data", "Fichier_binaire"]

# keywords = ["lacazette", "fekir", "gonalons"]

# keywords = ["UTC", "ingenieur", "informatique"]

# keywords = ["Olympique_lyonnais"]

url_prefix = "https://fr.wikipedia.org/wiki/"


class Word:
	def __init__(self, _name):
		self.name = _name
		self.voisins = []

	def addVoisin(self, word):
		self.voisins.append(word)

	def __str__(self):
		res = ""
		for i in self.voisins:
			res += " "
			res += i;
		return self.name + " :=> " + res 



urls_queue = []

for i in keywords:
	urls_queue.append((i, i))

words = []


counter = 0;

while len(urls_queue) != 0 and counter < 20:
	print(counter)
	w = Word(urls_queue[0][0])
	url = urls_queue[0][1]
	urls_queue.pop(0)
	r = requests.get(url_prefix + url)
	soup = BeautifulSoup(r.content)
	bodyContent = soup.find("div", {"id" : "bodyContent"})
	mvcontent = bodyContent.find("div", {"id" : "mw-content-text"})
	body = mvcontent.find_all("a")
	random = randint(0, 100)
	random = random / 100
	time.sleep(2*random)
	for link in body:
		title = link.get("title")
		href = link.get("href")
		if title != None and href != None:
			urls_queue.append((title, href))
			w.addVoisin(title)
	words.append(w)
	counter += 1


list_words = []
list_links = []


for i in words:
	list_words.append(i.name)
	for j in i.voisins:
		if j not in list_words:
			list_words.append(j)
		tmp = (list_words.index(i.name), list_words.index(j))
		list_links.append(tmp)



# write to a GEXF file

f = open("gephi_wiki2.gexf","wb")
f.write(bytes("<?xml version='1.0' encoding='UTF-8'?>", 'UTF-8'))
root = etree.Element("gexf")
root.set("xmlns", "http://www.gexf.net/1.2draft")
root.set("version", "1.2")
meta = etree.SubElement(root, "meta")
meta.set("lastmodifieddate", "2009-03-20")
creator = etree.SubElement(meta, "creator")
creator.text = "Gexf.net"
description = etree.SubElement(meta, "description")
description.text = "Olympique Lyonnais"

graph = etree.SubElement(root, "graph")
graph.set("defaultedgetype", "undirected")
graph.set("mode", "static")

nodes = etree.SubElement(root, "nodes")

counter = 0
for i in list_words:
	w = etree.SubElement(nodes, "node")
	w.set("id", str(counter))
	w.set("label", i)
	counter += 1

edges = etree.SubElement(root, "edges")
counter = 0
for i in list_links:
	l = etree.SubElement(edges, "edge")
	l.set("id", str(counter))
	l.set("source", str(i[0]))
	l.set("target", str(i[1]))
	counter += 1


f.write(etree.tostring(root, pretty_print=True))
