#/usr/bin/python
#coding=utf-8

#
f = open('testfile.txt')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    else:
        print(line,end='\n')

f.close()




