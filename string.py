#!/usr/bin/python

'''
字符串操作
'''

#使用3引号
str = '''
I am a string
I like python
'''

print(str)

'''
字符串操作
'''
#字符串拼接
str = "hello"
str1 = "python"

print(str+str1)
#字符串和数值拼接
#print(str+num)  程序报错
num = 20
print(str + repr(num))

str3 = "very good!";
print(str3[1])
#字符串切片
print(str3[:3])


#使用format 来格式化字符串

age = 25
name = 'Swaroop'
print('{0} is {1} years old'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

#首字母大写

name = "zhansan"
upName = name.title()
print(upName)

#去除字符串首尾空格

str = " hello world "

print(str,str.strip())
#字符串分割
s = 'crazyit.org is a good site'
print(s.split())

num1 = 3
num2 = 2.5
print(num1 % num2)

#三目运算

a = 10
b = 5

max = a if a > b else b
print(max)

a = input("请输入1个东西")

print("a的类型是", type(a))

if a >= 10:
	print("a是大于10的")
elif a > 20:
	print("a是大于20的")
else:
	print("a是小于10的")

print('哈哈哈哈')