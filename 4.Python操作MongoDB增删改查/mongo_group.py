import pymongo


with pymongo.MongoClient() as conn:
    db = conn.stu
    myset = db.ccc

    p = [
        {'$group': {'_id': 'name', 'count': {'$sum': 1}}},
        {'$match': {'count': {'$gt': 1}}}
    ]
    cursor = myset.aggregate(p)
    for item in cursor:
        print(item)
