# Python cookbook学习笔记

# 2.5 字符串搜索和替换

import re

# 对于简单的字面模式，直接使用str.replace()方法即可。
text = 'yeah, but no, but yeah, but no'
print(text.replace('yeah', 'yep'))						# yep, but no, but yep, but no

# 对于复杂的模式，请使用re模块中的sub()、subn()函数。
date = 'Today is 11/27/2018. PyCon starts 3/13/2020'
print(re.sub('(\\d+)/(\\d+)/(\\d+)', '\\3-\\1-\\2', date))	# Today is 2018-11-27. PyCon starts 2020-3-13

newtext, n = re.subn('(\\d+)/(\\d+)/(\\d+)', '\\3-\\1-\\2', date)	# Today is 2018-11-27. PyCon starts 2020-3-13
print(n)			# 2
