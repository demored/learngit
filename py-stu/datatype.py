#!/usr/bin/python
#coding=utf-8

list1 = [1,2,3,4,5]
print(list1)
print(help(list1))
print(len(list1))

#字典
dict1 = {'name':'helloword' , 'format_data': 'mysqldata'}

for key,val in dict1.items():
    print(key)
    print(val)
else:
    print('have gone')

# setparam  = set([1,2,3])
# help(setparam)
# print_r(setparam)
dist1 = {'name':'world' , 'backupdata':'mysql'}
list1 = [1,2,3,4]
def check_status(lists):
    for item in lists:
        print(item)

check_status(list1)

format_data = {'check_data' : 'orcale' , 'formart-php' : 'D://www/'}
print(format_data)
print(format_data.items())
data1 = set([1,2,2,3])
print(help(data1))

for key1,val1 in data1:
    print(key1)
    print(val1)

for key1,value1 in format_data.items():
    print(value1)
    print('format')















