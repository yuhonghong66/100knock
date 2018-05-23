# 係り受け解析
# cabocha -f3 neko.txt -o neko.txt.cabocha

import xml.etree.ElementTree as ET
import q40

class Morph:
    """形態素を表すクラス"""
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    # (surface,base,pos,pos1)
    def __str__(self):
        return "(" + ",".join([self.surface, self.base, self.pos, self.pos1]) + ")"


class Chunk:
    """文節を表すクラス"""
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    # dst,srcs: Morph(),...
    def __str__(self):
        return "{},{}: ".format(self.dst, self.srcs) + \
               ", ".join([str(s) for s in self.morphs])


if __name__ == '__main__':
    root = q40.readXML("../../../data/neko.txt.cabocha")
    rst = []
    for s in root:
        sentence = []
        for c in s:
            chunk = Chunk([], int(c.get("link")), [])
            for t in c:
                a = q40.getbpp(t.get("feature"))
                chunk.morphs.append(Morph(t.text, *a))
            sentence.append(chunk)
        for i,chunk in enumerate(sentence):
            if chunk.dst != -1:
                sentence[chunk.dst].srcs.append(i)
        rst.append(sentence)

    for i,t in enumerate(rst[7]):
        print(i,t)
