# Python cookbook学习笔记

# 2.4 Matching and Searching for Text Patterns

import re
# 如果你想匹配的是字面字符串，那么你通常只需要调用基本字符串方法就行，比如
# str.find() , str.endswith() , str.startswith() 或者类似的方法：

text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
# print(text == 'yeah')                     # False

# print(text.startswith('yeah'))              # True
# print(text.endswith('yeah'))                # True

# Search for the location of the first occurrence
# text.find('no')                             # 10

text1 = '01/06/2020'
text2 = 'Jan 6th, 2020'

if re.match('\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

# 如果像用同一个正则取匹配多个文本则使用 re.compile()
datepat = re.compile('(\d+)/(\d+)/(\d+)')
get_date = datepat.match(text1)             # <re.Match object; span=(0, 10), match='01/06/2020'>
print(get_date.group(0))                    # 01/06/2020

text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# print(datepat.findall(text3))             # ['11/27/2012', '3/13/2013']
for month, day, year in datepat.findall(text3):
    print('{}-{}-{}'.format(month, day, year))
