import requests
from bs4 import BeautifulSoup


urls = [("Ordinateurs portables","http://www.amazon.fr/Asus-Chromebook-C200MA-KX017-Portable-Celeron/dp/B0105LFO3G/ref=sr_1_4?s=computers&ie=UTF8&qid=1459258627&sr=1-4&keywords=pc")]


class Category:
	def __init__(self):
		self.keywords = []
	
	def addWords(self, w):
		self.keywords.append(w)	

	def __str__(self):
		res = ""
		for i in self.keywords:
			res += i + " "
		return res

class Node:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def __eq__(self, other):
		return (isinstance(other, self.__class__) and self.name == other.name)

nodes = []

edges = []
# n = Node("name")
# m = Node("aaaname")
# r = Node("namsdfe")
# nodes.append(n)
# nodes.append(m)
# nodes.append(r)
# print(nodes)
# print(nodes.index('aaaname'))
# exit()

counter = 0
while len(urls) != 0:
	prev_cate = urls[0][0]
	url = urls[0][1]
	urls.pop(0)
	# print(url)
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	# print(soup.prettify())
	# div = soup.find_all("div", {"aria-hidden":"true"})
	# div = soup.find_all("div", {"class":"p13n-sc-truncated"})
	div = soup.find_all("li", {"class":"a-carousel-card"})
	cate = soup.find("ul", {"class":"a-horizontal a-size-small"})
	cates = cate.find_all("a")
	
	# category = Category()

	category = cates[-1].text.strip()
	n = Node(category)
	if not n in nodes:
		nodes.append(n)
	
	edges.append((prev_cate, category))

	# for i in cates:
	# 	category = i.text.strip()
	# 	# category.addWords(i.text.strip())
	# 	n = Node(category)
	# 	print(n)
	# 	if not n in nodes:
	# 		nodes.append(n)

	for i in div:
		# print(i)
		link = i.find("a")
		txt_link = link.get("href")
		# print(link.get('href'))
		urls.append((category, "http://www.amazon.fr" + txt_link))
	if counter == 100:
		break
	counter += 1
	
print(nodes)
print(edges)

print(tab)




# urls = ["http://www.amazon.fr/gp/site-directory/ref=nav_shopall_btn"]



# url = urls[0]
# r = requests.get(url)
# soup = BeautifulSoup(r.content)
# body = soup.find("table", {"id": "shopAllLinks"})
# h2 = body.find_all("li");

# for i in h2:
# 	print(i.text)
# exit();