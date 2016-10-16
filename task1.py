from InlinkGenerator import InlinkGenerator


def start(self):
    url = "https://en.wikipedia.org/wiki/Sustainable_energy"
    myCrawler = InlinkGenerator(url)
    myCrawler.set_pages_to_crawl(5)
    myCrawler.setFileName("task1.txt")
    myCrawler.addToMandatoryList('/wiki/')
    myCrawler.addToDisallowedList(':')
    myCrawler.start()
    myCrawler.process_inlinks()
    myCrawler.store_pagerank("pagerank.txt", myCrawler.getPageRank())