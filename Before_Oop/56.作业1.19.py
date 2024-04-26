# 1.编写以下函数案例代码，并添加注释
# 函数定义，函数调用，函数形参，函数实参，函数返回值
# def fun(n1, n2):
#     return n1 + n2
# print(fun(3, 4))
# 函数调试
# 函数变量作用于
# g = 10
# def fun1():
#     global g
#     g += 10
#     return g
#
#
# print(fun1())
# 函数函数类型
# 匿名函数
# k = lambda: print("123")
# k()

# 递归函数

# # 2.编写一个函数，接受一个整数参数 n，返回斐波那契数列中前 n 个数字。
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# ans = []
# def fun3(n):
#     for i in range(1, n + 1):
#         ans.append(fibonacci(i))
#     return ans
#
#
# print(fun3(5))

# 3.编写一个函数，接受一个整数参数 n，返回 n 的阶乘和。
# def fun(n):
#     if n == 1:
#         return 1
#     return n * fun(n - 1)
# 4.编写一个函数，接受一个字符串参数，判断该字符串是否为回文
# def fun4(s):
#     n = len(s)
#     for i in range(n // 2):
#         if s[i] != s[n - 1 - i]:
#             return False
#     return True
#
# print(fun4("123123321321"))
# # 5.编写一个函数，接受一个列表参数，返回该列表中出现次数最多的元素。
# def fun(l):
#     dic = {
#
#     }
#     for i in l:
#         if str(i) in dic:
#             dic[str(i)] += 1
#         else:
#             dic[str(i)] = 1
#     print(dic)
#     return max(dic, key=dic.get)
# print(fun("aaasdasdasasfasfgfh13"))

# 6.编写一个函数，接受一个字符串参数，返回该字符串的所有排列组合。

# # 排列没有考虑到元素相同时的情况
# def fun6(s):
#     if len(s) == 1:
#         return [s]
#     if len(s) == 2:
#         return [s[0] + s[1], s[1] + s[0]]
#     else:
#         ans = []
#         for i in range(len(s)):
#             new_s = s[0:i] + s[i + 1:]
#             for j in fun6(new_s):
#                 ans.append(s[i] + j)
#         return ans

# print(fun6("121"))

# 组合！
# def fun6_(s):
#     if len(s) == 1:
#         return [s]
#     if len(s) == 2:
#         if s[0] != s[1]:
#             return [s[0] + s[1], s[1] + s[0]]
#         else:
#             return [s]
#     else:
#         headed = []
#         ans = []
#         for i in range(len(s)):
#             if s[i] in headed:
#                 pass
#             else:
#                 headed.append(s[i])
#                 new_s = s[0:i] + s[i + 1:]
#                 for j in fun6_(new_s):
#                     ans.append(s[i] + j)
#         return ans
# print(fun6_("121"))




# 7.编写一个函数，接受两个参数，一个是字符串 s，另一个是字符串 t，
# 判断 t 是否为 s 的字母异位词（即，两个字符串包含的字母相同，但顺序不同）。
# def fun7(s, t):
#     ans = fun6(s)
#     if t in ans:
#         return True
#     return False
#
#
# print(fun7("123", "213"))

# # 8.编写一个函数，求两个形参的最大公约数与最小公倍数
# def fun8(n1, n2):
#     ans = []
#     ans1 = max(n1, n2)
#     while 1:
#         if ans1 % n1 == 0 and ans1 % n2 == 0:
#             ans.append(ans1)
#             break
#         ans1 += 1
#     ans2 = min(n1, n2)
#     while 1:
#         if n1 % ans2 == 0 and n2 % ans2 == 0:
#             ans.append(ans2)
#             break
#         ans2 -= 1
#     return ans
# print(fun8(3, 5))

# # 9.编写一个函数，两个参数均为列表，返回两个列表中相同，和不同的元素
# def fun9(l1, l2):
#     s1 = set(l1)
#     s2 = set(l2)
#     ans1 = s1.intersection(s2)
#     ans2 = s1.difference(s2).union(s2.difference(s1))
#     return [ans1, ans2]
# print(fun9([1, 2, 3, 4], [2, 3, "a", "b"]))

# 10.编写函数，求输入的四位数字是否是闰年
#
# def fun10(n):
#     if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
#         return True
#     return False

# 11.编写函数，形参为列表，返回列表中的所有偶数
#
# def fun11(l):
#     ans = []
#     for i in l:
#         if i % 2 == 0:
#             ans.append(i)
#     return ans
#
#
# print(fun11([1, 6554, 165, 1615, 6, 516, 15615, 615, ]))
# # 12.编写函数，对形参列表进行冒泡排序，并将结果返回
# # 13.编写函数，对形参列表进行选择排序，并将结果返回
# def fun12(nums):
#     n = len(nums)
#     for i in range(n - 1):
#         for j in range(0, n - 1 - i):
#             if nums[j + 1] > nums[j]:
#                 pass
#             else:
#                 nums[j + 1], nums[j] = nums[j], nums[j + 1]
#     return nums
# nums = [10, 50, 20, 60, 40, 30]
# print(fun12(nums))
# def fun13(nums):
#     n = len(nums)
#     for i in range(n - 1):
#         min_index = i
#         for j in range(i + 1, n):
#             min_index = min_index if nums[min_index] < nums[j] else j
#         nums[min_index], nums[i] = nums[i], nums[min_index]
#     return nums
# nums = [10, 50, 20, 60, 40, 30]
# print(fun13(nums))


# 14.编写函数，对字符串 s = “ajldjlajfdljfddd”，去重并从小到大排序返回”adfjl”。
# def fun14(s):
#     """
#     仅排序
#     :param s:
#     :return:
#     """
#     n = len(s)
#     for i in range(n - 1):
#         min_index = i
#         for j in range(i + 1, n):
#             min_index = min_index if s[min_index] < s[j] else j
#         new_s = ""
#         for k in range(n):
#             if k == i:
#                 new_s += s[min_index]
#             elif k == min_index:
#                 new_s += s[i]
#             else:
#                 new_s += s[k]
#         s = new_s
#     return s
#
#
# def fun14_1(s):
#     """
#     去重
#     :param s:
#     :return:
#     """
#     re = ""
#     for i in s:
#         if i in re:
#             pass
#         else:
#             re += i
#     return re
# s = "ajldjlajfdljfddd"
# print(fun14(fun14_1(s)))


