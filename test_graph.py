from collections import defaultdict

import math

from InlinkGenerator import InlinkGenerator
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
ExplodedList.append(D)
ExplodedList.append(E)
ExplodedList.append(F)
ExplodedList.append(B)
ExplodedList.append(C)



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

print "ExplodedList : \n"
for node in ExplodedList:
    print node.url


print "Inlink graph : \n"
for key,value in inlink_graph.items():
    print key.url + " :=> "
    for v in value:
        print v.url + " "
    print "\n"

sinkNodeList=[]


def calcuatePageRank(ExplodedList, sinkNodeList, inlink_graph, dampingFactor=0.85):
    N = len(ExplodedList);
    print "inlink graph size :=> %d , ExplodedGraph Size : %d" % (len(inlink_graph), N)

    for node in ExplodedList:
        node.setPageRank(1.0 / N)

    while myCrawler.isConvergenceReached():
        sinkPR = 0

        for node in sinkNodeList:
            sinkPR += node.pageRank

        for node in ExplodedList:
            node.newPageRank = (1 - dampingFactor) / N
            node.newPageRank += dampingFactor * sinkPR / N


            for childnode in inlink_graph[node]:
                print "node.newPageRank %f" %node.newPageRank
                print "ChildNode Url :==>" + childnode.url
                print "ChildNode pageRank :==> %f" % childnode.pageRank
                print "childnode.numberOfOutlinks :==> %f" %childnode.numberOfOutlinks
                print "D* childnode.pageRank / childnode.numberOfOutlinks :==> %f" % (dampingFactor * childnode.pageRank / childnode.numberOfOutlinks)
                node.newPageRank += dampingFactor * childnode.pageRank / childnode.numberOfOutlinks
                print "new pagerank %f" % node.newPageRank

        sEntrophy = 0
        for node in ExplodedList:
            node.pageRank = node.newPageRank

        for node in ExplodedList:
            sEntrophy += node.pageRank * math.log(node.pageRank, 2.0)

        myCrawler.perprexity.append((2 ** (sEntrophy * -1)))

    return ExplodedList

myCrawler.store_pagerank("test_pagerank.txt",
                         calcuatePageRank(ExplodedList, sinkNodeList, inlink_graph))

