# # 1.如何判断一个字符串是否为另一个字符串的子串（使用while与for两种方法）
# s0 = "abcd"
# s1 = "ababc"
# for i in range(len(s1) - len(s0) + 1):
#     for j in range(len(s0)):
#         if s0[j] != s1[i + j]:
#             break
#     else:
#         print("是")
#         break

# # 2.随机生成10个位于10-50之间的数字,求10个数的平均数
# import random

# l0 = []
# n = 10
# while n:
#     tem = random.randint(10, 50)
#     l0.append(tem)
#     n -= 1
# print(f"这10个数的平均数为：{sum(l0) / 10}")
# print(l0)


# # 3.求1000以内满足以下条件的质数对（两个质数的和还是质数 2+3=5）
# prime = []
# for i in range(2, 1000):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         prime.append(i)
# for p in range(len(prime)):
#     for q in range(p + 1, len(prime)):
#         if (prime[p] + prime[q]) in prime:
#             print(prime[p], prime[q])

# # 4.输入两个数，求两个数的最大公约数，最小公倍数
# n1 = int(input("输入："))
# n2 = int(input("输入："))
# ans1 = max(n1, n2)
# while 1:
#     if ans1 % n1 == 0 and ans1 % n2 == 0:
#         print("最大公约数", ans1)
#         break
#     ans1 += 1
# ans2 = min(n1, n2)
# while 1:
#     if n1 % ans2 == 0 and n2 % ans2 == 0:
#         print(ans2)
#         break
#     ans2 -= 1

# # 5.删除指定列表中所有的奇数 [1,2,3,4,5,6,7,8,9]
# # 结果 [2,4,6,8]
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(nums) - 1, -1, -1):
#     if nums[i] % 2 != 0:
#         nums.remove(nums[i])
# print(nums)

# # 6.输入字符串(数字字母)找到字符串中Ascii码最大的一个
# alphabets = input("输入：")
# nums = []
# for a in alphabets:
#     nums.append(ord(a))
# print(max(nums), chr(max(nums)))

# # 7.有两个列表[1,2,3,4,5] [‘a’,’b’,’c’,’d’,’e’]
# # 合并列表 [1, ‘a’, 2, ‘b’, 3, ‘c’, 4, ‘d’, 5, ‘e’]
# l1 = [1, 2, 3, 4, 5]
# l2 = ['a', 'b', 'c', 'd', 'e']
# # # print(str(l1).join(str(l2)))
# # print("".join(str(l1)))
# # print(str(l1))
# ans = []
# p = 0
# while 1:
#     if p >= len(l1) or p >= len(l2):
#         break
#     ans.append(l1[p])
#     ans.append(l2[p])
#     p += 1
# if p >= len(l1):
#     ans.extend(l2[p:])
# if p >= len(l2):
#     ans.extend(l1[p:])
# print(ans)

# # 8.有两个列表[1,2,3,4,5,6,7] [‘a’,’b’,’c’,’d’,’e’]
# # 合并列表 [1, ‘e’, 2, ‘d’, 3, ‘c’, 4, ‘b, 5, ‘a’,6,7]
# l1 = [1, 2, 3, 4, 5]
# l2 = ['a', 'b', 'c', 'd', 'e']
# # # print(str(l1).join(str(l2)))
# # print("".join(str(l1)))
# # print(str(l1))
# ans = []
# p = 0
# q = len(l2) - 1
# while 1:
#     if p >= len(l1) or q < 0:
#         break
#     ans.append(l1[p])
#     ans.append(l2[q])
#     p += 1
#     q -= 1
# if p >= len(l1):
#     ans.extend(l2[:q:-1])
# if q == -1:
#     ans.extend(l1[p:])
# print(ans)


# # 10.使用is_prime变量方法判定1000以内相差为6的质数对（不使用for else与while else）


# prime = []
# for i in range(2, 1000):
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime.append(i)
#
# for p in range(len(prime)):
#     if (prime[p] + 6) in prime:
#         print(prime[p], prime[p] + 6)

# # 11.随机10个不同的位于10-30之间的数放入数组，总共随机了多少次
# import random
#
# count = 0
# n = 10
# ans = []
# while n:
#     while 1:
#         count += 1
#         tem = random.randint(0, 20000)
#         if 10 < tem < 30 and tem not in ans:
#             ans.append(tem)
#             break
#     n -= 1
# print(ans)
# print(count)

# # 12.求两个数组的并集与交集[1,2,3,4,5]  [3,4,5,6,7]
# # 结果 [1,2,3,4,5,6,7] [3,4,5]
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [3, 4, 5, 6, 7]
# # # 默认俩个数组都是升序
# # for i in nums2:
# #     if i in nums1:
# #         pass
# #     else:
# #         nums1.append(i)
# # print(nums1)
# # 默认俩个数组都是升序
# intersection = []
# for i in nums2:
#     if i in nums1:
#         intersection.append(i)
# print(intersection)

# # 13.输入一个数字，求该数字的阶乘和 5！+4！+3！+2！+1！
# n = int(input("输入一个整数："))
# ans = 0
# i = 1
# while i <= n:
#     tem = 1  # tem用来存储i的阶乘
#     j = 1
#     while j <= i:
#         tem *= j
#         j += 1
#     ans += tem
#     i += 1
# print(ans)


# # 14.输入数字n ，将裴波那契前n个数放入数组
#
# ans = [1, 1, 2]
# n = int(input("输入n："))
# i = 1  #
# j = 2  #
# time = n - 3  # 往前走多少步
# while time:
#     tem = j + i
#     i = j
#     j = tem
#     ans.append(tem)
#     time -= 1
# print(ans)

# # 15.编写一个程序，生成包含n个随机整数的列表，其中每个整数的范围为[1,100]，并计算出其中的众数（出现次数最多的数）。
#
# import random

# l0 = []
# n = int(input("输入："))
# while n:
#     l0.append(random.randint(1, 10))
#     n -= 1
# print(l0)
#
# count = [0] * 101
# for i in l0:
#     count[i] += 1
# count_max = max(count)
#
# ans = []
# while count_max == max(count):
#     ans.append(count.index(count_max))
#     count[count.index(count_max)] = 0
# print(count)
# print(ans)
# # 16.计算二维列表中所有数字的平均数
# # [
# # [1,2,3],
# # [4,5,6],
# # [7,8,9]
# # ]
# l0 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# s = 0
# c = 0
# for i in range(len(l0)):
#     for j in range(len(l0[i])):
#         c += 1
#         s += l0[i][j]
# print(s / c)

# 17.实现二维数组的转置
#
# l0 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # ans = [
# #     [0, 0, 0],
# #     [0, 0, 0],
# #     [0, 0, 0]
# # ]
# ans = [[0] * 3 for i in range(3)]
# for i in range(len(l0)):
#     for j in range(len(l0[i])):
#         ans[j][i] = l0[i][j]
# print(ans)

# # 18.找出一个二维数组每列的最大值
# # [
# #     [1, 5, 9],
# #     [2, 3, 6],
# #     [7, 5, 3]
# # ]
# # 输入 7 5 9
# l0 = [
#     [1, 5, 9],
#     [2, 3, 6],
#     [7, 5, 3]
# ]
# for i in range(len(l0)):
#     tem = l0[0][i]
#     for j in range(1, len(l0[i])):
#         tem = max(l0[j][i], tem)
#     print(tem)

# # 19.对二维数组进行竖直镜像
# # [
# # [1,2,3],
# # [4,5,6],
# # [7,8,9]
# # ]
# #
# # [
# # [7,8,9],
# # [4,5,6],
# # [1,2,3]
# # ]
# #
# l0 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# ans = [[0] * 3 for i in range(3)]
#
# for i in range(len(l0)):
#     for j in range(len(l0[i])):
#         ans[len(l0) - i - 1][j] = l0[i][j]
# print(ans)


# # 20.自己编写方法对列表进行升序排列
# # [10,50,20,60,40,30]
# l0 = [10, 50, 20, 60, 40, 30]
# p = 1
# while p < len(l0):
#
#     q = p - 1
#     while q >= 0:
#         if l0[q] <= l0[q + 1]:
#             break
#         else:
#             tem = l0[q]
#             l0[q] = l0[q + 1]
#             l0[q + 1] = tem
#             q -= 1
#     p += 1
# print(l0)


# s = [0, 1, 2, ]
# print(s[1:1])

#
# def way(s, left, r):
#     if left == r:
#         return [1, left]  # 长度，起始点
#     if left + 1 == r and s[left] == s[r]:
#         return [2, left]
#     if s[left] == s[r] and way(s, left + 1, r - 1)[0] == r - left + 1 - 2:
#         return [r - left + 1, left]
#     return way(s, left, r - 1) if way(s, left, r - 1)[0] > way(s, left + 1, r)[0] else way(s, left + 1, r)
#
#
# #     01234
# s0 = "babad"
# ans = way(s0, 0, len(s0) - 1)
# print(ans)

# 字符串
# count
# swapcase
# center
# format


# 列表
# append
# insert
# remove
# reverse 无返回值
# clear
# sort
# pop 默认最后一个
# extend
# index
# count
# +
# *

#
# a = ["a", "b", "c"]
# ans = "".join(a)
# print(ans, type(ans))

# l0 = [
#     [1, 2, 3, 54, 77],
#     [4, 5, 6, 60, 84],
#     [7, 8, 9, 10, 11]
# ]
# for i in range(len(l0)):
#     for j in range(0, len(l0[0]) // 2):
#         temp = l0[i][j]
#         l0[i][j] = l0[i][len(l0[0]) - 1 - j]
#         l0[i][len(l0[0]) - 1 - j] = temp
# print(l0)



