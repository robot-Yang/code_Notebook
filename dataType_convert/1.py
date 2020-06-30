# -*- coding: utf-8 -*-
# @Author: Yang Chen
# @Date:   2020-04-24 17:22:24
# @Last Modified by:   chenyang
# @Last Modified time: 2020-04-25 16:27:59
# Python code to demonstrate Type conversion 
# using int(), float() 
  
# s = '10010'

# # printing string converting to int base 2 
# c = int(s,2) 
# print ("After converting to integer base 2 : ", end="") 
# print (c) 

############################
# printing string converting to int base 2 
# initializing string 
s = '\x02'
print (s, type(s)) 

s = u'\x02'
print (s, type(s))

s = u'\x02' 
s = s.encode('ascii')
print (s, type(s)) 

s = '\x32'
print (s, type(s)) 
s = int(s,16) 
print (s, type(s)) 

# for python3
s = '\x02'
s = s.encode('ascii')
s = int.from_bytes(s,byteorder='big')
print(s, type(s))

# for python3
s = b'\x03'
print(s, type(s))

# # for python2
# s = '\x02'
# # s = s.encode('ascii')
# s = int(s.encode('hex'), 16)
# print(s, type(s))

s = b"\x00\x01"
s = list(s)
print(s, type(s))

s = '\x02'
s = s.encode('ascii')
s = list(s)
print(s, type(s))
