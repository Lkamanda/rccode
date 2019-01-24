from pymongo import MongoClient
class MongoAPI(object):
    def __init__(self, db_ip, db_port, db_name, table_name):
        self.db_ip = db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        # 链接创建
        self.conn = MongoClient(host=self.db_ip, port=self.db_port)
        # 数据
        self.db = self.conn[self.db_name]
        # 集合名
        self.table = self.db[self.table_name]

    # 获取一条数据
    def get_one(self, query):
        return self.table.find_one(query, property={"_id": False})

    # 获取多条数据
    def get_many(self, query):
        return self.table.find(query)

    # 添加数据
    def add(self, kv_dict):
        return self.table.insert(kv_dict)

    # 删除数据
    def delete(self, query):
        return self.table.delete_many(query)

    # 查看集合中是否包含符合查询条件的数据
    def check(self, query):
        ret = self.table.find_one(query)
        return ret is not None

    # 更新一条数据
    def update(self, query, kv_dict):
        self.table.update(query, {'$set': kv_dict}, upsert=True)

