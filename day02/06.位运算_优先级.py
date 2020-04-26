# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/7 17:42
@File ：06.位运算_优先级.py
@IDE ：PyCharm
"""
# 位运算符  & | ~ << >>
# & 按位与
var1 = 19
var2 = 15
res = var1 & var2
print(res)
'''
10011
01111

00011
'''
# | 按位或
res = var1 | var2
print(res)
'''
10011
01111
11111
'''
# ^ 按位异或
'''两个值不相同为真，相同为假'''
res = var1 ^ var2
print(res)
'''
10011
01111
11100
'''

#<< 左移
'''左移是乘 5左移2位相当于5 * 2 的2次幂 = 20 '''
res = 5 << 2
print(res)
'''
0000 0101
0001 0100
'''
# >> 右移
"""右移是除  5右移1位相当于 5 // 2的1次幂 = 2"""
res = 5 >> 1
print(res)
'''
0000 0101
0000 0010

'''

#~ 按位非 公式 -（n+1)
res = ~(-18)  #=-(-18+1) =17
print(res)

'''
总结：所有运算符优先级；
一元运算符：同一时间，操作一个数据(~ -）
二元运算符：同一时间，操作两个数据(+ - * / % ....)

一般情况下，一元运算符优先级大于二元运算符
-3 + 5 = 2

例外
所有运算符优先级最高的 ** 幂运算符 ~2**2
所有运算符优先最低的  = 赋值运算符

同等级运算符优先级
（） > not > and > or
乘除 > 加减
(<< >>) > & > ^ > |

除此之外，大体优先级高低
算术运算符 > 位运算符 > 比较运算符 > 身份运算符 > 成员运算符 >逻辑运算符

赋值运算符 单独列出来 用于把右侧的值算完之后收尾.
'''

res = ~2 **2
print(res) # ~4 => -(4+1) = -5
res = 5+5 << 6//3 is 40 and True
print(res)
'''
res = 10 << 2 is 40 and True
0000 1000=40 
True and True
True
'''
# 加上括号提升优先级 让别人也能看懂
res = (5+5) << (6//3) is 40 and True
print(res)

