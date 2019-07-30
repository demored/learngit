#!/usr/bin/python
#coding=utf-8
#异常处理

#Print('hello world')         抛出异常错误 NameError

try :
      input('enter a num -->')
      Print('Hello world')
     
except NameError:
      print('this is NameError')
else:
      print('no error')
finally:
      print('不管怎么样都走了这一步')
