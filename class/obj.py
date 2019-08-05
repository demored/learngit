#!/usr/bin/python
#coding=utf-8

class Pobj:

    __pri = 'hello world'
    """
        pobj's Document , test get mysql data
    """
    docName = 'this is main moudle'
    def __init__(self , paramName):
        print(paramName)
        if paramName != '':
            self.docName = paramName
        else:
            pass
    def getSelf(self):
        return self


pobj = Pobj('testname')
print(pobj.__doc__)
print(pobj.docName)
pobj1 = Pobj('')
print(pobj1.docName)
print(pobj._Pobj__pri)
pobj._Pobj__pri = 'welcome '
print(pobj._Pobj__pri)

class A:
    def __init__(self):
        print('I am a')
    def getName(self):
        print('a name')

class C:
    def __init__(self):
        print('I am c');
        
class B(A,C):
    def __init__(self):
        A.__init__(self);
        C.__init__(self);
    def getAge(self):
        print(20)
    
b = B()
b.getAge()
b.getName()

#docstrings
class A:
    '''this is a class docs'''
    def getName(self):
        '''this is a fun docs'''
        print('get name')

print(A.__doc__)
print(A.getName.__doc__)
a = A()
print(a.__doc__)
print(a.getName.__doc__)

class A:
    def __init__(self):
        print('A')
class B:
    def __init__(self):
        print('B')

class C:
    def __init__(self):
        print('C')
        
class D():
    
    @staticmethod
    def getName():
        print('hello world')
    def getAge(self):
        print('I am young')
d = D()
d.getName()
D.getName()

class F:
    getName1 = 'haha'
    
    def getName(self):
        print('hello world1')

f = F()
f.getName()
print(f.getName1,end='\n')
print(f.__dict__)

class A:
    getName = 'hello world'
    def printFunc(self):
        print('this is a fun')
 
print (A.__dict__)


class A:
    __slots__ = ('age' , 'name')

a = A()
a.name = 'name'
a.age = 'age'
#a.score = 11
print(a.age)


