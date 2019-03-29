import os

def data_dir(data='data', fileName=None):
    # os.path.dirname(__file__) 获取当前目录下父类路径
    """
    对文件路径的查找
    :param data: 目录名
    :param fileName:文件名
    :return:路径
    """
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), data, fileName)


