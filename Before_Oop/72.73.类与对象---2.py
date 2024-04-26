# class Person:
#     age = 10
#     sex = "保密"

#     # 在调用类之后先去执行这个初始化函数。
#     def __init__(self, name):
#         self.walk = "会走路。"
#         self.name = name
#         print(id(self))
#         print("正在根据Person类生成对象中！")

#     def update_name(self):
#         self.name = input("输入新的名字:")
#
#     def update_walk(self):
#         self.walk = input("描述一下，这个人走路有什么特点！\n")


# p1 = Person("jjj")
# print(id(p1))
# print(p1.name)

# p2 = Person("rrr")
# p2.update_name()
# print(p2.name)

# # print(p2.sex)
# # print(p1.sex)
# import math


# class Circle:
#     def __init__(self, radius, center):
#         self.center = center
#         self.radius = radius

#     def distance(self, another_circle):
#         return math.hypot(self.center[0] - another_circle.center[0], self.center[1] - another_circle.center[1])

#     def is_in(self, another_circle):
#         if self.distance(another_circle) < abs(self.radius - another_circle.radius):
#             return True
#         return False

#     def is_intersect(self, another_circle):
#         if self.distance(another_circle) == abs(self.radius - another_circle.radius) or self.distance(
#             another_circle) == abs(self.radius + another_circle.radius): :

#         def is_tangency(self, another_circle):
#             pass

#         def is_out(self, another_circle):
#             pass
class Queue:
    def __init__(self, maxsize):
        self.datas = []
        self.maxsize = maxsize

    def is_empty(self):
        if len(self.datas) == 0:
            return True
        return False

    def is_full(self):
        if len(self.datas) == self.maxsize:
            return True
        return False

    def enqueue(self, e):
        if not self.is_full():
            self.datas.append(e)
        else:
            print("已满队列！")

    def dequeue(self):
        if not self.is_empty():
            self.datas.pop(0)
        else:
            print("已空队列！")

    def size(self):
        return len(self.datas)




q1 = Queue(10)
q1.enqueue(3)
print(q1.size())
# # import os
# # import json
#
# datas = {
#     'students': [
#         {"id": 101, "name": 12, "age": 18, "sex": "男"},
#     ]
# }
# file_name = "小的学生系统(少但完整).txt"
# inf = """
# 输入数字1，添加学生信息
# 输入数字2，查看所有学生信息
# 输入数字3，统计学生平均年纪
# 输入数字4，统计学生性别比例
# 输入数字5，退出系统
# """  # 用户界面
#
#
# def select_check(tip, scope):
#     """
#     对用户输入的选项进行校验！
#     :param tip: 提示用户的信息。
#     :param scope: 用户合法输入的范围。
#     :return:
#     """
#     option = int(input(tip))
#     if option in scope:
#         return True, option
#     else:
#         print("输入内容不合法！请重新输入！")
#         return False, None
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
# class Student:
#     def __init__(self, stu_id, name, age, sex):
#         self.sex = sex
#         self.age = age
#         self.name = name
#         self.stu_id = stu_id
#
#     def __str__(self):
#         return f"学生id:{self.stu_id}\t学生姓名:{self.name}\t学生年纪:{self.age}\t学生性别:{self.sex}"
#
#
# class StudentManage:
#     def __init__(self):
#         self.students = []
#
#     def how_much_student(self):
#         return len(self.students)
#
#     def add_student(self):
#         while 1:
#             base_information = input_three_items()
#             new_student = Student(101 if self.how_much_student() == 0
#                                   else 1 + self.students[-1].stu_id,
#                                   base_information[0],
#                                   base_information[1],
#                                   base_information[2])
#             # noinspection PyTypeChecke
#             self.students.append(new_student)
#             for st in self.students:
#                 print(st)
#             print("添加成功！")
#             # save_datas()
#             show_isadd_interface()
#             while 1:
#                 option = select_check("请选择", [1, 2])
#                 if option[0]:
#                     if option[1] == 1:
#                         break
#                     else:
#                         return
#                 else:
#                     pass
#
#
# sm = StudentManage()
# sm.add_student()
#
#
# def show_user_interface():
#     print(f"欢迎来到学生管理系统".center(30, "$"))
#     print(inf)
#
#
# def quit_process():
#     print("感谢使用！欢迎下次再来！")
#     exit()
#
#
# def view_all_students():
#     if isexist_student():
#         for st in datas["students"]:
#             print(st)
#     print("所有学生信息显示完毕！")
#
#
# def isexist_student(student_id=0):
#     """
#     如果不传参，则判断的是是否有学生。
#     如果传入参数，就是判断指定的学生是否存在。
#     :param student_id:
#     :return:
#     """
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
# def add_student():
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
#         for st in datas["students"]:
#             print(st)
#         print("添加成功！")
#         # save_datas()
#         show_isadd_interface()
#         while 1:
#             option = select_check("请选择", [1, 2])
#             if option[0]:
#                 if option[1] == 1:
#                     break
#                 else:
#                     return
#             else:
#                 pass
#
#
# def get_average_age():
#     if isexist_student():
#         sum_age = 0
#         for stu in datas["students"]:
#             sum_age += stu["age"]
#         print(f"学生的平均年龄为{sum_age / len(datas['students'])}")
#
#
# def get_sex_ratio():
#     if isexist_student():
#         man_count = 0
#         for stu in datas["students"]:
#             if stu["sex"] == "男":
#                 man_count += 1
#         print(f"男生占比为{(man_count / len(datas['students'])) * 100}%")
#
#
# # def load_datas():
# #     global datas
# #     if os.path.exists(file_name):
# #         with open(file_name, "r") as f:
# #             datas = json.load(f)
# #     else:
# #         pass
# #
# #
# # def save_datas():
# #     global datas
# #     with open(file_name, "w") as f:
# #         json.dump(datas, f)
#
#
# def main():
#     # load_datas()
#     while 1:
#         show_user_interface()
#         ret_option = select_check("尊敬的用户请选择你的操作:", [i for i in range(1, 6)])
#         if ret_option[0]:
#             if ret_option[1] == 1:
#                 add_student()
#             elif ret_option[1] == 2:
#                 view_all_students()
#             elif ret_option[1] == 3:
#                 get_average_age()
#             elif ret_option[1] == 4:
#                 get_sex_ratio()
#             elif ret_option[1] == 5:
#                 quit_process()
#
#         else:
#             pass
#
# # main()
