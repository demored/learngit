#!/usr/bin/python
#coding=utf-8


'''
可变参数
'''
def check_array(name, *user):
    '''
        函数的说明
        __doc__
    '''


    print(name)
    print(user) #是一个tuple

    #打印这个元组
    for i in user:
        print(i)


check_array("zhangsan",'play', 'buffer')


##传入元组

def input(name , *tuple1):
    print(name)
    print(tuple1)


input("zhangsan", *(1,2,3))

##普通变量传参

def swap_commmon(a, b):
    a,b = b,a
    print("函数里的a和b的值是",a, b)

a,b= 4,3
print("交换前的a和b的值是",a,b)

swap_commmon(a,b)
print("交换后的a和b的值是",a,b)

print("==================================")


## 字典的传参


def swap_dict(dict1):
    dict1["a"],dict1["b"] = dict1["b"], dict1["a"]
    print("函数里的a和b的值是",  dict1["a"],  dict1["b"])


dict1 = {"a":1, "b": 2}

print("交换前的a和b的值是",dict1["a"],dict1["b"])
swap_dict(dict1)
print("交换后的a和b的值是",dict1["a"],dict1["b"])
