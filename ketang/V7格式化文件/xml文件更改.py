import xml.etree.ElementTree as et
tree = et.parse(r'to_edit.xml')
root = tree.getroot()
for e in root.iter('name'):
    print(e.text)
for stu in root.iter('student'):
    name = stu.find('Name')

    if name != None:
        name.set('test', name.text*2)

stu = root.find('student')

e = et.Element('ADDer')
e.attrib ={'a':'b'}
e.text = '我加的'
stu.append(e)

tree.write('to_edit.xml')