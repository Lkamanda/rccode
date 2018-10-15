import json

# 此时student 是一个dict 格式内容,不是json
student = {
    "name":"luidana",
    "age":18,
    "mobile":"123"
}

print(type(student))
# 把py转成json
stu_json = json.dumps(student)
print(type(stu_json))
print("JSON对象:{0}".format(stu_json))
# 把json格式转成py
stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)