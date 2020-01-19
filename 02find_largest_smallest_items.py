# Python cookbook学习笔记

# 1.4 Finding the Largest or Smallest N Items
# you want to make a list of the largest or smallest N items in a collection

import heapq

nums = [1, 8, 20, 10, 5, 6, 9, -1, -10, 100]

print(heapq.nlargest(3, nums))          # [100, 20, 10]
print(heapq.nsmallest(3, nums))         # [-10, -1, 1]


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPl', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHoo', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# 也可接受一个key为匿名函数
cheap = heapq.nsmallest(2, portfolio, key=lambda x:x['price'])
largest = heapq.nlargest(2, portfolio, key=lambda x:x['price'])

print('cheap:', cheap)
# cheap: [{'name': 'YHoo', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}]
print('largest:', largest)
# largest: [{'name': 'AAPl', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]


# 这里是拷贝nums，heapq[0]永远都是最小的
heap = list(nums)
heapq.heapify(heap)

heapq.heappop(heap)     # -10
heapq.heappop(heap)     # -1
heapq.heappop(heap)     # -6
print(heap)


# 总结：
# nlargest()和nsmallest()方法更常用，如果你只想找出最大或者最小值，使用这两个方法要比min()和max()要快。
# 如果你想找的item个数是列表的大小的话，比起使用sort()的方法排序也要快

# 参考：
# The nlargest() and nsmallest() functions are most appropriate if you are trying to
# find a relatively small number of items. If you are simply trying to find the single smallest
# or largest item (N=1), it is faster to use min() and max(). Similarly, if N is about the
# same size as the collection itself, it is usually faster to sort it first and take a slice (i.e.,
# use sorted(items)[:N] or sorted(items)[-N:])
