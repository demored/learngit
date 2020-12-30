#!/usr/bin/python
# -- coding: utf-8 --

'''
    python异常
'''

def minus():
    print(2/0)

try:
    minus()
except Exception as e:
    print(e)
else:
    print("执行了else")
finally:
    print("执行了finally")
