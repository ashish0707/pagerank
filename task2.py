from InlinkGenerator import InlinkGenerator

FileName = "text.txt"
url = "https://en.wikipedia.org/wiki/Sustainable_energy"
generator = InlinkGenerator(url)
inlinkPairList = generator.createInlinkPairsFromFile(FileName)
inlink_graph = generator.createGraphFromList(inlinkPairList)





