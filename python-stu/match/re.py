#!/usr/bin/python
#conding = utf-8
import re

#match是从头开始匹配
m = re.match('foo' , 'foot')
print(m.group(),'\n')

m1 = re.match('foo' , 'startfoot')
if m1 is not None:
    print(m1.group())
else:
    print('not match')


#search

m2 = re.search('foo' , 'startfoot')

if m2 is not None:
    print(m2.group())

#pattern

m3 = re.match('[cr][ab][cd]' , 'cac')

print(m3.group() , '\n')

print(re.match('[cr][ab][cd]' , 'cac').group() , '\n')

m4 = re.match('(all)' , 'alls')
print(m4.groups(0))

#m5 = re.findall()





