import re
# def fun():
#     """
#     没有返回值！
#     一个输出一堆乱东西的函数。
#     :return:  无
#     """
# #     print("asdasdghjkl;")
# #     print(2222445674)
# #     return 0
# #
# #
# # def fun1(n):
# #     print(n ** 2)
# #
# #
# # print(fun1(78))
# # # 函数之后要空开两行的了
# # print(fun())
# # fun()
# # fun()
#
#
# def fun(n1, n2, n3, n4):
#     """
#     第一个参数加上第二个×第三个将其结果打印n4次！
#     :param n1:
#     :param n2:
#     :param n3:
#     :param n4:
#     :return:not None 就是返回True。
#     """
#     for i in range(n4):
#         print(n1 + n2 * n3)
#     # return not None
#
#
# print(fun(1, 5, 8, 9, ))

# 写一个函数，输入从start到stop并且相隔为step的质数对！
# def fun(start, stop, step):
#     """
#
#     :param start:
#     :param stop:
#     :param step:
#     :return:
#     """
#     ans = []
#     for i in range(start, stop + 1):
#         # 判断i是否为质数
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             # i是质数
#             for k in range(2, i + step):
#                 if (i + step) % k == 0:
#                     break
#             else:
#                 ans.append([i, i + step])
#     return ans
#
#
# ans = fun(1, 165, 25)
# print(fun(1, 165, 25))

import random

lis = []
i = 10
while i:
    tem = random.randint(50, 100)
    if tem in lis:
        i += 1
    else:
        lis.append(tem)
    i -= 1
print(lis)
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for j in range(9, -1, -1):
    if lis[j] % 2 == 0:
        pass
    else:
        lis.pop(j)
print(lis)
