# Python cookbook学习笔记

# 4.13. Creating data processing pipelines

# 你想以数据管道 (类似 Unix 管道) 的方式迭代处理数据。比如，你有个大量的数据需要处理，但是不能将它们一次性放入内存中。

# 生成器函数是一个实现管道机制的好办法。为了演示，假定你要处理一个非常大的

# 日志文件目录：
"""
foo/
    access-log-012007.gz
    access-log-022007.gz
    access-log-032007.gz
    ···
    access-log-032007.gz
bar/
    access-log-032007.bz2
    ···
    access-log-032007.bz2
"""

# 假设每个包里面都有很多日志文件， 为了处理这些文件，你可以定义一个由多个执行特定任务独立任务的简单生成器
# 函数组成的容器。就像这样：

import os
import fnmatch
import bz2
import gzip
import re


def gen_find(file_pat, top):
    """
    find all filenames in a directory tree that match a shell wildcard pattern
    :param file_pat: 匹配规则
    :param top: 路径
    """
    for dir_path, dir_list, file_list in os.walk(top):
        # dir_path为返回的目录， dir_list为子目录
        for name in fnmatch.filter(file_list, file_pat):
            yield os.path.join(dir_path, name)


def gen_opener(filenames):
    """
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    """
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    """
    Chain a sequence of iterators together into a single sequence.
    """
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """
    Look for a regex pattern in a sequence of lines
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


# 讨论:

# 以管道方式处理数据可以用来解决各类其他问题，包括解析，读取实时数据，定时轮询等。
# 上述代码yield作为生产者，for作为消费者
# gen_concatenate() 函数的作用是为了将输入序列拼接成一个很长的行序列。函数中出现yield from语句。它将yield操作代理
# 到父生成器上去。语句yield from it简单的返回生成器it所产生的所有值。相关资料可以看4.14节

if __name__ == '__main__':
    # log_names = gen_find("access-log*", "C:\\project")
    log_names = gen_find("*txt", "C:\\project")
    files = gen_opener(log_names)
    lines = gen_concatenate(files)
    py_lines = gen_grep('(?i)python', lines)
    for line in py_lines:
        print(line)
