from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

categories = {"Alphabetic": ["abcba", "defgddy", "hijkl"], "Numeric": ["11223", "24124", "76809"], "Alphanumeric": ["121ab1", "556cd6", "09aa05bb"]}

categories_xml = dicttoxml(categories, attr_type = False)
categories_dom = parseString(categories_xml)

print(categories_xml)
print()
print(categories_dom.toprettyxml())

xmlfile = open("categories_dict.xml", "w")
xmlfile.write(categories_dom.toprettyxml(indent = ' ' * 4))
xmlfile.close()