from pymongo import MongoClient
import uuid



#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient('mongodb://localhost:27017/')
db = client.user_db


# Referenced code:
    # fivestar = db.reviews.find_one({'rating': 5})
    # result = db.user_collection.find_one({user_id: 1})


print(db.collection_names())
result_cursor = db.user_collection.find()

print(list(result_cursor))    #Changed to list and display all, not for production
#print(result_cursor.next())  # Comment list(result_cursor),  use next()  , next() to get each row by row


# { "_id" : ObjectId("5e510707c1fbe04fa9d5959d"), 
# "uuid" : UUID("da00fcb1-2869-4f47-b7ed-956b9afdf7f1"), 
# "first_name" : "johnny", 
# "family_name" : "hung", 
# "email" : "wolfmib@gmail.com", 
# "password" : "1234abcd", 
# "user_id" : 1, 
# "email_is_valid" : false 



# Check the max_user_id
    # Referenced code: measurement = mongo.db.measurements.find_one().sort([("timestamp", -1)])
    # cursor = mongo.db.measurements.find().sort([('timestamp', -1)]).limit(1)

# Sort user_id by decending '-1'
    # commme ca
        #   user_id = 2
        #   user_id = 1
check_cur   = db.user_collection.find().sort([('user_id',-1)]).limit(1)

# Obtenir 1st one,
_tem_data   = check_cur.next()

# Show user_id via dict format
max_user_id = _tem_data['user_id']
print("Current max_user_id = %d"%max_user_id)




#Step 2: Create sample data
tem_row = {
    "uuid"           : uuid.uuid1(),
    "first_names"    : 'others',
    "family_name"    : 'jfowjfo',
    "email"          : "what_ever",
    "password"       : "hello",
    "user_id"        : int((max_user_id + 1)),
    "email_is_valid" : False
}


# Step 3: Insert
result = db.user_collection.insert_one(tem_row)
print(result)

# Obtenir result
check_all     = db.user_collection.find()
_tem_row_data = check_all.next()
my_uuid = _tem_row_data['uuid']
print("type of uuid is  ", type(my_uuid)) #  #output : type of uuid is   <class 'uuid.UUID'>

while _tem_row_data:
    print(_tem_row_data)
   
    try:
        _tem_row_data = check_all.next()
    except:
        _tem_row_data = []
    

