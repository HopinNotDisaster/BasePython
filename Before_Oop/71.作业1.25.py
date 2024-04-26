# 使用函数封装完成以下题目
# 1.编写用户版管理系统，包含学生，课程，成绩
# 2.编写xmind汇总以下模块所有方法
# Keyword、random、turtle、math、datatime、time、calender
# Json、pickle、csv、urllib、sys

# 一、创建一个圆Circle类，
# 为该类提供一个初始化方法，用于初始化半径
# 为该类提供两个方法，
# 方法一用 于求圆的面积，方法二用于求圆的周长
# import math
import random


#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return math.pi * self.radius ** 2
#
#     def get_perimeter(self):
#         return 2 * math.pi * self.radius
#
#
# c1 = Circle(3.5)
#
# print(c1.get_area(), c1.get_perimeter())

# 二、创建Rectangle类，初始化属性width、height；
# 在Rectangle类中添加两个方法计算矩形的周长和面积；
# 在Rectangle类中添加方法输出矩形的周长和面积
# 生成10个矩形 width,height都位于 5-10之间  求周长与面积之和最大的一个矩形
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.height * self.width
#
#     def get_perimeter(self):
#         return self.width * self.height
#
#     def print_area(self):
#         print(self.get_area())
#         return
#
#     def print_perimeter(self):
#         print(self.get_perimeter())
#         return
#
#     def get_sum_area_and_perimeter(self):
#         return self.get_perimeter() + self.get_area()
#
#
# import sys
# from random import uniform
#
# n = 10
# my_max_value = -sys.maxsize - 1
# max_rectangle = Rectangle(0, 0)
# while n:
#     width = uniform(5, 10)
#     height = uniform(5, 10)
#     tem_rectangle = Rectangle(width, height)
#     if tem_rectangle.get_sum_area_and_perimeter() > my_max_value:
#         my_max_value = tem_rectangle.get_sum_area_and_perimeter()
#         max_rectangle = tem_rectangle
#     n -= 1
# print(my_max_value, max_rectangle.get_perimeter(), max_rectangle.get_area())
# 三、使用面向对象封装一个栈（百度一个 栈 ：后进先出）
# 提供插入数据与删除数据的方法。
# 删除的数据就是最后一个插入的数据，提供方法返回栈中元素的个数
# class Stack:
#     # 最大数量，空栈，满栈，入栈，出站，数量
#     def __init__(self, max_size):
#         self.max_size = max_size
#         self.items = []
#
#     def is_empty(self):
#         return not self.items
#
#     def is_full(self):
#         return len(self.items) == self.max_size
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def size(self):
#         return len(self.items)
#
#
# # s = Stack()
# s.push(35)
# print(s.size())
#
#
# # 四、新建学生类（学号，姓名，年纪）
#  	随机生成10个学生放入列表(年纪随机即可)，按学生的年纪对列表中的学生排序
# import random
#
#
# class Student:
#     def __init__(self, stu_id, age, name=""):
#         self.age = age
#         self.name = name
#         self.stu_id = stu_id
#
#     def get_age(self):
#         return self.age
#
#
# students = []
# for i in range(10):
#     students.append(Student(i, random.randint(18, 25)))
# students.sort(key=lambda e: e.get_age())
#
# for s in students:
#     print(s.age, s.stu_id)


# 五、编写汽车类（颜色，速度）
# 编写人类（名字，汽车实例）
# 编写列表 放入三个人， 遍历列表依次打印每个人的信息（包含汽车）

# class Car:
#     def __init__(self, colour, speed):
#         self.speed = speed
#         self.colour = colour
#
#     def display(self):
#         return f"汽车的颜色：{self.colour}，汽车的速度：{self.speed}"
#
#     def __str__(self):
#         return f"汽车的颜色：{self.colour},汽车的速度：{self.speed}"
#
#
# c1 = Car("白", 110)
# print(c1)
#
#
# class People:
#     def __init__(self, name, car):
#         self.car = car
#         self.name = name
#
#     def __str__(self):
#         return "0.0"
#
#     def display(self):
#         return f"{self.car}0.0"
#
#
# datas = []
# for i in range(3):
#     colour = input(f"第{i}个人车的颜色：")
#     speed = random.uniform(100, 120)
#     datas.append(People(str(i), Car(colour, speed)))
#     print(i, datas[i].name, datas[i].car.colour, datas[i].car.speed)
#
# # 六、使用turtle模块结合类封装一下功能，
# # 绘制圆形，绘制矩形，绘制三角形，绘制五角星，绘制爱心
# import turtle
#
#
# class Painter:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def paint_circle(radius):
#         # 创建一个 Turtle 对象
#         my_turtle = turtle.Turtle()
#
#         # 绘制一个半径为 3 的圆
#         my_turtle.circle(radius)
#
#         # 等待绘图窗口关闭
#         turtle.done()
#
#     @staticmethod
#     def paint_ractangle(wight, height):
#         # import turtle
#         canvas = turtle.Screen()
#         # 创建一个画布和画笔
#         pen = turtle.Turtle()
#
#         # 绘制矩形
#         pen.forward(wight)
#         pen.left(90)
#         pen.forward(height)
#         pen.left(90)
#         pen.forward(wight)
#         pen.left(90)
#         pen.forward(height)
#
#         # 关闭画布
#         canvas.exitonclick()
#
#     @staticmethod
#     def paint_triangle(side):
#         canvas = turtle.Screen()
#         pen = turtle.Turtle()
#
#         # 绘制三角形
#         pen.forward(side)
#         pen.left(120)
#         pen.forward(side)
#         pen.left(120)
#         pen.forward(side)
#
#         # 关闭画布
#         canvas.exitonclick()
#
#     @staticmethod
#     def paint_pentastar(side):
#         import turtle
#
#         # 创建一个画布和画笔
#         canvas = turtle.Screen()
#         pen = turtle.Turtle()
#
#         # 绘制五角星
#         for _ in range(5):
#             pen.forward(side)
#             pen.right(144)
#
#         # 关闭画布
#         canvas.exitonclick()
#
#     @staticmethod
#     def paint_love():
#         # 创建一个画布和画笔
#         canvas = turtle.Screen()
#         pen = turtle.Turtle()
#
#         # 设置画笔属性
#         pen.fillcolor("red")
#         pen.pensize(3)
#
#         # 绘制爱心
#         pen.begin_fill()
#         pen.left(140)
#         pen.forward(224)
#         for _ in range(200):
#             pen.right(1)
#             pen.forward(2)
#         pen.left(120)
#         for _ in range(200):
#             pen.right(1)
#             pen.forward(2)
#         pen.forward(224)
#         pen.end_fill()
#
#         # 关闭画布
#         canvas.exitonclick()
#
#
# painter1 = Painter()
# painter1.paint_love()
