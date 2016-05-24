import requests
from bs4 import BeautifulSoup
import time
from random import randint

	
# urls visités
old_urls = []

# file
# urls = [("Ballons", "B0116Q6U5U","https://www.amazon.fr/adidas-Replique-Ballon-Bright-Indigo/dp/B0116Q6U5U/ref=lp_339893031_1_1?s=sports&ie=UTF8&qid=1462282939&sr=1-1")]
# urls = [("Smartphones et téléphones portables débloqués", "B0168FGZR2","https://www.amazon.fr/Doogee-X5-Smartphone-D%C3%A9bloqu%C3%A9-Op%C3%A9rateur/dp/B0168FGZR2/ref=sr_1_1?s=electronics&ie=UTF8&qid=1462383104&sr=1-1&keywords=smartphone")]
urls = [("Ordinateurs portables", "B0105LFO3G","http://www.amazon.fr/Asus-Chromebook-C200MA-KX017-Portable-Celeron/dp/B0105LFO3G/ref=sr_1_4?s=computers&ie=UTF8&qid=1459258627&sr=1-4&keywords=pc")]




#load file à partir du fichier de sauvegarde
savedFile = open("saveFile", 'r')
urls = []
for i in savedFile:
	elements = i.split("*")
	urls.append((elements[0], elements[1], elements[2].strip()))

#load old_urls already visited
savedFile = open("saveOldUrls", 'r')
for i in savedFile:
	old_urls.append(i.strip())


try:
	nodes = []
	edges = []

	# fichier sortie
	f = open('tmp_res.txt','w')
	
	counter = 0
	while len(urls) != 0:
	
		# delai attente au bout de 100 itérations
		counter += 1
		if counter % 100 == 0:
			random = randint(0, 100)
			time.sleep(random)
		print("sizeFile = " + str(len(urls)))
		# catégorie du lien début de file
		prev_cate = urls[0][0]
		# reference du lein debut file
		prev_ref = urls[0][1]
		# url début de file
		url = urls[0][2]
		# pop file
		urls.pop(0)
	
		# si le lien a déjà été visité => itération suivante
		if url in old_urls:
			continue
		# ajout du nouveau lien dans la file
		old_urls.append(url)
	
		#recupération de la reference
		begin = url.find("dp")
		begin += 3
		end1 = url.find("/", begin)
		end2 = url.find("?", begin)
		end = min(end1, end2)
		if end < 0:
			end = max(end2, end1)
		ref = url[begin:end]
	
	
		r = requests.get(url)
		soup = BeautifulSoup(r.content, "html.parser")
		try:
			#object souvent achetés
			div = soup.find_all("li", {"class":"a-carousel-card"})
	
			#catégorie de page courante
			cate = soup.find("ul", {"class":"a-horizontal a-size-small"})
			cates = cate.find_all("a")
			# cates : différent niveau de catégorie (on veutl le dernier)
			# récupération de la vraie catégorie
			category = cates[-1].text.strip()
	
			# si la catégorie de la page est la même que celle de l'objet qui nous a fait arrivé sur cette page, on l'ignore
			#counter > 1 : sinon probleme à première itération
			if category == prev_cate and counter > 1:
				continue


			# si pas déjà ajout de new category dans les nodes 
			if not category in nodes:
				nodes.append(category)

		
			#ajout edge
			edges.append((prev_cate, category))
			#write edge to file
			s = prev_ref + ";" + ref + ";" + prev_cate + ";" + category + "\n"
			f.write(s)

			#ajout des autres liens dans la file
			for i in div:
				link = i.find("a")
				txt_link = link.get("href")
				urls.append((category, ref, "http://www.amazon.fr" + txt_link))

		except:
			print('No link in this page')
	f.close()




except KeyboardInterrupt:
    print("W: interrupt received, stopping…")
finally:
    # save urls in a file
	saveFile = open("saveFile", 'w')
	for i in urls:
		writeStr = i[0] + "*" + i[1] + "*" + i[2] + "\n"
		saveFile.write(writeStr)
	saveFile.close()

	# save urls already visited
	saveFile = open("saveOldUrls", 'w')
	for i in old_urls:
		writeStr = i + "\n"
		saveFile.write(writeStr)
	saveFile.close()