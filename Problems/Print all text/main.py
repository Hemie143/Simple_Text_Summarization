from lxml import etree

xml_string = input()
root = etree.fromstring(xml_string)
for e in root:
    print(e.text)
