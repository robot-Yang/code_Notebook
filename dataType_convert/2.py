# -*- coding: utf-8 -*-
# @Author: Yang Chen
# @Date:   2020-04-24 18:12:52
# @Last Modified by:   chenyang
# @Last Modified time: 2020-04-24 18:16:13
# \x02 to int
byteslist = [b'\x00',
b'\x01',
b'\x02',
b'\x03',
b'\x04',
b'\x05',
b'\x06',
b'\x07']

for x in byteslist:
    new = int.from_bytes(x,byteorder='big')
    print (new)