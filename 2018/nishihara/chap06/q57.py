from graphviz import Digraph
from q53 import *


def xml2dict(xml):
    d = {}
    for e in xml:
        d[e.tag] = e.text
    return d

if __name__ == '__main__':
    root = readXML("../../../data/nlp.txt.xml")




    for i,d in enumerate(root.findall(".//dependencies[@type='collapsed-dependencies']")):
        G = Digraph(format='png')
        G.attr('edge', dir='back')
        for dep in d:
            G.edge(dep[0].text, dep[1].text)
        G.render("q57/tree{}".format(i))
