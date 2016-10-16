import os
import sys
import fileinput
from collections import defaultdict


class Node:

    inlinks = []
    title = ""
    numberOfOutlinks = 0
    pageRank = 0.0;
    newPageRank = 0.0;

    def __init__(self, depth, url):
        self.depth = depth
        self.url = url

    def __eq__(self, node):
        if self.url == node.url:
            return True
        return False

    def addInlink(self,node):
        self.inlinks.append(node)

    def setTitle(self, title):
        self.title = title

    def setNoOfOutlinks(self,count):
        self.numberOfOutlinks = count

    def setPageRank(self,rank):
        self.pageRank = rank

    def setNewPageRank(self, rank):
        self.pageRank = rank

    def __hash__(self):
        return hash(self.url)

tempList = [Node(1 , "abc"),Node(1 , "abcd"),Node(1 , "abce")]
print Node(2, "abc") in tempList
print tempList.index(Node(2, "abce"))

temp = defaultdict(int)
temp = {'ash' : 1 , "bul" : 2}
if 'bul' in temp:
    print "ash is present"


