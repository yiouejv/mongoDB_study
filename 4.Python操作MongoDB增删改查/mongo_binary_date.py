import pymongo
import bson

# 小文件存储方案
# 直接转换为二进制插入到数据库
with pymongo.MongoClient() as conn:
    db = conn.db_small_file
    myset = db.file
    with open('gg.jpg', 'rb') as rf:
        data = rf.read()
    # 将bytes格式子串转换为mongodb的二进制存储格式
    content = bson.binary.Binary(data)

    ## 插入到数据库
    # myset.insert({'filename': 'gg.jpg', 'filedata': content})

    # 查找
    cursor = myset.find()

    # 从数据库中读出
    for item in cursor:
        if item['filename'] == 'gg.jpg':
            with open('狗狗.jpg', 'wb') as wf:
                wf.write(item['filedata'])
        print(item)

print('ok')
