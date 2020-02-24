from pymongo import MongoClient
import uuid
import pprint

import bson # fix uuid.UUID() class issue

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

    """
    import bson
    import pymongo

    mongo_client = pymongo.MongoClient(mongo_uri, document_class=dict)
    db = mongo_client.get_database(                              
        "my_db_name",                                                          
        bson.codec_options.CodecOptions(uuid_representation=bson.binary.UUID_SUBTYPE),
    ) 

    """
    
    print("[Jason]:  Please input Mongo Client Address:")
    print("Example:  mongodb://localhost:27017/")
    mongo_addr = input()

    client = MongoClient(mongo_addr,document_class=dict)
    

    print("[Jason]: Please select db_name")
    print("Example: user_db")
    db_name = input()
    #db      = getattr(client,db_name)
    db = client.get_database(db_name, bson.codec_options.CodecOptions(
        uuid_representation=bson.binary.UUID_SUBTYPE),)
    

    print("[Jason]:  Please input the collection name")
    print("Example:  user_collection")
    print("-----------------------------------")
    print(db.collection_names())
    print("---------------------------------------")
    collection_name = input()
    db_collection = getattr(db,collection_name)


    # Check all keys:
    print("-----------------------------")
    rough_print_all_keys(db_collection)
    print("-----------------------------")


    # Getattr Code Referenced
        # x = getattr(t, 'attr1')
        # setattr(t, 'attr1', 21)
    print("[Jason]:  Please input the uuid you want to query")
    print("Example:  '3442a288-b100-445e-b4dc-ae6b06d3ee28'")
    uuid_str = str(input("input:    "))
    
    data = uuid.UUID(uuid_str)
    print("data type = ",type(data),"value= ",data)
    print("uuid = ",uuid_str)

    db_cur        = db_collection.find({'uuid': uuid.UUID(uuid_str)})
    _tem          = db_cur.next()
    pprint.pprint(_tem)

if __name__ == "__main__":
    query_by_uuid()
