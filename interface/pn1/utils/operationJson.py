from interface.pn1.utils.public import *
import json
from interface.pn1.utils.operationExcal import *


class OperationJson:
    # 如果要使用其他模块的类,没必要继承该类,直接在构造函数中实例化该类
    def __init__(self):
        self.excal = OperationExcal()

    def getReadJson(self):
        """读取json文件"""

        # json.dump(open(data_dir(fileName='requestData.json')))

        with open(data_dir(fileName='requestData.json'), encoding='utf-8') as f:
            # load将str转为dict
            data = json.load(f)
            return data

    def getRequstData(self, row):
        """获取请求参数"""
        # json返回的是字典,通过k=login001的到对应的值v
        # return self.getReadJson()[self.excal.get_request_data(row=row)]
        # dumps 将dict转成str
        return json.dumps(self.getReadJson()[self.excal.get_request_data(row=row)])
        # ensure_ascii 忽略asc码


if __name__ == '__main__':
    OperationJson = OperationJson()
    print(OperationJson.getRequstData(1))
