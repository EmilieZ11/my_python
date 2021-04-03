import pymongo

myclient = pymongo.MongoClient("mongodb+srv://admin:1234@cluster0.zkshn.mongodb.net/first?retryWrites=true&w=majority")
mydb = myclient["first"]
# dblist = myclient.list_database_names()
# if "second" in dblist: print("The database exists.")
mycol = mydb["gematria"]
# collist = mydb.list_collection_names()
# if "words" in dblist: print("The collection exists.")
mydict = {"word": "Mahdi", "value": 59}
x = mycol.insert_one(mydict)
print(x)

# ServerSelectionTimeoutError timed out; means there's a problem with your IP address.
