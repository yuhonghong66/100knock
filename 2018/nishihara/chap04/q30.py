# coding: UTF-8
# 
# 形態素解析
# $ mecab -F"%m,%f[6],%f[1],%f[2]\n" neko.txt > neko.txt.mecab

tpl = ["surface", "base", "pos", "pos1"]

rst = []
ln = []
with open("../../../data/neko.txt.mecab", "r") as f:
    for l in f.readlines():
        if("EOS" in l):
            rst.append(ln)
            ln = []
        else:
            ln.append(dict(zip(tpl, l.rstrip().split(","))))
    print(rst)
