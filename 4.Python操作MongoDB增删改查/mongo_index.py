import pymongo
# import traceback


with pymongo.MongoClient() as conn:
    db = conn.stu
    myset = db.ccc

    # 添加索引
    # 默认创建正向索引
    myset.ensure_index('age')

    # 创建反向索引
    name_index = myset.ensure_index([('name', -1)])  # 返回索引的名字

    # 删除单个索引
    try:
        myset.drop_index('name_1')
    except Exception:
        # traceback.print_exc()
        pass

    # 删除所有索引
    myset.drop_indexes()

    # 创建其他索引的类型
    myset.ensure_index([('name', 1), ('age', -1)])

    # 创建唯一索引
    myset.ensure_index('name', name='name_index', unique=True)

    # 稀疏索引
    myset.ensure_index('age', sparse=True)
    
    # 查看索引
    indexes = myset.list_indexes()
    for index in indexes:
        print(index)
