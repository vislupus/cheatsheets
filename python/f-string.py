number = -7

print(f"{number = }")
# number = 123
# number = 1
# number = -7

print(f"{number = !s}")
# number = 123 
# number = 1
# number = -7

print(f"{number = :.2f}")
# number = 123.00
# number = 1.00
# number = -7.00

print(f"{number:02d}")
# 123
# 01
# -7

print(f"{number:#2d}")
# 123
#  1
# -7

print(f"{number:2d}")
# 123
#  1
# -7

print(f"{number:.2f}")
# 123.00
# 1.00
# -7.00

print(f"{number:08.2f}")
# 00123.00  
# 00001.00
# -0007.00
     
print(f"{number:,.2f}")
# 123.00
# 1.00
# -7.00

print(f"{number:.0%}")
# 12300%
# 100%
# -700%

print(f"{number:,}")
# 123
# 1
# -7

print(f"{number:_}")
# 123
# 1
# -7

print(f"{number:.1e}")
# 1.2e+02
# 1.0e+00
# -7.0e+00

print(f"{number:#.1g}")
# 1.e+02
# 1.
# -7.

print(f"{number:+}")
# +123
# +1
# -7

print(f"{number:-}")
# 123
# 1
# -7

print(f"{number:?<+11,}")  # fill (?), align (<), sign (+), width (11), sep (,)
# +123???????
# +1?????????
# -7?????????

print(f"{number:b}")  # binary
# 1111011
# 1
# -111

print(f"{number:x}")  # hexadecimal
# 7b
# 1
# -7

print(f"{number:#x}")
# 0x7b
# 0x1
# -0x7

print(f"{number} {number:>25} {number}")
# 123                       123 123       
# 1                         1 1
# -7                        -7 -7

print(f"{number} {number:.>25} {number}")
# 123 ......................123 123       
# 1 ........................1 1
# -7 .......................-7 -7

print(f"{number} {number:<25} {number}")
# 123 123                       123       
# 1 1                         1
# -7 -7                        -7

print(f"{number} {number:.<25} {number}")
# 123 123...................... 123       
# 1 1........................ 1
# -7 -7....................... -7

print(f"{number} {number:^25} {number}")
# 123            123            123 
# 1             1             1
# -7            -7             -7