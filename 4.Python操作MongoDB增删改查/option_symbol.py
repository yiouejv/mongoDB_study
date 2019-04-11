import pymongo

with pymongo.MongoClient() as conn:
    db = conn.stu
    myset = db.ccc
    myset.insert({'age':16})
    # cursor = myset.find({'age':{'$gt':18}},{'_id':0})
    cursor = myset.find({'$or':[{'age':{'$lt':19}}, {'sex':'女'}]},{})
    for item in cursor:
        print(item)
    print('ok')



