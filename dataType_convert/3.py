#  signed bytearray
wheel_L = -5000
a, b = wheel_L >> 8, wheel_L & 0xFF # divide into Decimal high/low, ex: 5000 > 0x13, 0x88 > 19, 136
# b is bigger than 128
a = a.to_bytes( 1 , byteorder='big' , signed=True )
b = b.to_bytes( 1 , byteorder='big' , signed=False )
print(a, b)

c = a+b
print (c)




