from collections import Iterable,Iterator
import time


class MylistIter(object):
    def __init__(self, data):
        # 保存 可迭代对象中的数据的引用
        self.data = data
        # 保存用户访问的下一个元素的下标
        self.index = 0

    def __next__(self):
        """next(迭代器对象) =====> 迭代器对象.__next__()"""
        # print("当前的下标是%d" % self.index)
        if self.index < len(self.data):
            data = self.data[self.index]
            self.index += 1
            return data
        else:
            # 抛出一个StopIteration异常
            raise StopIteration

    # python规定 迭代器也是可迭代对象
    def __iter__(self):
        return self

class Mylist(object):
    def __init__(self):
        self.data = [1,2,3,4,5]

    # iter(可迭代对象) === > 可迭代对象.__iter__()
    def __iter__(self):
        # 返回一个迭代器对象
        mliter = MylistIter(self.data)
        return mliter

ml = Mylist()
# 判断ml对象是否可迭代
print(isinstance(ml, Iterable))

# 判断对象是否是迭代器类型
print(isinstance(ml, Iterator))
mliter = iter(ml)
print(isinstance(mliter, Iterable))
print(isinstance(mliter, Iterator))

for i in ml:
    print(i)

