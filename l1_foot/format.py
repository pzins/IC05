from lxml import etree

# analyse file with match results and score
# process results : mean between each teams with victory (+1) draw (0) and defeat (-1)
# add gps coordinate
# write a gephi GEXF file containing information
# you just have to open the file with Gephi



#class representant une rencontre
class Fixtures:

	def __init__(self, home, away, hGoals, aGoals):
		self.hId = home
		self.aId = away
		self.hGoals = hGoals
		self.aGoals = aGoals

	def getResult(self):
		res = []
		first = min(self.hId, self.aId)
		second = max(self.hId, self.aId)
		third = 0
		if self.hGoals > self.aGoals:
			if first == self.hId:
				third = 1
			else:
				third = -1
		if self.hGoals < self.aGoals:
			if first == self.aId:
				third = 1
			else:
				third = -1
		else:
			third = 0
		return ((first, second), third)

	def __str__(self):
		return str(self.hId) + " " + str(self.aId) + " " + str(self.hGoals) + " " + str(self.aGoals) + " " + str(self.getResult()) 

teams = []
fixtures = []


tree = etree.parse("data_l1.xml")
for user in tree.xpath("/matches/match/home"):
    if user.text not in teams:
    	teams.append(user.text)
for user in tree.xpath("/matches/match/away"):
    if user.text not in teams:
    	teams.append(user.text)
# teams contient toutes les équipes

for user in tree.xpath("/matches/match"):
	id_home = teams.index(user.find("home").text)
	id_away = teams.index(user.find("away").text)

	homeGoals = int(user.find("homeGoals").text)
	awayGoals = int(user.find("awayGoals").text)
	tmp = Fixtures(id_home, id_away, homeGoals, awayGoals)
	fixtures.append(tmp)

moy_fixtures = {}
for i in fixtures:
	tmp = i.getResult()
	if tmp[0] in moy_fixtures:
		moy_fixtures[tmp[0]] += tmp[1]
	else:
		moy_fixtures[tmp[0]] = tmp[1]




gps = {}
f = open("gps.data")
for i in f:
	tab = str.split(i, " ")
	team = tab[0]
	gps[team] = (tab[1], tab[2].rstrip('\n'))
# print(gps)



f = open("gephi_foot_moy.gexf", "wb")
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
graph.set("defaultedgetype", "directed")
graph.set("mode", "static")

attribute = etree.SubElement(graph, "attributes")
attribute.set("class", "edge")
attribute.set("mode", "static")

attr = etree.SubElement(attribute, "attribute")
attr.set("id", "0")
attr.set("title", "result")
attr.set("type", "string")

attributenode = etree.SubElement(graph, "attributes")
attributenode.set("class", "node")
attributenode.set("mode", "static")

longattr = etree.SubElement(attributenode, "attribute")
longattr.set("id", "0")
longattr.set("title", "longitude")
longattr.set("type", "double")


latattr = etree.SubElement(attributenode, "attribute")
latattr.set("id", "1")
latattr.set("title", "latitude")
latattr.set("type", "double")

nodes = etree.SubElement(root, "nodes")

counter = 0
for i in teams:
	team = etree.SubElement(nodes, "node")
	team.set("id", str(counter))
	team.set("label", i)
	attvalues = etree.SubElement(team, "attvalues")
	longattvalue = etree.SubElement(attvalues, "attvalue")
	longattvalue.set("for", "0")
	longattvalue.set("value", str(gps[i][0]))
	latattvalue = etree.SubElement(attvalues, "attvalue")
	latattvalue.set("for", "1")
	latattvalue.set("value", str(gps[i][1]))
	counter += 1

edges = etree.SubElement(root, "edges")
counter = 0
for i in moy_fixtures:
	fixture = etree.SubElement(edges, "edge")
	fixture.set("id", str(counter))
	fixture.set("source", str(i[0]))
	fixture.set("target", str(i[1]))

	attvalues = etree.SubElement(fixture, "attvalues")
	attvalue = etree.SubElement(attvalues, "attvalue")
	attvalue.set("for", "0")
	attvalue.set("value", str( moy_fixtures.get(i)))
	counter += 1


f.write(etree.tostring(root, pretty_print=True))



# example gephi gefx simple file
# <?xml version="1.0" encoding="UTF-8"?>
# <gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">
#     <meta lastmodifieddate="2009-03-20">
#         <creator>Gexf.net</creator>
#         <description>A hello world! file</description>
#     </meta>
#     <graph mode="static" defaultedgetype="directed">
#         <nodes>
#             <node id="0" label="Hello" />
#             <node id="1" label="Word" />
#         </nodes>
#         <edges>
#             <edge id="0" source="0" target="1" />
#         </edges>
#     </graph>
# </gexf>
