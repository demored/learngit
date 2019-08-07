#!/usr/bin/python
#coding=utf-8

'''
1、roperty定义属性
2、封装机制及实现方法
3、继承机制及实现方法
4、父类方法重写
5、调用父类的构造方法
'''

###################property()定义属性###################
class A:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getSize(self):
        print("触发了getSize")
        size = self.width,self.height
        return size

    size = property(getSize) #切记有一个返回值


a = A(1,2)

print(a.size)

###################封装机制及实现方法###################

##设置隐藏成员

class B:
    __name = "我是隐藏的name"
    def __get(self):
        print('我是隐藏的get方法')


b = B()
# print(b.__name)  #会报错AttributeError: 'B' object has no attribute '__name'

# b.__get() #也会报错，AttributeError: 'B' object has no attribute '__get'

print(b._B__name) #通过隐蔽的调用也可以获得name


###################继承###################

class C1:

    def info(self):
        print("I am C1.info")

class C2:
    def info(self):
        print("I am C2.info")

class C(C1,C2):
    pass


c = C()
c.info()

###################父类重写###################

class D1:
    def info(self):
        print("我是父类的方法")

class D(D1):
    def info(self):
        print("我是子类的方法")
        D1.info(self) #可以使用父类名来调用父类中同名的方法


d = D()
d.info()


