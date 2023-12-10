import re
p = re.compile("[a-e]")
#using find all
x = p.findall("Aye, said Mr. State.")
print(x)
