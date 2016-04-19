from lxml import etree

categories = []
links = []



f = open("resultat_1h30")
# g = open("test", "w")
for i in f:
	tab = i.partition(";")
	#tab = str.split(i, ";")

	if not tab[0] in categories:
		categories.append(tab[0])
	if not tab[2].rstrip() in categories:
		categories.append(tab[2].rstrip())

# for i in categories:
# 	print(i)
# 	g.write(i + "\n")
# f.close()
# g.close()


f = open("resultat_1h30")
for i in f:
	tab = i.partition(";")
	if (tab[0] in categories) and (tab[2].rstrip() in categories):
		src = categories.index(tab[0])
		dst = categories.index(tab[2].rstrip())
		links.append((src, dst))
# print(nodes)



f = open("amazon_gephi.gexf", "wb")
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

attribute = etree.SubElement(graph, "attributes")
attribute.set("class", "edge")
attribute.set("mode", "static")

attributenode = etree.SubElement(graph, "attributes")
attributenode.set("class", "node")
attributenode.set("mode", "static")

nodes = etree.SubElement(root, "nodes")

counter = 0
for i in categories:
	node = etree.SubElement(nodes, "node")
	node.set("id", str(counter))
	node.set("label", i)
	counter += 1

edges = etree.SubElement(root, "edges")
counter = 0
for i in links:
	link = etree.SubElement(edges, "edge")
	link.set("id", str(counter))
	link.set("source", str(i[0]))
	link.set("target", str(i[1]))
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
