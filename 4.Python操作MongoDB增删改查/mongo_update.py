import pymongo

with pymongo.MongoClient() as conn:
    # 选择数据库
    db = conn.stu

    # 选择操作的集合
    myset = db.ccc

    # 创建游标对象
    # cursor = myset.insert([
    #     {'name': '小红', 'age': 18, 'sex': '女', 'hobby': ['跳舞']},
    #     {'name': '小明', 'age': 17, 'sex': '男', 'hobby': []},
    #     {'name': '小王', 'age': 19, 'sex': '男', 'hobby': []},
    #     {'name': '小李', 'age': 18, 'sex': '男', 'hobby': ['唱歌']},
    #     {'name': '小刘', 'age': 16, 'sex': '男', 'hobby': ['唱歌']}
    # ])

    # 修改
    # query = {'name': 'Jame'}  # {'name': '小红'}
    # update = {'$set':{'age':20, 'sex':'男', 'hobby':['唱歌', '跳舞']}}
    # upsert = True
    # multi = False
    # myset.update(query, update, upsert, multi)

    #　修改多条文档
    myset.update_many(
        {'name': '小明'},
        {'$set':{'hobby':['骑马', '喝酒']}}
    )


    # 查询
    cursor = myset.find()

    for item in cursor:
        print(item)
