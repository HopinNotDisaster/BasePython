#
# 扩展题


# # 1.使用for与while两种方法,计算500-1000以内能被3整除的数的个数
# count = 0
#
# # for
# # for i in range(501, 1000):
# # if i % 3 == 0:
# #     count += 1
# i = 501
# while i != 1000:
#     if i % 3 == 0:
#         count += 1
#     i += 1
#
# print(count)
#
# # 2.
# lower = 100  # 范围下限
# upper = 999  # 范围上限
# for num in range(lower, upper + 1):
#     # 将数字转换为字符串，并计算每个数字的 n 次幂之和
#     total = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         total += digit ** 3
#         temp //= 10
#     # 如果满足水仙花数条件，则打印该数
#     if num == total:
#         print(num)

# # 3.输入10个数字， 打印输入数字最大值与最小值的差
# a = int(input("请输入数字:"))
# i = int(input("请输入数字:"))
# Max = a if a > i else i
# Min = a if a < i else i
#
# n = 8
# while n:
#     n -= 1
#     tem = int(input("请输入数字:"))
#     Max = Max if Max > tem else tem
#     Min = Min if Min < tem else tem
# print(Max, Min)

# # 4.使用for与while两种方法求1000以内最大的10个质数的平均数
# count = 10
# i = 999
# total = 0
# while count:
#     j = 2
#     while j < i:
#         if i % j == 0:
#             i -= 1
#             break
#         else:
#             j += 1
#     else:
#         total += i
#         i -= 1
#         count -= 1
# print(total / 10)
#
# num = 10
# total = 0
# for i in range(999, 1, -1):
#     if num == 0:
#         break
#     for j in range(i - 1, 1, -1):
#         if i % j == 0:
#             break
#     else:
#         num -= 1
#         total += i
# print(total / 10)

# # 5.使用for与while两种方法计算n的阶乘和   5的阶乘和 =5！+4！+3！+2！+1！
# n = int(input("输入一个整数："))
# ans = 0
# for i in range(1, n + 1):
#     tem = 1  # tem用来存储i的阶乘
#     for j in range(1, i + 1):
#         tem *= j
#     ans += tem
# print(ans)
#
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

# # 6.一个五位数,若在它的后面写上一个7,得到一个六位数A,若在它前面写上一个7,得到一个六位数B,B是A的五倍,求此五位数
#
# for i in range(10000, 100000):
#     A = i * 10 + 7
#     B = 700000 + i
#     if B == A * 5:
#         print(i)
# # 7.随机生成5-10之间的数字，直到所有数字之和大于100，计算随机的次数
# import random
#
# count = 0
# total = 0
# while total <= 100:
#     count += 1
#     total += random.randint(5, 10)
#     print(total)
# print(count)

# 8.斐波那契数列指的是这样一个数列：1，1，2，3，5，8，13，21，34，55，89...
# 求第n个数是几                                 i  j  k ans
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
#


# # 9.找到1000以内相差为6的质数对（5,11）（7,13）...

# m到n 相差为k的素数对
# ans = []
# for i in range(m, n):
#     # 判断i是否为质数
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         # i是质数
#         for k in range(2, i + 6):
#             if (i + 6) % k == 0:
#                 break
#         else:
#             ans.append([i, i + 6])
# print(ans)
# #

# while True:
#     print("0.0")
#
# import math
#
# max_value = math.inf
# print(max_value, type(max_value))

# keyword
# random
# turtle

# 1.  导入请求模块
# from urllib import request
# import json
#
# count = 0
# # 2. 发起请求 将请求结果赋予 res 变量
# page = 1
# res = request.urlopen(
#     f"https://image.baidu.com/search/albumsdata?pn={30 * page}&rn=30&tn=albumsdetail&word=%E5%AE%A0%E7%89%A9%E5%9B%BE%E7%89%87&album_tab=%E5%8A%A8%E7%89%A9&album_id=688&ic=0&curPageNum={page}")
# page += 1
# # 3. 获取请求返回值  解码  将类型转换为字典
# res = res.read().decode()
# res = json.loads(res)
# # 4. 解析数据
# datas = res["albumdata"]["linkData"]
# print(res)
# for data in datas:
#     image_url = data["thumbnailUrl"]
#     # 5. 请求图片
#     res_image = request.urlopen(image_url)
#     res_image = res_image.read()
#     # 6. 保存图片
#     count += 1
#     file = open(f"D:\python2401\python基础语法\二十二.下载小狗图_爬取图片\{count}.jpg", "wb")
#     file.write(res_image)
#     file.close()
# print(f"总共{count}张图片")

def fun(m, n, k):
    if m > n or k < 0 or n <= 0:
        return
    ans = []
    for i in range(m, n):
        if i not in ans:
            # 判断i是否为质数
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                # i是质数
                for p in range(2, i + k):
                    if (i + k) % p == 0:
                        break
                else:
                    ans.append([i, i + k])
    return ans


print(fun(2, 1000, 6))
