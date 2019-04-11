import pymongo
from random import randint

with pymongo.MongoClient() as conn:
    db = conn.grade
    myset = db.class_
    # # 插入
    # myset.insert([
    #     {'name': 'zhangsan', 'age': 10, 'sex': 'm', 'hobby': ['draw', 'sing', 'dance']},
    #     {'name': 'lisi', 'age': 5, 'sex': 'm', 'hobby': ['draw', 'sing', 'dance', 'computer']},
    #     {'name': 'wangwu', 'age': 15, 'sex': 'm', 'hobby': ['pingpong', 'computer']},
    #     {'name': '阿宝', 'age': 8, 'sex': 'm', 'hobby': ['pingpong', 'computer']},
    #     {'name': '阿蓉', 'age': 14, 'sex': 'w', 'hobby': ['pingpong', 'computer', 'basketball']},
    #     {'name': '阿喆', 'age': 10, 'sex': 'm', 'hobby': ['dance', 'computer', 'basketball', 'football']},
    #     {'name': '百合', 'age': 18, 'sex': 'w', 'hobby': ['dance', 'computer', 'basketball', 'football']}
    # ])

    # 插入score域
    myset.update({},
                {'$set': {'score': {'chinese': 88, 'math': 77, 'english': 78}}},
                multi=True)  # 所有人添加所有相同的score域
    # 修改score, 生成随机的分数
    cursor = myset.find()
    for item in cursor:
        myset.update(
                    {'name': item['name']},
                    {'$set':{'score': {'chinese': randint(60, 100), 'math': randint(60, 100), 'english': randint(60, 100)}}}
        )

    # # 按性别分组统计每组人数
    # cursor = myset.aggregate([{'$group': {'_id': 'sex', 'count': {'$sum': 1}}}])
    # for item in cursor:
    #     print(item)

    # 统计每名男生的语文成绩
    cursor2 = myset.aggregate([{'$match': {'sex': 'm'}},
                              {'$project': {'_id': 0, 'name': 1, 'score.chinese': 1}}
                              ])
    for item in cursor2:
        print(item)

    # 将女生按照英语成绩降序排列
    cursor3 = myset.aggregate([{'$match': {'sex': 'w'}},
                               {'$sort': {'score.english': -1}}
                               ])
    for item in cursor3:
        print(item)

    # # 查询
    # cursor = myset.find({},{'_id': 0})
    # for item in cursor:
    #     print(item)
