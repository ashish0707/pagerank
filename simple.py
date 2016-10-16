from collections import defaultdict

import math

from Webcrawler import Node

OutlinkSet = {}
ExplodedList = []

def createGraphFromList(inlinkPairList):
    inlink_graph = defaultdict(list)
    for k, v in inlinkPairList:
        inlink_graph[k].append(v)
    sorted(inlink_graph.items())
    return inlink_graph


def createInLinkPairsFromFile(filename):
    inlinkPairList = []

    with open(filename, "r") as ins:
        for line in ins:
            tempList = line.rstrip("\n").split(" ")
            url = tempList.pop(0)
            parentNode = Node(0,url)

            if parentNode not in ExplodedList:
                ExplodedList.append(parentNode)
            # create inlink pairs
            if tempList:
                inlinkPairList.extend(createPairs(parentNode, tempList))


    return inlinkPairList


def getNodeFromExplodedList(value):
    for node in ExplodedList:
        if node.url == value:
            return node




def createPairs(parentNode, childList):
    tempPairList = []
    for value in childList:
        if value not in OutlinkSet:
            OutlinkSet[value] = 1
        else:
            OutlinkSet[value] += 1

        tempNode = createNode(value)
        if tempNode not in ExplodedList:
            ExplodedList.append(tempNode)
            tempPairList.append((parentNode,tempNode))
        else:
            tempPairList.append((parentNode,getNodeFromExplodedList(value)))
    return tempPairList


def createNode(title):
    node = Node(0, title)
    node.setTitle(title)
    return node


def getSinkNodeList(ExplodedList,OutlinkSet):
    sinkNodeList = []
    for node in ExplodedList:
        if node.url not in OutlinkSet:
            sinkNodeList.append(node)
    return sinkNodeList


inlink_graph = createGraphFromList(createInLinkPairsFromFile("text.txt"))
sinkNodeList = getSinkNodeList(ExplodedList,OutlinkSet)
from Pagerank import Pagerank
myPagerank = Pagerank()
page_rank_node_list = myPagerank.calcuatePageRank(ExplodedList,sinkNodeList,inlink_graph,OutlinkSet)
myPagerank.store_pagerank("testing_page_Rank.txt",page_rank_node_list)