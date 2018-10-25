import plyvel
import sys
from q60 import createLDB

LDBPATH = '../../../data/artist.ldb'


if __name__ == '__main__':
    my_db = plyvel.DB(LDBPATH, create_if_missing=True)
    # createLDB(my_db)

    print(len([key for key, value in my_db if value == "Japan".encode("utf-8")]))

    my_db.close()
