#!/usr/bin/python
#coding=utf-8
def _input(str):
    return str[::-1]

def _output(str):
    if str == _input(str):
        print('the string reverse')
    else:
        print('the string is not reverse')


#使用input 在默认的编辑器下会报错
# str = input('please inter a char')
# print(str)
#_output(str)




