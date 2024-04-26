# # 1.输入一个字符串，去除该字符串中所有数字后打印该字符串
# ans = ""
# string = input("请输入一个字符串：")
# for i in string:
#     if i.isdigit():
#         pass
#     else:
#         ans = ans + i
# print(ans)

# # 2.重复输入字符串，如果输入的字符串中都是字母，打印该字符串，否则继 datetime


# 4.输入一个日期格式如“2008/08/08”，将 输入的日期格式转换为“2008年-8月-8日后输出
from datetime import date, datetime

input_date = input("请输入日期：")
input_date1 = datetime.strptime(input_date, "%Y/%m/%d")
# 格式化为指定的输出格式
output_date = input_date1.strftime("%Y年-%#m月-%#d日")  # #保留一位
print("转换后的日期:", output_date)

# # 3.输入一个字符串找出其中所有字符”a”的位置
# string = input("请输入一个字符串：")
# for i in range(len(string)):
#     if string[i] == 'a':
#         print(i)

# # 4.输入一个日期格式如“2008/08/08”，将 输入的日期格式转换为“2008年-8月-8日后输出
# from datetime import datetime
# s = input("请输入:")
# new_s = s.split("/")
# print(new_s[0] + "年-", int(new_s[1]), "月-", int(new_s[2]), "日", sep="")

# # 5.如何判断一个字符串是否为另一个字符串的子串（自己遍历，不使用index,find等方法）

# s1 = "123456789"
# s2 = "567"
# print(s2 in s1)

# # 6.重复输入数字，如果连续输入两次素数则退出程序，否则继续输入

# ans1 = 0
# ans2 = 0
# while 1:
#     while 1:
#         n1 = int(input("输入："))
#         for i in range(2, n1):
#             if n1 % i == 0:
#                 ans1 = 0
#                 ans2 = 0
#                 break
#         else:
#             ans1 = n1
#             break
#
#     while 1:
#         n2 = int(input("输入："))
#         for i in range(2, n2):
#             if n2 % i == 0:
#                 ans1 = 0
#                 ans2 = 0
#                 break
#         else:
#             ans2 = n2
#             break
#     if ans1 != 0 and ans2 != 0:
#         print(ans1, ans1)
#         break

# 7.判断一个字符串是否为回文字符串
# # 回文：”abcdcba”, “1234554321”     不是回文：”abcdcdba”
#
# s = input("输入：")
# n = len(s)
# for i in range(n // 2):
#     if s[i] != s[n - 1 - i]:
#         break
# else:
#     print(s)

# # 8.输入一个字符串，逆序输出内容，奇数位舍弃
# # “abcdefg”      “geca”
# #  0123456
# # string = input("请输入一个字符串：")
# s = "123456"
# print("".join(reversed(s)))
# for i in range(len(s)):
#     if i % 2 == 0:
#         print(s[i], end="")

# # 9.将第一个字符串与第二个字符串进行拼接
# # abcdefg  1234 拼接结果a4b3c2d1efg
# s1 = "abcdefg"
# s2 = "1234"
# n1 = len(s1)
# n2 = len(s2)
# p = 0
# q = n2 - 1
# while p < n1 and q >= 0:
#     print(s1[p] + s2[q], end="")
#     q -= 1
#     p += 1
# if q >= 0:
#     print(s2[q:0])
# if p < n1:
#     print(s1[p:n1])
# # 10.编写一个程序，接受用户输入的字符串，将其中的所有空格替换为连字符（-），并打印出结果。
# string = input("请输入一个字符串：")
# print(string.replace(" ", "-"))




