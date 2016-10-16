from collections import defaultdict

from task1 import InlinkGenerator
from Webcrawler import Node


url = "https://en.wikipedia.org/wiki/Sustainable_energy"
myCrawler = InlinkGenerator(url)

A = Node(0, 'a')
A.setNoOfOutlinks(3)
A.setTitle('A')

B = Node(0, 'b')
B.setNoOfOutlinks(4)
B.setTitle('B')

C = Node(0, 'c')
C.setNoOfOutlinks(2)
C.setTitle('C')

D = Node(0, 'd')
D.setNoOfOutlinks(4)
D.setTitle('D')

E = Node(0, 'e')
E.setNoOfOutlinks(1)
E.setTitle('E')

F = Node(0, 'f')
F.setNoOfOutlinks(3)
F.setTitle('F')

ExplodedList = []
ExplodedList.append(A)
ExplodedList.append(B)
ExplodedList.append(C)
ExplodedList.append(D)
ExplodedList.append(E)
ExplodedList.append(F)

inLink = []
inLink.append((A,D))
inLink.append((A,E))
inLink.append((A,F))
inLink.append((B,A))
inLink.append((B,F))
inLink.append((C,A))
inLink.append((C,B))
inLink.append((C,D))
inLink.append((D,B))
inLink.append((D,C))
inLink.append((E,B))
inLink.append((E,C))
inLink.append((E,D))
inLink.append((E,F))
inLink.append((F,A))
inLink.append((F,B))
inLink.append((F,D))

inlink_graph = defaultdict(list)
for k, v in inLink:
    inlink_graph[k].append(v)

sorted(inlink_graph.items())
print inlink_graph
sinkNodeList=[]

myCrawler.store_pagerank("test_pagerank.txt", myCrawler.calcuatePageRank(ExplodedList, sinkNodeList, inlink_graph))

