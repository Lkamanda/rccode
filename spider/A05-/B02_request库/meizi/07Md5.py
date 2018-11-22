import hashlib
def getMd5(value):
    # 构建md5对象
    md5 = hashlib.md5()
    md5.update(bytes(value, encoding="utf-8"))
    sign = md5.hexdigest()
    print(sign)
if __name__ == '__main__':
    a = '123456'
    getMd5(a)