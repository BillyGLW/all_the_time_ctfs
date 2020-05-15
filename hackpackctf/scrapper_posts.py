import re


with open('Posts.xml', 'r', encoding='utf-8') as f:
	x = f.read()

pattern = r'^([a-zA-Z0-9@*#]{4,15})$'
x = x.splitlines()

foo = []
for item in x:
	em = re.findall(pattern,item)
	if em != []:
		foo.append(em)
		print(em)
# print(re.findall(x, pattern))