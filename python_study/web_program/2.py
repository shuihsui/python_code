#!/usr/bin/env python
# -*- coding:utf-8

#这里是进行不可变列表元组函数的学习

str1 = 'shuihsui'
word = 'hu'

ls1 = [str1,word]
ls2 = [22,]

print str1.__add__(word)

print ls1.__iadd__(ls2)
ls1.append(ls2)
print ls1
