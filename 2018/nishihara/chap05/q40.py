# 係り受け解析
# cabocha -f3 neko.txt -o neko.txt.cabocha

import xml.etree.ElementTree as ET

class Morph:
    """形態素を表すクラス"""
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return ",".join([self.surface, self.base, self.pos, self.pos1])


with open("../../../data/neko.txt.cabocha") as f:
    XmlData = f.read()
    root = ET.fromstring("<root>{}.</root>".format(XmlData))
    rst = []
    for s in root:
        sentence = []
        for c in s:
            for t in c:
                a = t.get("feature").split(",")
                sentence.append(Morph(t.text, a[6], a[0], a[1]))
        rst.append(sentence)

    for t in rst[3]:
        print(t)

