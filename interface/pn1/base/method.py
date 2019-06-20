import requests
from interface.pn1.utils.excal_data import *
from interface.pn1.utils.operationExcal import *
from interface.pn1.utils.operationJson import *


operationExcal = OperationExcal()


def checkHeader(row, f1=None, f2=None):
    """检测请求头"""
    # 获取url
    url = operationExcal.get_url(row=row)
    url = url.split('/')
    if url[5] == 'xxxx':
        return f1
    elif url[6] == "xx":
        return f2

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

    def post2(self, row, data):
        try:
            # print(self.operationExcal.get_url(row=row))
            # print(self.operationJson.getRequstData(row=row))
            print(data)
            r = requests.post(
                url=self.operationExcal.get_url(row=row),
                data=data,
                headers=checkHeader(
                    row=row,
                    f1=getHeaderValue(),
                    f2=getHeaderInfo()
                ),
                timeout=6)
            return r
        except Exception as e:
            print(e)
            raise RuntimeError('接口请求发生未知错误')

    def get(self, url, params=None):
        """对get请求进行二次分装"""
        r = requests.get(url=url, params=params, headers=getHeaderValue(), timeout=6)
        return r


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
    method = Method()
    method.post(1)
    # isansert = IsAssert()
    # print(isansert.isContent(row=ce1))





