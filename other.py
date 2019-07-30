#/usr/bin/python
#!conding=utf-8


list1 = [1,2,3,4]

list2 = [2*i for i in list1 if i>2]

#列表综合 ,对于之前的列表数据不会改变
print(list2)
print(list1)

#引用 , 对于一个引用的列表，删除主的列表，对于引用的列表的值也会改变
list3 = list1
del list3[0]
print(list3)
print(list1)

#如果不同引用则需要采用切片的形式生成列表

list5 = list2[:]
print(list5)

del list2[0]
print(list2)
print(list5)

#函数中，使用元组和字典传递参数

def a(b , *c , **d):
      print(b)
      print(c)
      print(d['d']['username'])
      
a(1,2,3,4 ,d ={'username':'zs' , 'age':20})


