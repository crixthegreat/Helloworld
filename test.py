#python code env
#-*-coding:utf-8-*-
#


with open("String.txt") as fobj:
    s = fobj.read()

res = ""

for char in s:
    if char.isdigit():
        res += char

print (res)
print ("done")

