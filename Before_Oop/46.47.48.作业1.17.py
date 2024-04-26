# # 1.编写Python中字符串，列表，元组，字典，集合五种数据类型常见操作方法
# # 包含案例，代码，注释
# # 字符串
# s1 = "   1 2 3   endd    "
# # s2 = s1.strip()  # 剔除两端的空格" ",第一次遇到非空格时，此语句结束。
# # 字符串不可变，所以这种操作方法会返回一个字符串
# # print(s2)
# # s3 = s1.lstrip()
# s4 = s1.rstrip("n")  # 从右向左剔除"n"，遇到第一个非"n"字符语句结束
# print(s4, )
# "\n", s4)
#
# import os
# s5 = " 1 23  4 5 7 85 6 "
# s51 = "011"
#
# print(s51.count("1", 0, 1))  # 返回s5字符串中的" "的个数
# #
# s6 = "***123***"
# s7 = s6.join(["a", "b", "c", "d"])  # join的（）里面填入一个iterable数据类型
# # # 将这个可迭代的数据类型展开，在每个元素之间插入s6,返回一个新的字符串
# print(s7)
# s8 = "***123***"
# print(s8.index("2"))
# 与count一样，不会对字符串进行操作，返回指定字符的下标，
# 默认从左往右，找到第一个就返回
# # 找不到就报错
# # print(s8.index("2", 3, 6)) # 同样的左闭右开，指定在字符串的哪个具体范围。
# # print(s8.find("0"))  # 找到的话，和index一样的。，如果找不到就会返回-1，不会报错
# # print(s8.find("3"))  # 同样可以像index一样指定一个左闭右开的一个范围。
# # print(s8.find("0", 3, 6))
# s9 = "***123***"
# # print(s9.split("*")) # 是一个对字符串的操作，所有返回操作的结果。以指定字符串分割
# # 该字符串没了，剩余的几部分字符串或者字符，成为返回列表的每个元素。
# # print(s9)
# s10 = "111111111111"
# # print(s10.split("0")) # 如果要以一个没有在该字符串的字符分割，则返回一个列表，该列表只有一个元素，就是原字符串。
# s11 = "1111111112"
# # print(s11.split("2")) # 有空！！就是指定分割符的左边没有元素，或者是一个同样的分隔符，返回的列表中就会有空！
# s12 = "醒醒醒醒啦"
# # print(s12.replace("醒", "太")) # 同样的，这个方法对原字符串操作了，所以会返回一个操作结果的字符串。原字符串不变。
# # print(s12.replace("醒醒", "太帅"))  # 左边的整体会替换右边的整体，遇到就替换，从左往右
# s13 = "1354134313"
#
# # print(s13.isdigit()) # 暂且不需要传入参数 ，连正负号都不可以有
#
# """
#         Return True if the string is a digit string, False otherwise.
#
#         A string is a digit string if all characters in the string are digits and there
#         is at least one character in the string.
#         """
# s14 = "基于脑肿瘤的算法设计论文"
#
# # print(s14.center(1))  # 也是修改类的     , 传入第一个参数为int类型，必须传入，如果传入的参数< len(s14)
# # 则打印的还是原来的字符串 。第二个参数是用设置以什么字符填充 but The fill character must be exactly one character long
# # print(s14.center( 20, "/"))  # 也是修改类的     , 传入第一个参数为int类型
# # print(s14)
# s15 = "san yue qi "
# # print(s15.capitalize()) # 只针对s15[0] ,如果该字符是小写字母，则将其大写，其余不变，返回。垃圾方法啊！！
# s16 = "1313a嚯嚯嚯sf4sa3fas"
# # print(s16.encode()) # 操作类方法，将其编码。
# s17 = "132asdasdfas132asasf121sa32sa"
# # print(s17.endswith("2sa"))  # 返回一个bool看一看该字符串是否是以给定的字符结尾。
# s18 = "1111{}33"
# # print(s18.format("222"))  # 刚需{} 还有很多
# s19 = "asdsadasd121322dsa54"
# print(s19.isalnum()) # 判断该字符串是否是由数字字母组成
# s20 = "sdgdssdsddssdfgfhthttedjggh"
# # print(s20.isalpha())
# s21 = '"1634张165"0s'
# print(s21)
# for i in s21:
#     print(i)
# print(len(s21))
# print(s21.isascii())
# #
# # # 列表
# # [].index()
# # [].count()
# # [].append()
# lex = [1, 2, 3, 4]
# lex.extend(['a', 'b', 'c'])
# print(lex)


# # [].remove()
# # [].sort()
# # [].clear()
# # [].pop()
# # [].insert()
# l1 = [1, 2, 3, 4, 5, 6, 7, ]
# l1.reverse()
# # print(l1)
#
#
# # 元组
# # ().index()
# # ().count()
# # 字典
#
# d0 = {
#     "aaa": 123, "bbb": 456, "ccc": 789, "fff": 1
# }
# # # # print(d0)
# # d0.pop("aa")  # pop 是必须要指定删除谁， 如果没有就报错
# # # print(d0)
# #
# # d0.clear()
# # d0.keys()
# # d0.items()
#
# print(d0.fromkeys("asdsafadsfaafsd", 1232))  # 与原字典无关，参数一：一个可迭代的对象。参数二，value值！

# d0.get()
# d0.values()

# d0.update({"a/a": 11})  # 无 ，则添加！！！
# d0.update({"aaa": 1})  # 有 ， 则更改  ~!!! 里面放入一个字典
# d0.setdefault("bb", 1)  # 无 ，则添加！！！   里面放入的是两个参数，第一个参数是指 键，第二个参数是指值
# d0.setdefault("bbb",1000) # 有，则保持原来的值

# print(d0)
#
#
# print(d0.popitem())  # 无法指定删除，会返回要删除的键值对，用元组返回！
# print(d0)

# # 集合
se = {1, 2, 5, 6, 8, }
se.update({6, 9, 10})  # 就是合并！
print(se)
se.discard()


# se.pop()
# print(se)

# se.clear()
# se.remove(2)
# print(se)

# se.intersection_update()
# se.intersection()
# se.add()
# se.difference()
# se.difference_update()
# se.issubset()
# se.union()
# se.symmetric_difference_update()
# se.symmetric_difference()
# se.issuperset()
# se.isdisjoint()


# 2.编写学生管理系统，实现以下需求
# 输入数字1，添加学生信息（名字，年纪，性别）
# 输入数字2，查看所有学生信息
# 输入数字3，统计学生平均年纪
# 输入数字4，统计学生性别比例
# 输入数字5，退出系统
#
#
# # 3.编写学生管理系统，实现增删改查
# # 输入数字1，添加学生信息（编号, 名字，年纪，性别）
# # 第一个学生id为101 后续学生自动加1
# # 输入数字2，查看所有学生信息
# # 输入数字3，查看指定学生信息
# # 输入学生id，显示对应学生信息
# # 输入数字4，修改学生信息
# # 输入学生id，输入学生新名字，新年纪，新性别
# # 输入数字5，删除指定学生
# # 输入学生id，删除指定学生
# # 输入数字0，退出系统
#
#
# inf = """
# 输入数字1，添加学生信息（编号, 名字，年纪，性别）
# 输入数字2，查看所有学生信息
# 输入数字3，查看指定学生信息
# 输入数字4，修改学生信息
# 输入数字5，删除指定学生
# 输入数字0，退出系统
# """
# print(inf)
# s_id = 102
# students = [
#     {'id': 101, 'name': '12', 'age': 18, 'sex': '男'},
#
# ]
# while 1:
#     n = int(input("输入你要进行的操作："))
#     if n == 1:
#
#         while 1:
#             tem_na = input("输入名字,长度为2或者3：")
#             if len(tem_na) > 3 or len(tem_na) < 2:
#                 print("名字不合法！")
#             else:
#                 break
#         while 1:
#             tem_se = input("输入性别，男或者女：")
#             if tem_se != '男' and tem_se != '女':
#                 print("性别不合法！")
#             else:
#                 break
#         while 1:
#             tem_ag = int(input("输入年龄，15-25之间："))
#             if tem_ag >= 25 or tem_ag <= 15:
#                 print("年龄不合法！")
#             else:
#                 break
#         students.append({"id": s_id, "name": tem_na, "age": tem_ag, "sex": tem_se})
#         s_id += 1
#         print("添加完成！")
#
#     elif n == 2:
#         print(students)
#     elif n == 3:
#         looked_id = int(input("输入需要查看学生的id"))
#         for di in students:
#             if di["id"] == looked_id:
#                 print(di)
#                 break
#         else:
#             print("查找失败！")
#     # if n == 3:
#     #     sum_ag = 0
#     #     for di in students:
#     #         sum_ag += di["age"]
#     #     print(sum_ag / len(students))
#     # if n == 4:
#     #     man = 0
#     #     woman = 0
#     #     for di in students:
#     #         if di["sex"] == "男":
#     #             man += 1
#     #         else:
#     #             woman += 1
#     #     print(f"{man}/{woman}")
#     elif n == 4:
#         modified_id = int(input("输入需要修改学生的id"))
#         for di in students:
#             if di["id"] == modified_id:
#                 while 1:
#                     tem_na = input("输入新名字,长度为2或者3：")
#                     if len(tem_na) > 3 or len(tem_na) < 2:
#                         print("名字不合法！")
#                     else:
#                         break
#                 while 1:
#                     tem_se = input("输入新性别，男或者女：")
#                     if tem_se != '男' and tem_se != '女':
#                         print("性别不合法！")
#                     else:
#                         break
#                 while 1:
#                     tem_ag = int(input("输入新年龄，15-25之间："))
#                     if tem_ag >= 25 or tem_ag <= 15:
#                         print("年龄不合法！")
#                     else:
#                         break
#                 di.update({"name": tem_na, "age": tem_ag, "sex": tem_se})
#                 print("修改完成！")
#                 break
#         else:
#             print("查找失败，无法修改！")
#     # if n == 5:
#     #     exit()
#     elif n == 5:
#         deleted_id = int(input("输入需要删除学生的id"))
#         for di in students:
#             if di["id"] == deleted_id:
#                 students.remove(di)
#                 break
#         else:
#             print("查找失败，无法删除！")
#         # if len(students) == 1:
#         #     students[0]["id"] = 101
#         # else:
#         #     for ind in students:
#         #         # students[ind].update({"id": students[ind]["id"] - 1})
#         #         if ind["id"] == deleted_id + 1:
#         #             ind["id"] -= 1
#         #             deleted_id += 1
#     elif n == 0:
#         exit()#     else:
#          print("输入不合法，请重新输入！")

# 4.自己编写方法对列表进行升序排列(学习选择排序) # [10,50,20,60,40,30]
#
# arr = [10, 50, 20, 60, 40, 30]
# n = len(arr)
# for i in range(n-1):
#     min_idx = i
#     for j in range(i+1, n):
#         if arr[j] < arr[min_idx]:
#             min_idx = j
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]
# print(arr)  # 输出：[10, 20, 30, 40, 50, 60]
#
# operation 操作


# def list_subdirectories(root_dir):
#     for item in os.listdir(root_dir):
#         item_path = os.path.join(root_dir, item)
#         if os.path.isdir(item_path):
#             print("子目录:", item_path)
#             list_subdirectories(item_path)
#         else:
#             print("文件", item_path)


# list_subdirectories("D:\\Program Files\\")
