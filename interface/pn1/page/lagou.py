from interface.pn1.utils.operationJson import *
from interface.pn1.utils.operationExcal import *

operationJson = OperationJson()
operationExcal = OperationExcal()


def setSo(kd=None):
    """对搜索的数据重新赋值"""
    print(kd)
    # operationJson.getRequstData(1) 得到的dict1为str ,需要反序列化
    dict1 = json.loads(operationJson.getRequstData(1))
    dict1['kd'] = kd
    return dict1


def write_PositionId(content):
    """ 把获取的参数写入文件中"""
    with open(data_dir(fileName='positionID'), 'W') as f:
        f.write(content)


def getPositionID():
    """获取参数"""
    with open(data_dir(fileName='positionID'), 'r') as f:
        # type(json.loads(f.read(content))) list
        return json.loads(f.read())


def getUrl():
    # urlInfo = operationExcal.get_url(2)
    url_list = []
    for item in getPositionID():
        url = '/{0},html'.format(item)
        list.append(url_list)
    return url_list




if __name__ == '__main__':
    print(setSo())