#!/usr/bin/python
#coding=utf-8

'''
    列表表达式
'''
num = [(x,y) for x in range(5) for y in range(5)]
print(num)

## for的用法

for x in range(10):
    print(x)
else:
    print("for 循环已经结束")
