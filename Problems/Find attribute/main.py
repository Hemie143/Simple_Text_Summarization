from lxml import etree

xml_string = input()
xml_attr = input()
root = etree.fromstring(xml_string)
print(root.get(xml_attr))