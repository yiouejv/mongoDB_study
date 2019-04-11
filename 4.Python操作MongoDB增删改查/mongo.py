import pymongo

# 创建数据库链接
conn = pymongo.MongoClient()

# 创建数据库对象
db = conn.stu

#　创建集合对象
myset = db.log

# print(dir(myset))
# myset.insert([{'name': '张铁林', 'king': '乾隆'},
#              {'name': '张国立', 'king': '康熙'},
#              {'name': '陈道明', 'king': '康熙'},
#              {'name': '唐国强', 'king': '雍正'},
#              {'name': '郑少秋', 'king': '乾隆'},
#              {'name': '陈建斌', 'king': '康熙'}])
# myset.save({'_id': '5ba46b1569d72e1616156f7c', 'name': '陈建斌', 'king': '哈哈爸爸'})

# 查询结果
items = myset.find({'name': '郑少秋'})

# 遍历结果打印
for item in items:
    print(item)

# 关闭链接
conn.close()
