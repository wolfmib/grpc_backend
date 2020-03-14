from pymongo import MongoClient
import uuid
import pprint

def rough_print_all_keys(db_collection):
    # document = db.collection_name.find_one()
    # for k in document:
    # print(k)
    document = db_collection.find_one()
    for k in document:
        print(k)

# Link: who can help me finish that....
    #  https://www.geeksforgeeks.org/reduce-in-python/
    #  https://www.objectrocket.com/blog/how-to/get-keys-mongodb-collection/


def check_all_unikeys(db):
    pass


def query_by_uuid():

    print("[Jason]:  Please input Mongo Client Address:")
    print("Example:  mongodb://localhost:27017/")
    mongo_addr = input()

    client = MongoClient(mongo_addr)

    print("[Jason]: Please select db_name")
    print("Example: user_db")
    db_name = input()
    db = getattr(client, db_name)

    print("[Jason]:  Please input the collection name")
    print("Example:  user_collection")
    print("-----------------------------------")
    print(db.collection_names())
    print("---------------------------------------")
    collection_name = input()
    db_collection = getattr(db, collection_name)

    # Check all keys:
    print("-----------------------------")
    rough_print_all_keys(db_collection)
    print("-----------------------------")

    # Getattr Code Referenced
    # x = getattr(t, 'attr1')
    # setattr(t, 'attr1', 21)
    print("[Jason]:  Please input the col_name and match value you want to query")
    print("Example:  user_id   /    13")
    query_name = input("col_name:        ")
    query_type = int(input("value type:      0: str, 1: int\n"))
    if query_type == 0:
        query_value = input("Value: \n")
    elif query_type == 1:
        query_value = int(input("Value: \n"))
    else:
        print("There is no this type:   %d" % query_type)

    db_cur = db_collection.find({query_name: query_value})
    _tem = db_cur.next()
    pprint.pprint(_tem)


if __name__ == "__main__":
    query_by_uuid()
