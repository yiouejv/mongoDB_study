import pymongo
import gridfs

# # 将文件以grid方案存放到数据库
# with pymongo.MongoClient() as conn:
#     db = conn.db_grid
#     # 获取gridfs对象
#     fs = gridfs.GridFS(db)
#
#     with open('mongo.py', 'rb') as rf:
#         # 将文件写入到数据库
#         fs.put(rf.read(), filename='mongo.py')
#
# print('ok')


# 获取grid方案存放到数据库中的文件
    # 获取grids对象
with pymongo.MongoClient() as conn:
    db = conn.db_grid
    fs = gridfs.GridFS(db)
    # 得到文件集合对象
    files = fs.find()
    # 分别取每一个文件
    for file in files:
        # 打印文件名称
        print(file.filename)
        if file.filename == 'mongo.py':
            # 从数据库中读取
            data = file.read()
            with open('outer.py', 'wb') as wf:
                wf.write(data)

print('ok')

