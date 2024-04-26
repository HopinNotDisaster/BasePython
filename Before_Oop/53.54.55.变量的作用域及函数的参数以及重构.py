# i = 5
#
#
# def fun():
#     global i
#     i += 5
#     m = i
# #     return m + i
# #
# # #
# # # print(fun())
# # # print(i)
# # #
# #
# # def fun1(a, b, c, **kwargs):
# #     print(a, b, kwargs, c)
# #
# #
# # fun1(1, 2, di=1, c=3, d1=2, d3=4)
# from typing import Callable, Any
#
# fun: Callable[[Any, Any, Any], Any] = lambda x1, x2, x3: x1 * x2 * x3
#
# print(fun(3.2, -16.15, 15221))
# #
# #
# # def f2(n,f):
# #     for i in range(n):
# #         f()
# #
# #
# # f2(3,lambda :print("444"))
#
#
# l_dic = [
#     {"aaaa": 1111, "bbbb": 2222},
#     {"aaaa": 0000, "bbbb": 3333},
# ]
#
#
# def fun(n):
#     if n == 1:
#         return 1
#     return n + fun(n - 1)
#
#
# print(fun(2))
# import sys
#
# print(sys.getrecursionlimit())


def fun(n):
    print(n)


print(fun(3))
