import xml.etree.ElementTree as et

# 在内存中创建一个空文档

etree = et.ElementTree()
e = et.Element('student')

etree._setroot(e)
e_name = et.SubElement(e, 'Name ')
e_name.text = 'haha'
etree.write('v06.xml')