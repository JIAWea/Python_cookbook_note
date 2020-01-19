# Python cookbook学习笔记

# 3.1. Rounding Numerical Values
# You want to round a floating-point number to a fixed number of decimal places.

print(round(1.23, 1))       # 1.2
print(round(1.27, 1))       # 1.3
print(round(-1.27, 1))      # -1.3
print(round(1.25361, 3))    # 1.254

# 当一个值刚好在两个边界的中间的时候，round 函数返回离它最近的偶数。也就是
# 说，对 1.5 或者 2.5 的舍入运算都会得到 2。
print(round(1.5))           # 2
print(round(2.5))           # 2

# 传给 round() 函数的 ndigits 参数可以是负数，这种情况下，舍入运算会作用在
# 十位、百位、千位等上面。比如：
a = 1627731
print(round(a, -1))         # 1627730
print(round(a, -2))         # 1627700
print(round(a, -3))         # 1628000

# 如果只需要简单的格式化，则不需要用round
print(format(1.234568, '0.2f'))          # 1.23
print(format(1.234568, '0.5f'))          # 1.23457
