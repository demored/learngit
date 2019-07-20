#!/usr/bin/python
'''
列表和元组
'''
#声明一个元组
list = 1,2,3,4
#或者
list1 = (1,2,3)
#申明一个元素的元组
list2 = (1,)
print(list)
print(list1)
print(list2)

#声明一个列表

m1 = [1,2,3,4]
print(m1)

#循环列表
for a in m1:
	print(a)
#循环元组

for b in list1:
	print(b)

a= range(22,27)
print(type(a))

del list1
# print(list1)

#测试列表的赋值
list1 = [1,2,3,4]
list2 = list1
list1[0] = 99
print(list2) #[99, 2, 3, 4]
del list1
print(list2) #[99, 2, 3, 4]
list3 = list2
print(list3) #[99, 2, 3, 4]
list2.clear()
print(list3) #[]


#测试字典

dict1 = {"hello":'张三', "world":"李四"}
print(dict1) #{'hello': '张三', 'world': '李四'}
dict2 = dict1
del dict1
print(dict2)