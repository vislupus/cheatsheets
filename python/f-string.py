number = 123

print(f"{number = }")
# number = 123

print(f"{number = !s}")
# number = 123 
#   
print(f"{number = :.2f}")
# number = 123.00

print(f"{number:02d}")
# 123

print(f"{number:#2d}")
# 123

print(f"{number:2d}")
# 123

print(f"{number:.2f}")
# 123.00

print(f"{number:08.2f}")
# 00123.00  
     
print(f"{number:,.2f}")
# 123.00

print(f"{number:.0%}")
# 12300%

print(f"{number:,}")
# 123

print(f"{number:_}")
# 123

print(f"{number:.1e}")
# 1.2e+02

print(f"{number:#.1g}")
# 1.e+02

print(f"{number:+}")
# +123

print(f"{number:-}")
# 123

print(f"{number:?<+11,}")  # fill (?), align (<), sign (+), width (11), sep (,)
# +123???????

print(f"{number:b}")  # binary
# 1111011

print(f"{number:x}")  # hexadecimal
# 7b

print(f"{number:#x}")
# 0x7b

print(f"{number} {number:>25} {number}")
# 123                       123 123       

print(f"{number} {number:.>25} {number}")
# 123 ......................123 123       

print(f"{number} {number:<25} {number}")
# 123 123                       123       

print(f"{number} {number:.<25} {number}")
# 123 123...................... 123       

print(f"{number} {number:^25} {number}")
# 123            123            123 