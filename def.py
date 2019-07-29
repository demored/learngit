#!/usr/bin/python

'''
函数的具体使用

'''

#函数的多个返回值
def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        # 如果元素e是数值
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum / count
my_list = [20, 15, 2.8, 'a', 35, 5.9, -1.8]

# 获取sum_and_avg函数返回的多个值，多个返回值被封装成元组
tp1,tp2= sum_and_avg(my_list)
print(tp1)
print(tp2)

tp= sum_and_avg(my_list)
print(tp)