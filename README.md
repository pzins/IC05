# IC05-foot-L1
match L1 last 4 seasons


## l1_foot : Present graph view of L1 match
- 2012/2013
- 2013/2014
- 2041/2015
- 2015/2016


An oriented edge from team A to team B
- if the result attribute is > 0 : A have more victory against B
- if the result attribute is < 0 : B have more victory against A
- if the result attribute is = 0 : A and B have equal victories/defeats/draws

<b>Example</b> : Lyon ------> Nice
an edge result attribute = 2

- it means that LYON have a score of 2 :
- so for matchs : Lyon - Nice or Nice - Lyon
- it could be 2 victories for Lyon and 0 defeat and 2 draws
- or 3 victories for Lyon and 1 defeat and 0 draw
- or ...
- <b>the global result is +2 for Lyon</b>


## wikipedia
- Scraping data from Wikipedia
- Follow every link in the wikipedia page
- Start with one or several page at the beginning
- Give a graph view with links between related words
