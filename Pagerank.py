from collections import defaultdict

import math


class Pagerank:

    def __init__(self):
        pass

    inlink_list = [];
    perprexity = []
    sinkNodeList = []
    inlink_graph = defaultdict(list)
    PAGERANK = "pagerank.txt"
    SKEW_THREASHOLD = 1
    INLINKFILE = "inlinks.txt"

    def calcuatePageRank(self,ExplodedList, sinkNodeList, inlink_graph, OutLinkSet, dampingFactor=0.85):
        N = len(ExplodedList);
        print "inlink graph size :=> %d , ExplodedGraph Size : %d" % (len(inlink_graph), N)

        for node in ExplodedList:
            node.setPageRank(1.0 / N)

        while self.isConvergenceReached():
            sinkPR = 0

            for node in sinkNodeList:
                sinkPR += node.pageRank

            for node in ExplodedList:
                node.newPageRank = (1 - dampingFactor) / N
                node.newPageRank += dampingFactor * sinkPR / N

                for childnode in inlink_graph[node]:
                    # print "node.newPageRank %f" % node.newPageRank
                    # print "ChildNode Url :==>" + childnode.url
                    # print "ChildNode Pagerank :==> %f" % childnode.pageRank
                    # print "OutLinkSet[node.url] :==> %f" % OutLinkSet[childnode.url]
                    # print "D* childnode.pageRank / OutLinkSet[node.url] :==> %f" % (
                    # dampingFactor * childnode.pageRank / OutLinkSet[childnode.url])
                    node.newPageRank += dampingFactor * childnode.pageRank / OutLinkSet[childnode.url]
                    # print "new pagerank %f" % node.newPageRank

            sEntrophy = 0
            for node in ExplodedList:
                node.pageRank = node.newPageRank

            for node in ExplodedList:
                sEntrophy += node.pageRank * math.log(node.pageRank, 2.0)

            self.perprexity.append((2 ** (sEntrophy * -1)))

        return ExplodedList

    def isConvergenceReached(self):
        if len(self.perprexity) < 4:
            return True
        else:
            print self.perprexity
            temp = any([((self.perprexity[i + 1] - self.perprexity[i]) > self.SKEW_THREASHOLD)
                        for i in range(len(self.perprexity) - 1)])
            self.perprexity = []
            return temp

    def store_pagerank(self, title_of_file, ExplodedList):
        for node in ExplodedList:
            self.save_to_file(title_of_file, node.title + " ==> " + str(node.pageRank) + "\n")


    def save_to_file(self, title, raw_data):
        with open(title, 'a') as _file_:
            _file_.write(raw_data)