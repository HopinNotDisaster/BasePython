# iterable
"""
可迭代:Iterable
可以使用for循环遍历！
迭代器:Iterator

isinstance
生成器就是一个迭代器

迭代器一定是可迭代的 可以使用next和for
可以迭代的不一定是迭代器 可以使用iter来将可迭代的转化为迭代器！

可迭代就是可以进行for循环！

next 取不到回报异常，可以进行异常捕获！
"""

# g1 = ()

from collections.abc import Iterable, Iterator, Generator

# print(isinstance(100, Iterable))
# print(isinstance(100, Iterator), isinstance((i for i in range(10)), Iterator))
#
# iterator1 = (i for i in range(10))
# print(type(iterator1), isinstance(iterator1, Iterator), isinstance(iterator1, Generator))


class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            result = self.current
            self.current += 1
            return result
#
# my_range = MyRange(1, 5)
# for num in my_range:
#     print(num)

#
# class MyStopIteration(StopIteration):
#     def __init__(self, massage="使用next越界了！"):
#         super().__init__()
#         self.massage = massage

# s = [1, 2, 3, 4, 5, 6]
# i = iter(s)
# # print(isinstance(i, Iterator))
# while 1:
#     try:
#         print(next(i))
#     except MyStopIteration as e:
#         print(e)
#         break


# """

# __iter__ 当迭代一个对象时触发，返回一个可迭代对象！
# 自定义迭代器
# __next__
# 自定义可迭代

# """


# class MyIterator:
#     """
#     自定义迭代器！
#     """

#     def __init__(self, datas):
#         self.datas = datas
#         self.current_index = -1

#     def __iter__(self):
#         """
#         返回一个可迭代的对象！

#         :return:self 返回一个迭代器，固定就是迭代器！
#         """
#         return self

#     def __next__(self):
#         """
#         才可以进行！for循环！
#         :return:
#         """
#         if self.current_index < len(self.datas) - 1:
#             self.current_index += 1
#             return self.datas[self.current_index]
#         else:
#             raise StopIteration("00100")  # 抛出异常，抛给了as e


# my_iterator = MyIterator([1, 2, 3])
# print(isinstance(my_iterator, Iterator))
# print(isinstance(my_iterator, Iterable))

# while 1:
#     try:
#         print(next(my_iterator))
#     except StopIteration:  #
#         # print(e)
#         e = StopIteration()
#         print(e)
#         break
# except IndexError:
#     print("下标越界！")
#     break

"""
当存储数据（小于20个时）时！生成器内存大   184      20的时候刚好相等，数组也是184 

"""

# 生成器的所占内存小，固定的是184

t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20)
print(t1.__sizeof__())
# print(184/20)
t2 = (_ for _ in range(1, 21))
print(t2.__sizeof__())
