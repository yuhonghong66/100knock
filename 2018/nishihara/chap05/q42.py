import re
from q40 import Morph
from q41 import Chunk, getChunks


def add_instatnce(cls, method):
    setattr(cls, method.__name__, method)

def get_surface(self):
    return "".join([re.sub("[。、,.]", "", m.surface) for m in self.morphs])

add_instatnce(Chunk, get_surface)




if __name__ == '__main__':
    rst = getChunks("../../../data/neko.txt.cabocha")

    for s in rst:
        for c in s:
            if(c.dst != -1):
                print(c.get_surface() + "\t" + s[c.dst].get_surface())
