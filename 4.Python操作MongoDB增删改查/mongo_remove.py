import pymongo


with pymongo.MongoClient() as conn:
    # 选择数据库
    db = conn.stu

    # 选择操作的集合
    myset = db.ccc

    # # 删除操作
    # query = {'name': '小王'}
    # multi = True  # Ture删除所有查询到的结果
    # myset.remove(query, multi)

    # #　删除所有爱好只有一个的
    # query = {'hobby': {'$size':1}}
    # multi = True
    # myset.remove(query, multi)

    # 查找名字等于小明并删除
    query = {'name': '小明'}
    print(myset.find_one_and_delete(query))

    print('================')
    # 查询
    cursor = myset.find()

    for item in cursor:
        print(item)

