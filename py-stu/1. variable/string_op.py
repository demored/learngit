#--coding=utf-8--
'''
字符串函数的操作
'''

#首字母大写

name = "zhan san"
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




