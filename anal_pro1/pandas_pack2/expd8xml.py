# XML 자료 읽기
import xml.etree.ElementTree as etree

xml_f = open('my.xml', 'r', encoding='utf8').read() # 'r'은 읽기
print(xml_f, type(xml_f)) # <class 'str'>
root = etree.fromstring(xml_f)
print(root, type(root)) # <class 'xml.etree.ElementTree.Element'>
print(len(root))

print("----------")
# ElementTree로 file_open
xmlfile = etree.parse('my.xml')
print(xmlfile, type(xmlfile))
root = xmlfile.getroot()
print(root.tag) # items태그
print(root[0].tag) # item 0번째 요소명(node name) 읽기
print(root[0][0].tag) # name
print(root[0][1].tag) # tel
print(root[0][0].attrib) # key, value
print(root[0][2].attrib)
print(root[0][2].attrib.keys())
print(root[0][2].attrib.values())
print()
myname = root.find('item').find("name").text # root안에서 item태그를 찾고, 그안의 name의 문구
mytel = root.find('item').find("tel").text
print(myname + ' ' + mytel)

print()
for child in root:
    print(child.tag)
    for child2 in child:
        print(child2.tag, ' ', child2.attrib)
    print()

print()
for e in root.iter('exam'):
    print(e.attrib)

print()
#children = root.findall('item')
children = root.findall('.//item')
print(len(children))

for aa in children:
    re_id = aa.find('name').get('id') # attrib처럼 해당 요소의 속성값 얻어냄
    re_name = aa.find('name').text
    re_tel = aa.find('tel').text
    print(re_id, re_name, re_tel)






















