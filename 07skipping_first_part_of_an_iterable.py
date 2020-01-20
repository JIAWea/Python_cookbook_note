# Python cookbook学习笔记

# 4.8. Skipping the First Part of an Iterable
# You want to iterate over items in an iterable, but the first few items aren’t of interest and
# you just want to discard them.

# 假如你在读取一个开始部分是几行注释的源文件。所有你想直接跳过前几行的注释

from itertools import dropwhile

with open('/etc/passwd') as f:
	for line in dropwhile(lambda line: line.startswith('#'), f):
		print(line, end='')

# 迭代器和生成器是不能使用标准的切片操作的，因为它们的长度事先我们并不知道 (并且也没有实现索引)。
# 函数 islice() 返回一个可以生成指定元素的迭代器，它通过遍历并丢弃直到切片开始索引位置的所有元素。
# 然后才开始一个个的返回元素，并直到切片结束索引位置。

from itertools import islice

items = ['a', 'b', 'c', 1, 6, 8, 10]


for x in islice(items, 3, None)
	print(x)

# 1
# 6
# 8
# 10


# 4.12 不同集合上元素的迭代

# itertools.chain() 方法可以用来简化这个任务。它接受一个可迭代对象列表作为输入，并返回一个迭代器

from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
	print(x)

# 1
# 2
# 3
# 4
# x
# y
# z
