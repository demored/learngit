#!/usr/bin/python
#coding=utf-8

#
'''
lambda表达式的使用
'''

##简单的lambda表达式
a = lambda x,y: x*y

print(a(2,4))

## 复杂的lambda表达式
a,b= 100,200
user = lambda x,y:x+y if a > b else print("a > b")

print(user) #打印出来是lambda表达式的函数地址


