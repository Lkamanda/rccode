import json

data = {"name":"xiaolin", "age":18}
# 写入文件
with open("t.json", "w") as f :
    json.dump(data, f)
# 重新打开吧json转回python
with open("t.json", "r") as f:
    d = json.load(f)
    print(d)
