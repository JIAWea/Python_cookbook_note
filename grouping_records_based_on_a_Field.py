# Python cookbook学习笔记

# 1.15 Grouping Records Together Based on a Field
# You have a sequence of dictionaries or instances and you want to iterate over the data
# in groups based on the value of a particular field, such as date.

# The itertools.groupby() function is particularly useful for grouping data together like this:

from operator import itemgetter
from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/05/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# Now suppose you want to iterate over the data in chunks grouped by date. To do it, first
# sort by the desired field (in this case, date) and then use itertools.groupby():
rows.sort(key=itemgetter('date'))
print(rows)

# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('    ', i)


# 使用defaultdict()可将数据分组:
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
print(rows_by_date)         # defaultdict(<class 'list'>, {'07/01/2012': [{'address': ' ', ...}], ...})
