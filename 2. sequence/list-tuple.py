#!/usr/bin/python
#coding=utf-8

'''
创建列表
'''

list1 = [1,2,3,4]
print(list1)
print(type(list1))

'''
创建元组
'''

tuple1 = (1,2,3)
print(tuple1)
print(type(tuple1))
#创建单个元素的元组
tuple2 = (1,)
print(tuple2)


'''
元组或列表的切片
'''

list4 = [1,2,3,4,5,6]
print(list4[1:3]) #从下标开始

'''
list()和tuple函数用法
'''
print(help(list)) #查看list的函数

##使用list()将元组转成list
a_test=(1,2,3)
print(a_test, type(a_test))

b_test=list(a_test)
print(b_test,type(b_test))

##使用tuple()将list转成元组
aa_test = [1,2,3]
print(aa_test,type(aa_test))
bb_test = tuple(aa_test)
print(bb_test, type(bb_test))

##测试range函数

cc_range = range(1,10)
print(cc_range, type(cc_range))

##给列表增加元素

list3 = [1,2,3,4,5]
list3.append((1,2))
print(list3)





