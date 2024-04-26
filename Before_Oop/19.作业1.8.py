# # # 1.输入数字n求n的阶乘和   5的阶乘和 =5！+4！+3！+2！+1！
# num = int(input("输入一个整数："))
# ans = 0
# for i in range(1, num+1):
#     tem = 1
#     for j in range(1 , i+1):
#         tem *= j
#     ans += tem
# print(ans)

# # 2.9行9列的图形，控制各种显示各种位置三角形
# # 上三角
# for i in range(9):
#     for j in range(9):
#         if i <= j and i + j <= 8:
#             print(" * ", end="")
#         # elif i >= j and i + j >= 8:
#         #     print(" * ", end="")
#         else:
#             # pass
#             print("   ", end="")
#     print()
#
# # 下三角
# for i in range(9):
#     for j in range(9):
#         # if i <= j and i + j <= 8:
#         #     print(" * ", end="")
#         if i >= j and i + j >= 8:
#             print(" * ", end="")
#         else:
#             # pass
#             print("   ", end="")
#     print()
#
#     # 左三角
# for i in range(9):
#     for j in range(9):
#         # if i <= j and i + j <= 8:
#         #     print(" * ", end="")
#         if i >= j and i + j <= 8:
#             print(" * ", end="")
#         else:
#             # pass
#             print("   ", end="")
#     print()
#
#     # 右三角
# for i in range(9):
#     for j in range(9):
#         # if i <= j and i + j <= 8:
#         #     print(" * ", end="")
#         if i <= j and i + j >= 8:
#             print(" * ", end="")
#         else:
#             # pass
#             print("   ", end="")
#     print()
#
# # 3.输入3打印
# # *
# # ***
# # *****

n = 3
for i in range(3, 0, -1):
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# 4.已知两个三位数abc和cba之和为1333（即abc+cba=1333）求 a、b、c
#
# for i in range(1, 10):  # i  是 a
#     for j in range(1, 10):  # j 是c
#         if i + j == 13:  # i + j 必须等于13
#             # print(i, j)
#             for k in range(5):  # k是 b
#                 if i * 101 + k * 20 + j * 101 == 1333:
#                     print(i, k, j)
#         else:
#             continue

# # 5.编程求出满足以下条件的三位数:它除以11所得的商等于它各位数字之和.
# for i in range(1, 10):
#     for j in range(10):
#         # print(i, j)
#         for k in range(10):
#             if (i * 100 + j * 10 + j * 1) // 11 == i + j + k:
#                 print(i, j, k)
#

# # 6.求1000以内最大的5个能同时被3和6整除的数。
# n = 5
# for i in range(999, 0, -1):
#     if n == 0:
#         break
#     if i % 3 == 0 and i % 6 == 0:
#         n -= 1
#         print(i)
# # print(999/6)
#
# # 7.输入一个数字，如果这个数字是质数则打印该数字，否则则打印该数字最大的因数
# x = int(input("输入一个数："))
# for i in range(x - 1, 1, -1):
#     if x % i == 0:
#         print(i)
#         exit()
# print(x)

# 8.求1000以内所有质数的平均数.0...............................0.0.0.0..00.00.0..0.

#
# num = 6
# total = 5
# for i in range(4, 1000):
#     ifPrime = 1
#     for j in range(i - 1, 1, -1):
#         if i % j == 0:
#             ifPrime = 0
#             break
#     if ifPrime == 1:
#         num += 1
#         total += i
# print(total / num)

# n = 9
# for i in range(2, n - 1):
#     if n % i == 0:
#         print("不是质数")

count = 10
for i in range(999, 1, -1):
    if count == 0:
        break
    prime = 1
    for j in range(2, i - 1):
        if i % j == 0:
            prime = 0
            break
    if prime == 1:
        count -= 1
        print(i)
