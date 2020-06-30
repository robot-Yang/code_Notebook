wheel_L = 5000

print (bin(wheel_L))

high_L = wheel_L >> 8
print (high_L, bin(high_L))

low_L = wheel_L & 0xFF
print (low_L, bin(low_L))

high_L, low_L = wheel_L >> 8, wheel_L & 0xFF # 拆分成十进制高位/低位, ex: 5000 > 0x13, 0x88 > 19, 136
print(high_L, low_L)