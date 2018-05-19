# coding: UTF-8
from matplotlib import pyplot
import q30

mor = q30.readma("../../../data/neko.txt.mecab")
wdict = {}
hdict = {}

for s in mor:
    for m in s:
        w = (m["base"], m["pos"])
        wdict[w] = wdict[w] + 1 if w in wdict else 1

for v in wdict.values():
    hdict[v] = hdict[v] + 1 if v in hdict else 1

rst = sorted(hdict.items(), key=lambda x: -x[1])

pyplot.bar([t[0] for t in rst], [t[1] for t in rst], align="center")
pyplot.show()
