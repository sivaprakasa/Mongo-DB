import pymongo   #import the pymongo package

mongocon = pymongo.MongoClient("mongodb://localhost:27017") #connect mongodb server

mydatabase = mongocon["Library"]    #create database

mycollection = mydatabase["books"]  #create collection

mydoc = [
    {
        "book":"C",                 #collection of record
        "author":"kumar"
    },
    {
        "book":"C++",
        "author":"vetri"
    },
    {
        "book":"java",
        "author":"kabir"
    },
    {
        "book":"php",
        "author":"vel"
    },
    {
        "book":"python",
        "author":"venket"
    }
    ]
# create insert method
insertmy = mycollection.insert_many(mydoc)
print(f"Insertd Document Id:{insertmy.inserted_ids}")

# Display the all record methods
documents = mycollection.find()
for document in documents:
    print(document)

#update method
query = {"book":"python"}
new_value = {"$set":{"author":"ganesh"}}
mycollection.update_one(query,new_value)
up_doc = mycollection.find_one(query)
print(f"Updated document: {up_doc}")

#delete method
query = {"book":"php"}
mycollection.delete_one(query)
de_doc = mycollection.find_one(query)
print(f"Delete document:{de_doc}")

