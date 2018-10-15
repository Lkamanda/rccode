import xml.dom.minidom
# 在内存中创建空白文档
doc = xml.dom.minidom.Document()
# 创建一个根节点

root = doc.createElement("Managers")

# 设置根节点属性

root.setAttribute('company', 'xx科技')
root.setAttribute('address', '北京')
# 将根节点添加到文档对象中

doc.appendChild(root)

managerList = [
    {'name': 'joy', 'age': 27, 'sex': '女'},
    {'name': 'xiaolin', 'age': 22, 'sex': '男'},
    {'name': 'jun', 'age': 27, 'sex': '女'}
]

for i in managerList:
    nodeManager = doc.createElement("Manager")
    nodeName = doc.createElement('name')
    # 给子节点name 设置一个文本节点
    nodeName.appendChild(doc.createTextNode(str(i['name'])))

    nodeAge = doc.createElement('Manger')
    nodeAge.appendChild(doc.createTextnode(str(i['age'])))

    nodeSex = doc.createElement('sex')
    nodeSex.appendChild(doc.createTextNode(str(i["sex"])))

    # 将各子节点添加到付节点Manger中
    # 最后将Manger添加到根节点Mangers中
    nodeManager.appendChild(nodeName)
    nodeManager.appendChild(nodeAge)
    nodeManager.appendChild(nodeSex)

# 开始写文件

fp = open('Manger.xml', 'w')
doc.write(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
