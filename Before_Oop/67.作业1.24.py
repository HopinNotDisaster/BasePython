# import os
# import json
#
# datas = {
#     'students': [
#         {"id": 101, "name": "12", "age": 18, "sex": "男"}
#     ],
#     "class": [
#         {"id": 1001, "name": "C++"}
#     ],
#     "score": [
#         {"id": 10001, "sid": 101, "cid": 1001, "score": 98}
#     ],
#     'user': [
#         {'id': 11, 'name': 'aa', 'pwd': '123456'},
#         {'id': 12, 'name': 'bb', 'pwd': '111222'}
#     ]
# }
# file_name = "学生管理系统（完整）.txt"
# user_id = 13
#
#
# def load_datas():
#     global datas
#     if os.path.exists(file_name):
#         with open(file_name, "r", encoding="utf-8") as f:
#             datas = json.load(f)
#     else:
#         pass
#         # 如果没有文件，也就是第一次执行程序。
#         # with open(file_name, "w", encoding="utf-8") as f:
#         #     json.dump(datas, f)
#
#
# def save_datas():
#     with open(file_name, "w", encoding="utf-8") as f:
#         json.dump(datas, f)
#
#
# # def course():
# #     global course_id
# #     if n == 6:  # 添加课程
# #         while 1:
# #             tem_na = input("输入课程的名字,长度为2或者3：")
# #             if len(tem_na) > 3 or len(tem_na) < 2:
# #                 print("名字不合法！")
# #             else:
# #                 break
# #         datas["course"].append({"id": course_id, "name": tem_na})
# #         course_id += 1
# #         print("添加课程完成！")
# #     elif n == 7:  # 删除课程
# #         delete_id = int(input("输入要删除课程的ID："))
# #         for di in datas["course"]:
# #             if di["id"] == delete_id:
# #                 datas["course"].remove(di)
# #                 print("删除课程完成！")
# #         print("未查到此课程，删除课程失败！")
# #     elif n == 8:  # 修改课程
# #         modified_id = int(input("输入需要修改课程的id"))
# #         for di in datas["course"]:
# #             if di["id"] == modified_id:
# #                 while 1:
# #                     tem_na = input("输入新名字,长度为2或者3：")
# #                     if len(tem_na) > 3 or len(tem_na) < 2:
# #                         print("名字不合法！")
# #                     else:
# #                         break
# #                 di.update({"name": tem_na})
# #                 print("修改完成！")
# #                 break
# #         else:
# #             print("查找课程失败，无法修改！")
# #     # 下面是查看指定课程id信息
# #     elif n == 9:
# #         looked_id = int(input("输入需要查看课程的id"))
# #         for di in datas["course"]:
# #             if di["id"] == looked_id:
# #                 print(di)
# #                 break
# #         else:
# #             print("查找失败！")
# #
# #     elif n == 10:
# #         print(datas["course"])
#
#
# # def enroll():
# #     global user_id
# #     # 注册成功[{'id': 11, 'name': 'ab', 'pwd': '123456'}]
# #     tem_name = input("输入你的名字：")
# #     tem_pwd = input("输入你的密码：")
# #     datas["user"].append({"id": user_id, "name": tem_name, "pwd": tem_pwd})
# #     user_id += 1
# #     print("注册成功")
# #
# #
# # def login():
# #     tem_name = input("输入你的用户名：")
# #     tem_pwd = input("输入你的密码：")
# #     for u in datas["user"]:
# #         if u["name"] == tem_name and u["pwd"] == tem_pwd:
# #             print("登陆成功！")
# #             print("**********欢迎来到用户界面！**********", end="")
# #             return True
# #     else:
# #         print("用户名或者密码错误！")
# #         return False
# #
#
# def delete_student_2():
#     deleted_student_id = int(input("请输入要删除学生的id:"))
#     if isexist_student(deleted_student_id):
#         for di in datas["students"]:
#             if di["id"] == deleted_student_id:
#                 datas["students"].remove(di)
#                 count = len(datas["students"])
#                 save_datas()
#                 print(f"删除成功！现在还有{count}个学生。")
#                 return
#     else:
#         print("删除失败！")
#
#
# inf2 = """
# 0. 退出程序
# 1. 添加学生
# 2. 删除学生
# 3. 修改学生信息
# 4. 查看指定学生详细信息
# 5. 查看所有学生列表
# 6. 添加课程
# 7. 删除课程
# 8. 修改课程
# 9. 查看指定课程详细信息
# 10. 查看所有课程信息
# 11. 添加成绩
# 12. 删除成绩
# 13. 修改成绩
# 14. 查看指定成绩详细信息
# 15. 查看所有成绩信息
# 16. 查看所有不及格的成绩信息
# """  # 用户界面
# inf1 = """
# 0. 退出程序
# 1. 登录
# 2. 注册
# """  # 登录界面
#
#
# # print(inf1)
#
#
# def show_user_interface():
#     print(f"欢迎来到学生管理系统".center(30, "$"))
#     print("0. 退出程序")
#     print("1. 添加学生")
#     print("2. 删除学生")
#     print("3. 修改指定学生信息")
#     print("4. 查看指定学生信息")
#     print("5. 查看所有学生信息")
#     print("6. 添加课程")
#     print("7. 删除课程")
#     print("8. 修改指定课程信息")
#     print("9. 查看指定课程信息")
#     print("10. 查看所有课程信息")
#     print("11. 添加成绩")
#     print("12. 删除成绩")
#     print("13. 修改指定学生的指定课程的成绩信息")
#     print("14. 查看指定学生的指定课程的成绩信息")
#     print("15. 查看所有成绩信息")
#
#
# def select_check(tip, scope):
#     option = int(input(tip))
#     if option in scope:
#         return True, option
#     else:
#         print("输入内容不合法！请重新输入！")
#         return False, None
#
#
# def quit_process_0():
#     print("感谢使用！欢迎下次再来！")
#     exit()
#
#
# def view_all_students_5():
#     if isexist_student():
#         for st in datas["students"]:
#             print(st)
#     print("所有学生信息显示完毕！")
#
#
# def isexist_student(student_id=0):
#     if student_id == 0:
#         if len(datas["students"]) == 0:
#             print("该学生管理系统中还未有学生。")
#             return False
#         else:
#             return True
#     else:
#         for stu in datas["students"]:
#             if stu["id"] == student_id:
#                 return True
#         print(f"未找到id为{student_id}的学生！")
#         return False
#
#
# def isexist_class(class_id=0):
#     if class_id == 0:
#         if len(datas["class"]) == 0:
#             print("该系统中还未有课程。")
#             return False
#         else:
#             return True
#     else:
#         for c in datas["class"]:
#             if c["id"] == class_id:
#                 return True
#         print(f"未找到id为{class_id}的课程！")
#         return False
#
#
# def input_three_items():
#     while 1:
#         tem_na = input("输入名字,长度为2或者3：")
#         if len(tem_na) > 3 or len(tem_na) < 2:
#             print("名字不合法！")
#         else:
#             break
#     while 1:
#         tem_se = input("输入性别，男或者女：")
#         if tem_se != '男' and tem_se != '女':
#             print("性别不合法！")
#         else:
#             break
#     while 1:
#         tem_ag = int(input("输入年龄，15-25之间："))
#         if tem_ag >= 25 or tem_ag <= 15:
#             print("年龄不合法！")
#         else:
#             break
#     return tem_na, tem_ag, tem_se
#
#
# def show_isadd_interface():
#     print("是否要继续添加？")
#     print("1.继续！")
#     print("2.返回主菜单！")
#
#
# def add_student_1():
#     while 1:
#         base_information = input_three_items()
#         if isexist_student():
#             new_student = {"id": 1 + datas["students"][-1]["id"], "name": base_information[0],
#                            "age": base_information[1],
#                            "sex": base_information[2]}
#
#         else:
#             new_student = {"id": 101, "name": base_information[0],
#                            "age": base_information[1],
#                            "sex": base_information[2]}
#         # noinspection PyTypeChecke
#         datas['students'].append(dict(new_student))
#         save_datas()
#         print("添加成功！")
#         show_isadd_interface()
#         while 1:
#             option = select_check("请选择", [1, 2])
#             if option[0]:
#                 if option[1] == 1:
#                     break
#                 elif option[1] == 2:
#                     return
#             else:
#                 pass
#
#
# def input_class_name():
#     while 1:
#         class_name = input("请输入课程名：")
#         if 2 <= len(class_name) <= 10:
#             for c in datas["class"]:
#                 if c["name"] == class_name:
#                     print("输入的课程已存在，请重新输入！")
#                     break
#             else:
#                 return class_name
#         else:
#             print("输入的课程名不合法，请重新输入！")
#
#
# def add_class_6():
#     while 1:
#         class_name = input_class_name()
#         if isexist_class():
#             new_class = {"id": 1 + datas["class"][-1]["id"], "name": class_name}
#         else:
#             new_class = {"id": 1001, "name": class_name}
#         datas['class'].append(new_class)
#         save_datas()
#         print("添加成功！")
#         show_isadd_interface()
#         while 1:
#             option = select_check("请选择", [1, 2])
#             if option[0]:
#                 if option[1] == 1:
#                     break
#                 elif option[1] == 2:
#                     return
#             else:
#                 pass
#
#
# def watch_appointed_student_4():
#     watch_id = int(input("请输入你要查看学生的id:"))
#     if isexist_student(watch_id):
#         for stu in datas["students"]:
#             if stu["id"] == watch_id:
#                 print(stu)
#                 return
#
#
# def update_student_3():
#     stu_id = int(input("请输入你要更新学生的id："))
#     if isexist_student(stu_id):
#         base_information = input_three_items()
#         for s in datas["students"]:
#             if s["id"] == stu_id:
#                 s["name"] = base_information[0]
#                 s["age"] = base_information[1]
#                 s["sex"] = base_information[2]
#                 break
#         # noinspection PyTypeChecke
#         save_datas()
#         print("修改成功！")
#     else:
#         pass
#
#
# def delete_class_7():
#     deleted_class_id = int(input("请输入要删除课程的id:"))
#     if isexist_class(deleted_class_id):
#         for di in datas["class"]:
#             if di["id"] == deleted_class_id:
#                 datas["class"].remove(di)
#                 count = len(datas["class"])
#                 save_datas()
#                 print(f"删除成功！现在还有{count}个课程。")
#                 # 还要将score中相应的课程成绩删除！
#                 return
#     else:
#         print("删除失败！")
#
#
# def update_class_8():
#     class_id = int(input("请输入你要更新课程的id："))
#     if isexist_class(class_id):
#         class_name = input_class_name()
#         for di in datas["class"]:
#             if di["id"] == class_id:
#                 di["name"] = class_name
#                 save_datas()
#                 print("修改成功！")
#                 return
#     else:
#         pass
#
#
# def watch_appointed_class_9():
#     watch_id = int(input("请输入你要查看课程的id:"))
#     if isexist_class(watch_id):
#         for c in datas["class"]:
#             if c["id"] == watch_id:
#                 print(c)
#                 return
#
#
# def view_all_classes_10():
#     if isexist_class():
#         for c in datas["class"]:
#             print(c)
#     print("所有课程信息显示完毕！")
#
#
# def input_score():
#     while 1:
#         score = int(input("请输入该学生该门课程的成绩："))
#         if 0 <= score <= 100:
#             return score
#         else:
#             print("输入的成绩不合法，请重新输入！")
#
#
# def add_score_11():
#     while 1:
#         score_cid = int(input("请输入课程的id："))
#         score_sid = int(input("请输入学生的id："))
#         if isexist_student(score_sid) and isexist_class(score_cid):
#             if isexist_score_sid_cid(score_sid, score_cid):
#                 print("该学生的该门成绩已经存在了！")
#             else:
#                 score = input_score()
#                 datas["score"].append(dict({"id": 1 + datas["score"][-1]["id"] if len(datas["score"]) != 0 else 10001,
#                                             "sid": score_sid,
#                                             "cid": score_cid, "score": score}))
#                 save_datas()
#                 print("添加成功！")
#                 show_isadd_interface()
#                 while 1:
#                     option = select_check("请选择", [1, 2])
#                     if option[0]:
#                         if option[1] == 1:
#                             break
#                         elif option[1] == 2:
#                             return
#                     else:
#                         pass
#
#
# def isexist_score_sid_cid(sid, cid):
#     for c in datas["score"]:
#         if c["cid"] == cid and c["sid"] == sid:
#             return True
#     return False
#
#
# def isexist_score(score_id=0):
#     if score_id == 0:
#         if len(datas["score"]) == 0:
#             print("该系统中还未有成绩。")
#             return False
#         else:
#             return True
#     else:
#         for c in datas["score"]:
#             if c["id"] == score_id:
#                 return True
#         print(f"未找到id为{score_id}的成绩！")
#         return False
#
#
# def delete_score_12():
#     deleted_score_id = int(input("请输入要删除成绩的id:"))
#     if isexist_score(deleted_score_id):
#         for di in datas["score"]:
#             if di["id"] == deleted_score_id:
#                 datas["score"].remove(di)
#                 count = len(datas["score"])
#                 save_datas()
#                 print(f"删除成功！现在还有{count}个成绩。")
#                 return
#     else:
#         print("删除失败！")
#
#
# def update_appointed_score_13():
#     score_cid = int(input("请输入课程的id："))
#     score_sid = int(input("请输入学生的id："))
#     if isexist_score_sid_cid(score_sid, score_cid):
#         score = input_score()
#         for c in datas["score"]:
#             if c['cid'] == score_cid and c["sid"] == score_sid:
#                 c["score"] = score
#                 break
#         save_datas()
#         print("修改成功！")
#
#
# def watch_appointed_score_14():
#     watch_id = int(input("请输入你要查看成绩的id:"))
#     if isexist_score(watch_id):
#         for c in datas["score"]:
#             if c["id"] == watch_id:
#                 print(c)
#                 return


# def view_all_scores_15():
#     if isexist_score():
#         for c in datas["score"]:
#             print(c)
#     print("所有课程信息显示完毕！")
#
#
# def main():
#     load_datas()
#     while 1:
#         show_user_interface()
#         # n = input("请选择登录,注册还是退出:")
#         ret_option = select_check("尊敬的用户请选择你的操作:", [i for i in range(16)])
#         if ret_option[0]:
#             if ret_option[1] == 0:
#                 quit_process_0()
#             elif ret_option[1] == 1:
#                 add_student_1()
#             elif ret_option[1] == 2:
#                 delete_student_2()
#             elif ret_option[1] == 3:  # 3. 修改指定学生信息
#                 update_student_3()
#             elif ret_option[1] == 4:
#                 watch_appointed_student_4()
#             elif ret_option[1] == 5:
#                 view_all_students_5()
#             elif ret_option[1] == 6:  # 6. 添加课程
#                 add_class_6()
#             elif ret_option[1] == 7:
#                 delete_class_7()
#                 # delete_student()
#             elif ret_option[1] == 8:  # 8. 修改指定课程信息
#                 update_class_8()
#             elif ret_option[1] == 9:
#                 watch_appointed_class_9()
#             elif ret_option[1] == 10:
#                 view_all_classes_10()
#                 pass
#             elif ret_option[1] == 11:  # "11. 添加成绩"
#                 add_score_11()
#                 pass
#             elif ret_option[1] == 12:  # "12. 删除成绩"
#                 delete_score_12()
#             elif ret_option[1] == 13:  # "13. 修改指定学生的指定课程的成绩信息"
#                 update_appointed_score_13()
#             elif ret_option[1] == 14:  # "14. 查看指定学生的指定课程的成绩信息"
#                 watch_appointed_score_14()
#             elif ret_option[1] == 15:  # 15. 查看所有成绩信息
#                 view_all_scores_15()
#                 pass
#         else:
#             pass
#
#
# main()


# Keyword、
import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword("if"))  # True
# print(keyword.iskeyword("myvar"))  # False


# random、

import random

#
# # 生成一个 0 到 9 之间的随机整数
# random_number = random.randint(0, 9)  # 目前唯一一个闭区间的函数！
# print(random_number)
# count = 0
# while 1:

#     # 生成一个 0 到 1 之间的随机浮点数
#     random_float = random.random()
#     print(random_float)
#     if random_float == 0:
#         break

#     else:
#         count += 1

# turtle、
# import turtle

# t = turtle.Turtle()
#
# # 绘制正方形
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# # 关闭窗口
# turtle.done()
#
# # #
# import math
#
# # 输入圆的半径
# radius = float(input("请输入圆的半径："))
#
# # 计算圆的面积
# area = math.pi * radius ** 2
#
# # 输出结果
# print("圆的面积为：", area)
#


# 引入 datetime 模块
import datetime

# # 使用 模块 的方法
# print(datetime.strptime('%Y'))
# print(datetime.today())
#
# # 创建 datetime 对象
# d = datetime.datetime()  # 两个 datetime !! 第一个是模块，第二个是模块里面同名的类
# # 格式化为年月日，这个是 datetime 对象的方法，而不是模块的方法
# dStr = d.strftime('%Y-%m-%d')

# 注意还是两个datetime，这里是 datetime 类的方法
# dt = datetime.datetime.strptime('2021-09-01 10:53:13', '%Y-%m-%d')
#
# 报错！天，时分秒未转换
#
# print(dt)
dt = datetime.datetime.strptime('2021-09-01 10:53:13', '%Y-%m-%d %H:%M:%S')
# print(dt)
# 正常转换
# 2021, 9, 1, 10, 53, 13
#

# # time、
# import time
# print(time.time())
# # 1596760621.3079221
# print(time.ctime())
# print(time.localtime())
# print(time.gmtime())
# # calender
# import calendar
#
# # 将星期日设置为一周第一天
# # calendar.setfirstweekday(firstweekday=6)
#
#
# # 将星期日设置为一周第一天
# calendar.setfirstweekday(firstweekday=6)
# print(calendar.firstweekday())      # 6
# Json、
# import calendar
#
# # 2018年是平年，所以为False
# print(calendar.isleap(2018))  # False
# # 2008年是如年，所以为True
# print(calendar.isleap(2008))  # True


# # pickle、
file_name = "text.txt"
# with open(file_name, "wb", ) as f:
#     pickle.dump(dic, f)

# with open(file_name, "rb", ) as f:
#     context = pickle.load(f)
#     print(context, type(context))

# # # csv、
# import csv
#
# csv_reader = csv.reader(open("data.csv"))
# for row in csv_reader:
#     print(row)

# # urllib
# from urllib import request,parse
# url = 'http://httpbin.org/post'
# #请求头
# headers = {
# 	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
# 	'Host':'httpbin.org'
# }
# param = {
# 	'name':'Germey'
# }
# data = bytes(parse.urlencode(param),encoding='utf-8')
# req = request.Request(url=url,data=data,headers=headers,method='POST')
# '''
# 也可以通过add_header()方法逐个添加请求头
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0')
# '''
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))
