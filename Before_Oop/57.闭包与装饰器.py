# 闭包三要素！
# 1. 嵌套
# 2. 返回
# 3. 局部变量
# i = 1
# def f1():
#     def f2():
#         global i
#
#         i += 1
#         print(i + 1)
#
# #     return f2
# #
# #
# # r = f1()
# # r()
# import time
# import random
#
#
# def decorator(f):
#     def time_cal():
#         begin = time.time()
#         f()
#         print(time.time() - begin)
#
#     return time_cal
#
#
# @decorator
# def bubbling():
#     n = len(nums1)
#     for i in range(n - 1):
#         for j in range(0, n - 1 - i):
#             if nums1[j + 1] > nums1[j]:
#                 pass
#             else:
#                 nums1[j + 1], nums1[j] = nums1[j], nums1[j + 1]
#
#
# def select(nums):
#     n = len(nums)
#     for i in range(n - 1):
#         min_index = i
#         for j in range(i + 1, n):
#             min_index = min_index if nums[min_index] < nums[j] else j
#         nums[min_index], nums[i] = nums[i], nums[min_index]
#     return nums
#
#
# nums1 = []
# for i in range(10000):
#     nums.append(random.randint(1, 500))
#
# print(bubbling(nums))
# # print(select(nums))

import json

dic = {"aaa": 111, "bbb": 222}
dic_s = json.dumps(dic)
# print(dic_s, type(dic_s))
dic_y = json.loads(dic_s)
print(dic_y, type(dic_y))
