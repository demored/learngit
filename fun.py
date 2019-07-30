#!/usr/bin/python
#coding=utf-8


def fun():
    print('test pyfun')
fun()

#局部变量
num=1
def localfun():
    num = 10
    print(num)

localfun()
print(num)
#全局变量

def globalFun():
    global num
    num = 2
    print(num)
    print('this is a global function')
globalFun()
print(num)

#默认参数

def defaultFun(a , b = 1):
    print(a)
    print(b)

defaultFun(10)
#关键字参数
def keywordFun(a = 1 , b = 2 , c = 3):
    print(a)
    print(b)
    print(c)
keywordFun(10 , c=500)
#varArgs参数

def varFun(a=1 , *b , **c):
    print(a)
    print(b)
    print(c)

varFun(1,2,3,4,m='hello' , n = 'world')




