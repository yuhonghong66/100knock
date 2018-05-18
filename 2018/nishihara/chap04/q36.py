# coding: UTF-8

import q30

mor = q30.readma("../../../data/neko.txt.mecab")
wdict = {}

for s in mor:
    for m in s:
        w = (m["base"], m["pos"])
        wdict[w] = wdict[w] + 1 if w in wdict else 1

rst = sorted(wdict.items(), key=lambda x: -x[1])
for t in rst:
    print(t[1], t[0][0])
