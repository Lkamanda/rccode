import requests
from interface.pn1.utils.excal_data import *
from interface.pn1.utils.operationExcal import *
from interface.pn1.utils.operationJson import *


class Method:
    def __init__(self):
        self.operationExcal = OperationExcal()
        self.operationJson = OperationJson()

    def post(self, row):
        try:
            print(self.operationExcal.get_url(row=row))
            r = requests.post(
                url=self.operationExcal.get_url(row=row),
                data=self.operationJson.getRequstData(row=row),
                headers=getHeaderValue(),
                timeout=6)

            return r
        except Exception as e:
            print(e)
            raise RuntimeError('接口请求发生未知错误')


class IsAssert:
    def __init__(self):
        self.excal = OperationExcal()
        # 因网站接口该改变这里str2理应从页面获取,但实际自定义
        self.str2 = 'abcdedf'

    def isContent(self, row):
        # print(self.excal.get_except(row=row))
        if self.excal.get_except(row=row) in self.str2:
            flag = True
        else:
            flag = False
        return flag


if __name__ == '__main__':
    #method = Method()
    #method.post(1)
    isansert = IsAssert()
    print(isansert.isContent(row=1))





