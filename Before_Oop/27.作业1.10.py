# # 1.一直输入数字，直到数字之和为5的倍数，求输入数字的平均数
#
# count = 0
# total = 0
# while 1:
#     n = int(input("请输入一个数："))
#     total += n
#     count += 1
#     if total % 5 == 0:
#         break
# print(total / count)

# # 2.输入1 个正整数 n(n<=100)，计算并输出1＋1/2＋1/3＋……＋1/n 。
# n = int(input("请输入一个数："))
# ans = 0
# while n != 0:
#     ans += 1 / n
#     n -= 1
# print(ans)

# # 3.输入两个数，求两个数的最大公约数，最小公倍数
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

# # 4.已知四位数3025有一个特殊性质: 它的前两位数字30和后两位数字25的和是 55, 而	55的平方刚好等于该数(55*55=3025). 试编一程序打印所有具有这种性质的四位数.
#
# for i in range(10, 100):
#     for j in range(100):
#         add = i + j
#         if add ** 2 == i * 100 + j:
#             print(i * 100 + j)

# 5.找到500到1000以内满足以下的质数对（前两个差值是第二个与第三个差值的一半）
# ans = []
# for first in range(500, 1000):
#     # 判断first是否为质数
#     for first_j in range(2, first):
#         if first % first_j == 0:
#             break
#     else:
#         # first已经是质数
#         # 寻找second
#         for second in range(first + 1, 1000):
#             for second_j in range(2, second):
#                 if second % second_j == 0:
#                     break
#             else:
#                 # second 已经是质数
#                 tem = second - first
#                 third = second + 2 * tem
#                 for third_j in range(2, third):
#                     if third % third_j == 0:
#                         break
#                 else:
#                     if first < 1000 and second < 1000 and third < 1000:
#                         ans.append([first, second, third])
# print(ans)

# # 6.编程实现如下图列出的图形。7行
# # *           0
# # ***         1
# # *****       2
# # *******     3
# # *****      0
# # ***        1
# # *          2
#
# for i in range(4):
#     print("*" * (2 * i + 1))
# for i in range(3):
#     print("*" * ((2 - i) * 2 + 1))


# # 7.人猿泰山第一天摘了桃子若干 每天吃掉前一天的一半多一个 到第10天发现只剩一个了 求泰山一共摘了多少桃子
n = 1
day = 9
while day:
    n = (n + 1) * 2
    day -= 1
print(n)
import random

while 1:
    day = 9
    n = random.randint(0, 10000)
    tem = n
    while day:
        tem = (tem / 2) - 1
        day -= 1
    if tem == 1:
        print(n)
        break
# # 8.随机生成10个位于10-50之间的数字， 打印25以上与25以下平均数的差值
# import random
#
# n = 10
# count1 = 0
# total1 = 0
# count2 = 0
# total2 = 0
# while n:
#     x = random.randint(10, 50)
#     if x > 25:
#         count2 += 1
#         total2 += x
#     else:
#         count1 += 1
#         total1 += x
#     n -= 1
# print(total1 / count1 - total2 / count2)

# 9.斐波那契数列指的是这样一个数列：1，1，2，3，5，8，13，21，34，55，89...
# 求第n个数是几
# n = int(input("输入n："))
# i = 1  # n-2
# j = 1  # n-1
# k = 2  # 第n个
# if n == 1:
#     print(1)
# if n == 2:
#     print(1)
# if n == 3:
#     print(2)
# else:
#     ans = 0
#     time = n - 3  # 往前走多少步
#     while time:
#         ans = j + k
#         i = j
#         j = k
#         k = ans
#         time -= 1
# print(ans)
# #
# # 10.找出1000以内所有的完数（所有因子之和等于本身）
# print(6, 28, 496)
# for i in range(1, 1000):
#     tem = i
#     for j in range(1, tem):
#         if i % j == 0:
#             tem -= j
#     if tem == 0:
#         print(i)
