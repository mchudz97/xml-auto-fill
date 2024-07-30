import sys
import os
import copy
import xml.etree.ElementTree as et
print(sys.argv[1])
tree = et.parse(sys.argv[2])
root = tree.getroot()
first_child = list(root).pop()
for child in root.findall("*"):
    root.remove(child)
print(len(list(root)))
values_list = []
with open(sys.argv[3], 'r') as file:
    for line in file:
        values_list.append(line.replace("\n", ""))
for i in range(len(values_list)):
    cloned_child = copy.deepcopy(first_child)
    to_find = ".//" + sys.argv[1]
    value_to_change = cloned_child.findall(to_find)[0]
    value_to_change.text = values_list[i]
    print(len(list(root)))
    root.append(cloned_child)
print(len(list(root)))
if os.path.exists("new.xml"):
    os.remove("new.xml")
tree.write("new.xml", encoding="utf-8")

