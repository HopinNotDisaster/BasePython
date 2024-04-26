"""
keyword     关键字
turtle      乌龟绘图
random      随即模块
math        数学
datetime    日期时间
time        时间模块
calendar
csv excel
json pickle
sys   os
urllib
tkinter  GUI
pygame


re 正则：用于匹配，搜索，
优势：执行效率极高！！！！
劣势：可读性不强
"""

# import calendar


# print(re)
# re.I 就是忽略大小写！

# r = re.match(r".\w{2}", "Hello_World", re.I)
# if r:
#     print(r.group())

# 第一个参数是模式
# 第二个参数是目标字符串
# 第三个参数是忽略大小写 re.I

#  dir
# match 匹配成功 返回一个match实例！
# findall  寻找所有！
# """
# 字符匹配 .匹配任意字符
#     """
# \d\d匹配连着的两个数字！
# \w 字母数字 下划线！！！
# \W 取反！！！
# \s空白字符 空格
# \S取反！！！ 非空白


# \s \S \w \W \d \D
# 大写就是取反！
# r = re.findall(r"\w", "he\tllo wor\nld")
# print(type(r), r)

# findall 找到所有，返回列表！

# re.match(pattern, string, flags=0)：从字符串的开头开始匹配模式，如果匹配成功则返回一个匹配对象，否则返回None。
# fullmatch不仅需要从头开始，还要匹配到结束！！！
# 只能从头开始！
import re

#
# pattern = r"."
# string = "hello world"
# r = re.search(pattern, string, flags=0)  # 可以从任意的位置开始！
# print(type(r), r)
#
# # re.findall(pattern, string, flags=0)：查找字符串中所有与模式匹配的子串，并以列表的形式返回。
#
# # re.finditer(pattern, string, flags=0)：返回一个迭代器，迭代器中的每个元素都是一个匹配对象，表示字符串中的一个匹配。
#
#
# # r = re.sub("h", "HHH", "hellh", count=0, flags=0)
# # print(r)
# # ：用指定的替换字符串repl替换字符串中与模式匹配的部分。如果指定count参数，则最多替换count次。
# # subn 就是比sub多了一个替换了几个元素的内容！
# r = re.subn("h", "HHH", "hellh", count=0, flags=0)  # count等于0或者count大于可替换的所有个数，就会替换所有！
# print(r)
# # split
# # s
# # split split split
# r = re.split("h", "ohklsdgnlsdho", maxsplit=0, flags=0)
# print(r)
# ：根据模式对字符串进行分割，并返回分割后的子串列表 将h当作刀来使用，不包括h了 ，并且会返回""空！
# 正则模块！！！

# *
# 可以重复 0-n次


# """
# .*默认是贪婪模式
# .*？是非贪婪模式（尽可能少的匹配！）
# {n}匹配n次！
# {n,m}匹配n到m次！
# """
#
# r = re.findall(r"\d{2,3}", "1234")  # 一次尽可能多的匹配
# # 不会匹配二次两个的，而是匹配一次三个的然后丢掉一个！
# print(r)

# .代表任意字符串 不能匹配"" \n
# r = re.match(r".", "")
# print(r, type(r), r.group())
# .*可以匹配空是*给.的能力，而不是.自己的能力！，.*可以匹配"" a b ab 但是.*选择一次性匹配尽可能多的元素！
r = re.findall(r".*?", "ac bd")  # .*就相当于..............或者""
print(r, type(r))  # 一次匹配尽可能少的元素！

# 特殊字符 []
# [^    ] 取反！
# [a-zA-Z0-9_] 就相当于\w
#
# ()分组

#
# #
# from urllib import request
# import re
#

# datas = [
#
# ]
#
#
#
# res = request.urlopen("https://tieba.baidu.com/t/f/?class=college")
# res = res.read().decode()
# # print(res)
# schools = re.findall(
#     r'<a class="each_topic_entrance_item" href="(.*?)" data-fid="\d+"> (.*?)</a>',
#     res
# )

# # print(schools)
# for school in schools:
#     print(f"https:" + school[0], school[1], )
#     website = "https:" + school[0]
#     school_res = request.urlopen(website)
#     school_res = school_res.read().decode()
#     # print(school_res)
#     modules = re.findall(r'<div class="module_item"><p class="module_name">(.*?)</p>', school_res)
#     print(modules)
#     module_res = school_res.split('module_item')
#     for i in range(len(module_res) - 1):
#         module_titles = re.findall(r'href="//tieba.baidu.com/p/\d+">(.*?)</a>', module_res[i + 1])
#         print(module_titles)


# <a class="each_topic_entrance_item" href="//tieba.baidu.com/t/f/2030690" data-fid="2030690"> 安徽工程大学</a>
# <a class="each_topic_entrance_item" href="//tieba.baidu.com/t/f/93952" data-fid="93952"> 安徽理工大学</a>
