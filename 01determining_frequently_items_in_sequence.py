# Python cookbook学习笔记

# 1.12 Determining the Most Frequently Occurring Items in a Sequence

# 怎样找出一个序列中出现次数最多的元素呢？

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
# print(word_counts)                  # Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, ...})
top_three = word_counts.most_common(3)
print(top_three)                    # Outputs [('eyes', 8), ('the', 5), ('look', 4)]

# 作为输入，Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象。
# 在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上。比如：
print(word_counts['not'])           # 1
print(word_counts['eyes'])          # 8
