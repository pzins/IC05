# Projet IC05

## amazon

### Description:
This projet consists of two part:
* First, the data has to be scraped from an online store in order to build links between items.
* Secondly, the data has to be reprensented as a graph.

### Members:
* Daniel Artchounin
* Camil Sadiki
* Pierre Zins


## l1_foot

### L1 matches of the last 4 seasons

- 2012/2013
- 2013/2014
- 2041/2015
- 2015/2016


An oriented edge from team A to team B
- if the result attribute is > 0 : A have more victory against B
- if the result attribute is < 0 : B have more victory against A
- if the result attribute is = 0 : A and B have equal victories/defeats/draws


### files : 
- gps.data : GPS coordinate of French L1 cities
- foot.py : scrap data about L1 results
- format.py : create GEFX file with GPS coordinate from data scraped
- data_l1.xml : data scraped about L1 results
- gephi_data_l1.gexf : formatted data
- l1_moyenne.gephi : result L1 mean (victory, defeat, draw)



## wikipedia
- Scraping data from Wikipedia
- Visit every links in the wikipedia page
- Start with one or several key pages
- Give a graph view with links between related words


