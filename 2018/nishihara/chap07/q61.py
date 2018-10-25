import plyvel
import sys
from q60 import createLDB

LDBPATH = '../../../data/artist.ldb'


# 引数に指定したアーティスト名の活動場所を取り出す
# 引数省略すると全て取り出す

if __name__ == '__main__':
    my_db = plyvel.DB(LDBPATH, create_if_missing=True)
    # createLDB(my_db)

    argc = len(sys.argv)
    if(argc == 1):
        for key, value in my_db:
            print("{} => {}".format(key.decode('utf-8'), value.decode('utf-8')))
    else:
        for key in sys.argv[1:]:
            print("{} => {}".format(key, my_db.get(key.encode("utf-8")).decode("utf-8")))
