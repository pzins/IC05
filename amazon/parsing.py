from lxml import etree

input_file = "resultat_1h30"
output_file = "amazon_gephi2.gexf"


# categories == nodes
categories = []
# links == edges
links = []


#fichier avec les données
f = open(input_file)
#récupération des catégories == nodes
for i in f:
	tab = i.partition(";")
	if not tab[0] in categories:
		categories.append(tab[0])
	if not tab[2].rstrip() in categories:
		categories.append(tab[2].rstrip())

f.close();

f = open(input_file)
#récupération des edges
for i in f:
	tab = i.partition(";")
	if (tab[0] in categories) and (tab[2].rstrip() in categories):
		src = categories.index(tab[0])
		dst = categories.index(tab[2].rstrip())
		links.append((src, dst))


#fichier de sortie
f = open(output_file, "wb")

#ajout de l'entete
# debut ==========================================================================
f.write(bytes("<?xml version='1.0' encoding='UTF-8'?>", 'UTF-8'))
root = etree.Element("gexf")
root.set("xmlns", "http://www.gexf.net/1.2draft")
root.set("version", "1.2")

meta = etree.SubElement(root, "meta")
meta.set("lastmodifieddate", "2009-03-20")

creator = etree.SubElement(meta, "creator")
creator.text = "Gexf.net"

description = etree.SubElement(meta, "description")
description.text = "description"

graph = etree.SubElement(root, "graph")
graph.set("defaultedgetype", "undirected")
graph.set("mode", "static")

attribute = etree.SubElement(graph, "attributes")
attribute.set("class", "edge")
attribute.set("mode", "static")

attributenode = etree.SubElement(graph, "attributes")
attributenode.set("class", "node")
attributenode.set("mode", "static")
# fin entete ==========================================================================


#ajout des nodes
nodes = etree.SubElement(root, "nodes")

counter = 0
for i in categories:
	node = etree.SubElement(nodes, "node")
	node.set("id", str(counter))
	node.set("label", i)
	counter += 1


#ajout des edges
edges = etree.SubElement(root, "edges")
counter = 0
for i in links:
	link = etree.SubElement(edges, "edge")
	link.set("id", str(counter))
	link.set("source", str(i[0]))
	link.set("target", str(i[1]))
	counter += 1


#ecriture dans le fichier
f.write(etree.tostring(root, pretty_print=True))



# example gephi gefx simple file
#
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
