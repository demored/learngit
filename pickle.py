#!/usr/bin.pyhton
#coding=utf-8

import pickle
file = open('./pick.txt' , 'wb')
listdata = {'username':'mysql' , 'lang':'english'}
print(listdata)
pickle.dump(listdata,file)
file.close()


f = open('./pick.txt' , 'rb')

data = pickle.load(f)
print(data)





