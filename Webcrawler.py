from urllib import urlopen
from bs4 import BeautifulSoup
from bfs import BFS
import time


class Node:

    inlinks = []
    title = ""
    numberOfOutlinks = 0
    pageRank = 0.0
    newPageRank = 0.0

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

    def __str__(self):
        return self.title


class Crawler:

    url = ''
    ExplodedList = []
    traversed_list = []
    MandatoryList = []
    Dis_Allowed_List = []
    FOCUSED_TEXT = ''
    delay = 0
    PAGES_TO_CRAWL = 1000

    def __init__(self, url, searcher = BFS()):
        self.mySearcher = searcher
        self.fileName = searcher.name
        self.url = url


    def process_wiki_url(self, depth, list_of_url):
        tempList = []
        for value in list_of_url:
            if self.filter_url(value):
                if "https" in value[1]:
                    tempList.append(Node(depth, value[1]));
                else:
                    tempList.append(Node(depth, "https://en.wikipedia.org" + value[1]));
        return tempList

    def filter_url(self,value):
        if (all(x in value[1].lower() for x in self.MandatoryList)
            and not any(x in value[1] for x in self.Dis_Allowed_List)
            and (self.FOCUSED_TEXT in value[0].lower() or self.FOCUSED_TEXT in value[1].lower())):
            return True
        else:
            return False

    def store_webpage(self, title, raw_data):
        with open(title, 'a') as _file_:
            _file_.write(raw_data)

    def get_soup(self,url):
        raw_data = urlopen(url).read()
        rawSoup = BeautifulSoup(raw_data, 'html.parser')
        return rawSoup

    def extract_url_list(self,raw):
        list_of_url = [(url.text ,str(url.get('href'))) for url in raw.find_all('a')]
        return list_of_url

    def set_searcher(self, searcher):
        self.mySearcher = searcher

    def setFileName(self,name):
        self.fileName = name

    def start(self):
        counter = 0
        parent_node = Node(1, self.url)
        wikilist = []
        self.traversed_list.append(parent_node)
        while counter < self.PAGES_TO_CRAWL and (len(self.traversed_list) > 0):
            time.sleep(self.delay)
            try:
                node = self.traversed_list.pop(0)
                if node not in self.ExplodedList:
                    print node.url
                    if node.depth < 5:
                        soup = self.get_soup(node.url)
                        node.setTitle(node.url[30:])
                        wikilist = self.process_wiki_url(node.depth+1, self.extract_url_list(soup))
                        # print "lenght of wikilist is %d" % (len(wikilist))
                        # print "lenght of traversed List is %d" % (len(self.traversed_list))
                        # print "depth is %d" % node.depth
                        self.traversed_list = self.mySearcher.merge_list(self.traversed_list, wikilist)

                    # store_webpage(rawSoup.title.string, raw_data);
                    self.store_webpage(self.fileName, node.url + "\n")
                    self.ExplodedList.append(node)
                    self.add_pairs_inlinks_list(node, wikilist)
                    counter += 1

            except Exception as inst:
                print inst.message
                break
            finally:
                print counter

        self.inlinksToOutputStream();

    def addToMandatoryList(self, value):
        self.MandatoryList.append(value)

    def addToDisallowedList(self, param):
        self.Dis_Allowed_List.append(param)

    def setFocusedText(self, value):
        self.FOCUSED_TEXT = value

    def setDelay(self, delay):
        self.delay = delay

    def add_pairs_inlinks_list(self, node, wikilist):
        pass

    def inlinksToOutputStream(self):
        pass

    def set_pages_to_crawl(self,count):
        self.PAGES_TO_CRAWL = count

    def getNode(self, url):
        return self.ExplodedList[self.ExplodedList.index(Node(0, url))]