# ADM_HW5

<p align="center">
  <img src="https://camo.githubusercontent.com/e19c873d53f273528653c1c1f577689464f844859e364cbf6e1c9c65a37c8472/68747470733a2f2f63727970746f6272696566696e672e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031382f30342f57696b6970656469612d616e642d526571756573742d4e6574776f726b2d656e61626c652d646f6e6f72732d746f2d646f6e6174652d696e2d63727970746f63757272656e63792e6a7067" />
</p>


In this Homework we analyse the Wikipedia's hyperlinks network. 

The model provides that the articles are nodes of the network, connected through links (edges).<br> 
The articles are characterized by the category they belong to.
Looking at the categories of the articles, we analyze important characteristics of the network, such as the reachability, the distance between nodes, the ranking of categories based on the PageRank.

The work is based on the web graph of Wikipedia hyperlinks provides by the Stanford Network Analysis Project [here](https://snap.stanford.edu/data/wiki-topcats.html).
The resource also gives the page names of the articles and the categories of the articles.

## Datasets:

1. the reduced version of the [web graph](https://drive.google.com/file/d/1QVt0aMOFvLjOEm5eKeCxBQUwIU30_NIh/view?usp=sharing).
2. ```wiki-topcats-categories.txt.gz``` datset of the categories of the articles.
3. ```wiki-topcats-page-names.txt.gz``` dataset of names of the articles.

2 and 3 are available on the [SNAP page](https://snap.stanford.edu/data/wiki-topcats.html).

## Content of the repository:

1) ***```main.ipynb```***
contains answers to research questions and the implemented algorithms.<br>
[Click here](https://nbviewer.jupyter.org/github/AlessandradellaFazia/ADM_HW5/blob/main/main.ipynb) to visualize the notebook.
2) ***```functions.py```***
contains all used functions.

## Analysis topics:
Precisely the analysis consists of:

1) Build the graph G=(V, E), where V is the set of articles and E the hyperlinks among them. Provides basic information as: number of articles, number of hyperlinks, the graph density, the nodes' degree distribution.
2) Given a page v and a number of clicks d, provides the set of all pages reachable within d clicks. 
3) Given a category C, considering the set of pages in C p = {p1, ..., pn}, provides the minimum number of clicks required to reach all pages in p, starting from the page v, where v is  corresponding to the most central article in C.
4) Given two categories: C1 and C2, looking at the subgraph constituted by the articles in the two categories and considering two arbitrary pages U and V in the subgraph, tells what is the minimum set of hyperlinks one can remove to disconnect U and V.
5) Given an arbitrary category C0, provides the list of remaning categories sorted by their distance from C0. The distance between two categories is defined as:

    distance(C0, Ci) = median(ShortestPath(C0, Ci))

    where ShortestPath(C0, Ci) is the set of shortest paths from each pair of nodes in the two categories.

6) Rank the categories in the graph according to their PageRank (PR).

More details in the [delivery](https://github.com/CriMenghini/ADM/blob/master/2020/Homework_5/README.md) of the project.

### People:
- Mirko Lozzi 
- Lorenzo Petroni 
- Alessandra della Fazia 
