def tohex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits))

wheel_L = tohex(5000, 16)
print(wheel_L, type(wheel_L))
hex(-199703103 & (2**32-1))
hex(-199703103 & (2**64-1)) # 64-bit
