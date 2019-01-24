import pymongo

# 默认连接本地

# client = pymongo.MongoClient()

client = pymongo.MongoClient('172.22.106.110', 27017)
# 获取数据库，链接数据库
def client_mongo():
    # 获取数据库，不存在创建
    db = client.shujukuming
    # 获取集合，没有则创建
    my_set = db.jiheming

    # 获取数据
    datas = my_set.find()
    for data in datas:
        print(data['ziduanname'])
        # 获取集合中字段属性
        print(data.keys())

# 插入数据库
def insert_mongo(datas):
    db = client.db_name
    myset = db.set_name
    posts = db.posts
    post_id = posts.insert_one(datas).insert_id

