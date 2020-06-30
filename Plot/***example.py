# -*- coding: utf-8 -*-
# @Author: Yang Chen
# @Date:   2020-06-10 03:31:21
# @Last Modified by:   chenyang
# @Last Modified time: 2020-06-10 03:32:10

#  tutorial to understand *variable and **variable
def functionA(*a, **kw):
   print(a)
   print(kw)
functionA(1, 2, 3, 4, 5, 6, a=2, b=3, c=5)

lis=[1, 2, 3, 4]
dic={'a': 10, 'b':20}
functionA(*lis, **dic)
