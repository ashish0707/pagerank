import math
from Webcrawler import Crawler
from collections import defaultdict
from Webcrawler import Node




class InlinkGenerator(Crawler):

    inlink_list = [];
    perprexity = []
    sinkNodeList = []
    inlink_graph = defaultdict(list)
    PAGERANK = "pagerank.txt"
    SKEW_THREASHOLD = 1
    INLINKFILE = "inlinks.txt"

    def add_pairs_inlinks_list(self, parentnode, wikilist):

            if wikilist:
                for node in wikilist:
                    self.inlink_list.append((node, parentnode))
            else:
                self.sinkNodeList.append(parentnode)

            parentnode.setNoOfOutlinks(len(set(wikilist)))

    def process_inlinks(self):

        for k, v in self.inlink_list:
            self.inlink_graph[k].append(v)

        sorted(self.inlink_graph.items())
        print "lenght is inlink graph is %d" %(len(self.inlink_graph))
        print "lenght is Exploded graph is %d" % (len(self.ExplodedList))

        for node in self.ExplodedList:
            self.save_to_file(self.INLINKFILE,
                                  node.title + " " + self.getChildNodeString(self.inlink_graph[node]) + "\n")

    def getChildNodeString(self, childNodeList):

        tempstring = ""
        for x in (list(set(childNodeList))):
            tempstring += x.url[30:].replace(" ", "-") + " "
        return tempstring

    def save_to_file(self, title, raw_data):
                    with open(title, 'a') as _file_:
                        _file_.write(raw_data)



    def calcuatePageRank(self, ExplodedList , sinkNodeList , inlink_graph, dampingFactor = 0.85 ):


        N = len(ExplodedList);
        print "inlink graph size :=> %d , ExplodedGraph Size : %d" %(len(inlink_graph),N)

        for node in ExplodedList:
            node.setPageRank(1.0/ N)

        while self.isConvergenceReached():
            sinkPR = 0

            for node in sinkNodeList:
                sinkPR += node.pageRank

            for node in ExplodedList:
                node.newPageRank = (1 - dampingFactor) / N
                node.newPageRank += dampingFactor * sinkPR / N
                print "newpageRank for " + node.title + "%f" %node.newPageRank
                for childnode in inlink_graph[node]:
                    node.newPageRank += dampingFactor * childnode.pageRank / childnode.numberOfOutlinks

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
            temp = any([((self.perprexity[i+1] - self.perprexity[i]) > self.SKEW_THREASHOLD)
                        for i in range(len(self.perprexity)-1)])
            self.perprexity = []
            return temp

    def getPageRank(self):
        return self.calcuatePageRank(self.ExplodedList,self.sinkNodeList,self.inlink_graph)

    def store_pagerank(self,title_of_file, ExplodedList):
        for node in ExplodedList:
            self.save_to_file(title_of_file, node.title + " ==> " + str(node.pageRank) + "\n")


url = "https://en.wikipedia.org/wiki/Sustainable_energy"
myCrawler = InlinkGenerator(url)
myCrawler.set_pages_to_crawl(5)
myCrawler.setFileName("task1.txt")
myCrawler.addToMandatoryList('/wiki/')
myCrawler.addToDisallowedList(':')
myCrawler.start()
myCrawler.process_inlinks()
myCrawler.store_pagerank("pagerank.txt", myCrawler.getPageRank())

