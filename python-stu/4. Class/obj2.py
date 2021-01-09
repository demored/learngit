#!/usr/bin/python
#coding=utf-8

'''
1、self的用法详解
2、类的实例方法
3、静态方法和类方法的区别
4、@函数装饰器及用法
5、类的命名空间
6、类变量和实例变量
'''

##########self的使用###########

class A:
    name = "zhangsan"
    def __init__(self):
        print("this is __init__")
    def getName(self):
        print(self.name)

a = A()
a.getName()

##########类调用实例#########

class B:
    name = "zhangsan"
    def getName(self):
        print(self.name)

    def getP():  #警告的红线可以不用管
        print("haha")

##对象调用方法
b = B()
b.getName()
print(b.name)

#类调用
print(B.name)
B.getP()  #不用加参数也可以


##########静态方法和类方法#########

class C:

    @classmethod

    def fly(cls):
        print("I am class method", cls)

    @staticmethod

    def info(p):
        print("静态方法", p)

#使用类去调用
C.fly()
C.info('hello') #必须指定一个参数

c = C()
c.fly()
c.info('demo')

##########函数装饰器#########

def checkAuth(fn):
    print("我是函数装饰者")
    fn()
    def auth(*a):
        print(a)
    return auth

@checkAuth

def login():
    print("我是要被装饰的函数")

login(1,2,3)


##########类变量和实例变量#########

class D:
    name = "lisi"

d = D()
print(d.name) #通过对象访问
print(D.name) #通过类名去访问

d.name = "demored"
print(D.name)
D.name = "summary"
print(d.name)