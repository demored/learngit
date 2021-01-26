#!/usr/bin/python
#coding=utf-8

#声明一个字典
dict1 = {}
print(dict1, type(dict1))
dict2 = {"name":"tencent"}
print(dict2, dict2['name'])

##声明一个空字典
dict3 = dict()
print(dict3)

dict4 = [("hello", 2), ("world", 3)]
print(dict4, dict(dict4))

##赋值时，修改list元素对另一个list有没有影响
print("==============")
dict5 = dict2
print(dict5)
dict2.clear()
print(dict5)