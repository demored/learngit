#!/usr/bin/python

'''
字符串语法基本操作
'''

#####################使用3引号
name = "zhansan";
str = '''
I am a string
'
I like python
'''

print(str)


######################字符串拼接
str = "hello"
str1 = "python"

print(str+str1)

######################字符串和数值拼接
#print(str+num)  程序报错
num = 20
print(str + repr(num))

######################字符串切片
str3 = "very good!";
print(str3[1])
print(str3[:3])


#######################使用format 来格式化字符串

age = 25
name = 'Swaroop'
print('{0} is {1} years old'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
print('Why is {name} playing {user} with that python?'.format(name="haha",user="hehe"))
