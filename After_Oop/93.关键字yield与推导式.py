# g1 = (i for i in range(10))
#
#
# def f1():
#     yield 200
#
#     return 10000
#
#
# r = f1()
# # print(type(r))
# while 1:
#     try:
#         data = next(r)
#         print(data)
#     except StopIteration as e:
#         print("取完了", e)
#         break
from collections.abc import Iterable, Iterator


# import Iteration as Iteration


class MyGenerate:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        yield current
        while current < self.end:
            self.start += 1


my_generate = MyGenerate(1, 6)
print(isinstance(my_generate, Iterable))
print(isinstance(my_generate, Iterator))  # 没next就不是迭代器！
