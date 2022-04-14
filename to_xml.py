from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

categories_dict = {"Animals": ["dog", "cat", "chicken"], "furniture": ["closet", "chair", "table"], "food": ["pizza", "falafel", "chocolate"]}

categories_xml = dicttoxml(categories_dict, attr_type = False)
categories_dom = parseString(categories_xml)

print(categories_xml)
print()
print(categories_dom.toprettyxml())

xmlfile = open("categories_dict.xml", "w")
xmlfile.write(categories_dom.toprettyxml(indent = ' ' * 4))
xmlfile.close()