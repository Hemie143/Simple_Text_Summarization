from lxml import etree

def find_password(xml_string):

    def parse_element(el):
        pwd = el.get('password')
        if pwd:
            return pwd
        else:
            for e in el:
                parse_element(e)

    root = etree.fromstring(xml_string)
    pwd = parse_element(root)
    return pwd



'''    
Test 1
<profile><account login="login" password="secret"/></profile>
'''

