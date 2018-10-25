import plyvel
import json

JSONPATH = "../../../data/artist.json"
LDBPATH = '../../../data/artist.ldb'


def createLDB(db):
    with open(JSONPATH, "r") as f:
        for l in f.readlines():
            d = json.loads(l)
            if("name" in d and "area" in d):
                db.put(d["name"].encode('utf-8'), d["area"].encode('utf-8'))


if __name__ == '__main__':
    my_db = plyvel.DB(LDBPATH, create_if_missing=True)
    createLDB(my_db)

    for key, value in my_db:
        print('%s => %s' % (key.decode('utf-8'), value.decode('utf-8')))

    my_db.close()
