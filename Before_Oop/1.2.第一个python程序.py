# print("第一个python程序")
# print("程序是以行为单位运行的")
# print("注释是不会被执行的")
# # 此行为注释，可以不要空格但是不够漂亮。
# print("# 是注释的符号")
#
# # 变量：在程序执行过程中产生的数据
# # 数据的存储需要变量
# # 随着程序的执行，数据会发生变化，变量的值就会发生变化。
#
# # 变量的声明
# # 1.包含字母，数字，下划线（数字不可以开头）
# a_1 = 10
# a_1 = 10
# _a1 = 20
# # 1_a =30 数字不可以开头
# # 2.变量不可以使用关键字
# # python 中的保留字 会展现特殊的颜色的字
# abc = 10
# # def  是一个保留字
#
#
# import keyword
#
# k = keyword.kwlist
# print(k)  # 一共有35个关键字
# # 可以获取python中所有的关键字
# # 3.变量名字区分大小写
# # 4.若变量名有多个单词，用下划线链接
# # 5.变量名要有意义（多看一看大家都在使用什么变量名）
import math
import os
import random
import sys
from datetime import datetime

L = []
x = 3


# def pri_val(x):
#     L.append(x)
#
#
# x = 5
# pri_val(x)
# class People:
#     def __init__(self):
#         pass
#
#
# p1 = People()
# print(getattr(p1, "name"))
# print(math.floor(3.14))
# list2 = [3, 5, 6, 4, 2, 22, 45, 5]
# print(list2.reverse())
# print(list2)
# print(sys.getrefcount(3))

# l

# os.remove('D:\\python2401\\python基础语法\\Before_Oop\\3.变量和数据类型.py')

#
# # 将属性和方法写在class里面就叫封装便于调用与维护！
# class People:
#     def __init__(self, name):
#         self.name = name
#         pass
#
#     def eat(self):
#         print("好吃！爱吃！")
#
#
# # 玩家类继承父类人，可以直接使用人类的属性和方法。
# class Player(People):
#     def __init__(self, name, id):
#         super().__init__(name)
#         self.pler_id = id
#
#     # 通过eat方法来实现多态中的重写与重载！
#     def eat(self, food):
#         print(f"吃了{food}道具！")
#
#     def eat(self, food, hp):
#         print(f"吃了{food}道具！恢复了{hp}点血！")
#
#
# pioneer = Player("轻罗小扇", "147353639")
# # pioneer.eat()   # 如果Player类不写eat方法就会去使用父类的eat方法
# try:
#     pioneer.eat(food="小零食")
# except Exception:
#     print("python不支持重载，他必须让你输入hp")
# pioneer.eat("大零食", 50)


class Student:
    def __init__(self, sex, age, sid):
        self.sex = sex
        self.sid = sid
        self.age = age

    def __str__(self):
        return f"年龄：{str(self.age)}学号：{self.sid}性别：{self.sex}"


class StudentManage:
    def __new__(cls, *args, **kwargs):
        if hasattr(cls, "self"):
            return cls.self
        else:
            self = object.__new__(cls)
            cls.self = self
            return self

    def __init__(self):
        self.stus = []

    def add_stu(self, sex, age):
        sid = 1 + self.stus[-1].sid if self.stus else 101
        self.stus.append(Student(sex, age, sid))

    def show_stu_by_sex(self, sex):
        for stu in self.stus:
            if stu.sex == sex:
                print(stu)


sm = StudentManage()
sm.add_stu("男", 19)
sm1 = StudentManage()
sm.add_stu("女", 18)
sm1.show_stu_by_sex("女")
# slist = []
# for i in range(10):
#     slist.append(Student("小A", random.randint(10, 15), i))
#
# slist.sort(key=lambda e: (e.age, -e.sid), )
#
# for sl in slist:
#     print(sl)
