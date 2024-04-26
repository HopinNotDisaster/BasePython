# 一、饲养员类
# 数据：名字
# 方法：喂养(动物，草)，行走()
# 动物类
# 数据：名字
# 方法：  吃， 行走
# 食物类
# # 数据：名字
# # 实现饲养员给动物喂食物。
# class Food:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def walk(self):
#         print(f"{self.name}正在行走！")
#
#     def eat(self, food):
#         return f"{self.name}吃{food.name}！"
#
#
# class Breeder:
#     def __init__(self, name):
#         self.name = name
#
#     def feed(self, animal, food):
#         print(f"{self.name}正在让{animal.eat(food)}！")
#
#
# food = Food("草")
# animal = Animal("小绵羊")
# breeder = Breeder("呼哈")
# breeder.feed(animal, food)
#
# # 二、使用面向对象实现简易版本换装系统
# 性别（gender）、发型（hairstyle）、
# 武器（weapon）、头盔（helmet）、衣服(clothes)、
# 护腕（wristband）、裤子（pants）和鞋子（shoes）
# 武器和防具分为普通、稀有、经典、传奇四种类型，每种类型有+1到+8
# # 8种强化等级
# # 提供管理类，添加对应的方法实现换装
#
# class Hero:
#     def __init__(self, gender, hairstyle, em):
#         self.em = em
#         self.hairstyle = hairstyle
#         self.gender = gender
#
#
# class Equip:
#     def __init__(self, name, quality, degree):
#         self.name = name
#         self.degree = degree
#         self.quality = quality
#
#
# # class Helmet:
# #     def __init__(self, name, quality, degree):
# #         self.name = name
# #         self.degree = degree
# #         self.quality = quality
#
#
# # class Weapon:
# #     def __init__(self, name, quality, degree):
# #         self.name = name
# #         self.degree = degree
# #         self.quality = quality
#
#
# class EquipManage:
#     def __init__(self):
#         self.equips = []
#
#     def get_equip(self):
#         self.equips.append(Equip("究极霸王魔剑", "稀有", 6))
#
#     # def get_helmet(self):
#     #     self.equips.append(Helmet("三级头", "经典", 3))
#
#     def intensify_equip(self, i):
#         self.equips[i].degree += 1

# 三、根据tkinter 以及ai问答实现绘图软件
# 参考： Z:\share\python2401\第一阶段\90.GUI 绘图软件.exe
import tkinter as tk


def canvans_bg_change(colour):
    bg_color_var.set(colour)
    canvas.configure(bg=bg_color_var.get())
    canvas.pack()


def start_drawing_rec(event):
    global start_x, start_y, rect_id
    start_x = event.x
    start_y = event.y
    rect_id = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="black")  # 创建一个黑色矩形轮廓
    rect_id = canvas.create_rectangle(start_x, start_y, start_x, start_y, fill=fill_colour_var.get())  # 创建一个黑色矩形轮廓


def drawing_rectangle(event):
    global start_x, start_y, rect_id
    end_x = event.x
    end_y = event.y
    canvas.coords(rect_id, start_x, start_y, end_x, end_y)  # 更新矩形轮廓的坐标


def draw_rectangle():
    canvas.bind("<ButtonPress-1>", start_drawing_rec)  # 点击事件
    canvas.bind("<B1-Motion>", drawing_rectangle)


#
# def fill_colour_change(colour):
#
def start_drawing_cir(event):
    global start_x, start_y, circle_id
    start_x = event.x
    start_y = event.y
    circle_id = canvas.create_oval(start_x, start_y, start_x, start_y, outline="black")  # 创建一个黑色圆形轮廓
    circle_id = canvas.create_oval(start_x, start_y, start_x, start_y, fill=fill_colour_var.get(), tags="circle")


def drawing_circle(event):
    global start_x, start_y, circle_id
    global end_y, end_x
    end_x = event.x
    end_y = event.y
    radius = max(abs(end_x - start_x), abs(end_y - start_y))  # 计算半径
    canvas.coords(circle_id, start_x - radius, start_y - radius, start_x + radius, start_y + radius, )  # 更新圆形轮廓的坐标


def draw_circle():
    global end_y, end_x
    global start_x, start_y, circle_id
    initialize_coord()
    canvas.bind("<ButtonPress-1>", start_drawing_cir)
    canvas.bind("<B1-Motion>", drawing_circle)
    # canvas.create_oval(start_x, start_y, end_x, end_y, fill="red")


def initialize_coord():
    global end_y, end_x, start_x, start_y
    end_y = 0
    end_x = 0
    start_x = 0
    start_y = 0


def clear_canvas():
    canvas.delete("all")


rect_id = 0
circle_id = 0
end_y = 0
end_x = 0
start_x = 0
start_y = 0
root = tk.Tk()
root.title("GUI 绘图软件")
root.geometry("800x400")

bg_color_var = tk.StringVar()
bg_color_var.set("green")
canvas = tk.Canvas(root, width=200, height=300)
canvas.configure(bg=bg_color_var.get())
canvas.pack()

# 创建菜单栏
menu_bar = tk.Menu(root)
# 添加“绘图”菜单
draw_menu = tk.Menu(menu_bar, tearoff=0)
draw_menu.add_command(label="矩形", command=draw_rectangle)  # 添加“矩形”选项
draw_menu.add_command(label="圆形", command=draw_circle)  # 添加“圆形”选项
menu_bar.add_cascade(label="绘图", menu=draw_menu)

canvas_bg_menu = tk.Menu(menu_bar, tearoff=0)
canvas_bg_menu.add_command(label="红色", command=lambda: canvans_bg_change("red"))  # 添加“矩形”选项
canvas_bg_menu.add_command(label="蓝色", command=lambda: canvans_bg_change("blue"))  # 添加“圆形”选项
menu_bar.add_cascade(label="调整画布背景颜色", menu=canvas_bg_menu)

fill_colour_var = tk.StringVar()
fill_colour_var.set("white")
fill_menu = tk.Menu(menu_bar, tearoff=0)
fill_menu.add_command(label="紫色", command=lambda: fill_colour_var.set("purple"))
fill_menu.add_command(label="天蓝色", command=lambda: fill_colour_var.set("#87CEEB"))
menu_bar.add_cascade(label="调整填充颜色", menu=fill_menu)

clear_button = tk.Button(root, text="清屏", command=clear_canvas)
clear_button.pack()
# 创建画布
root.config(menu=menu_bar)
root.mainloop()

# 四、设计一个图书管理系统,
# 基类为类Book,要求有书名和作者属性，
# 由Book类派生子类AudioBook(有声书，需要具有演说者属性)，
# # 对于Book和AudioBook进行合理的属性及行为的抽象，
# class Book:
#     def __init__(self, name, author):
#         self.author = author
#         self.name = name
#
#     def readed(self):
#         return f"有人读{self.author}写的{self.name}了"
#
#
# class AudioBook(Book):
#     def __init__(self, name, author, speaker):
#         Book.__init__(self, name, author)
#         self.speaker = speaker
#
#     def listened(self):
#         return f"{self.speaker}给你读{self.author}写的{self.name}了"
#
#
# ab = AudioBook("飘", "飘的作者", "飘的演说者")
# print(ab.listened())
# 五、写出一个类People，并由该类做基类派生出子类Employee和Teacher。
# 其中People类具有name、age两个成员变量，分别为String类型、整型，
# 且具有公有的GetAge成员函数，用于返回age变量的值。
# Employee类具有成员变量empno,
# Teacher类有teacherNo成员变量。
# 编写show方法可以展示对应实例信息
# class People:
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#     def get_age(self):
#         return self.age
#
#     def show(self):
#         return f"名字：{self.name},年龄：{self.age}"
#
#
# class Teacher(People):
#     def __init__(self, teacher_num, name, age):
#         self.teacher_num = teacher_num
#         People.__init__(self, name, age)
#
#     def show(self):
#         return f"工号：{self.teacher_num}" + People.show(self)
#
#
# class Employee(People):
#     def __init__(self, empno, name, age):
#         self.empno = empno
#         People.__init__(self, name, age)
#
#     def show(self):
#         return f"工号：{self.empno}" + People.show(self)
#
#
# e1 = Employee(101, "aaa", 18)
# print(e1.show())
# 六、设计一个继承关系其中存在动物类Animal、狗类Dog和猫类Cat,
# 对于猫类和狗类都有一个吃eat方法，但是猫和狗的吃eat方法的实现不同，
# 请合理的设计出Animal Dog Cat
# class Animal:
#     def eat(self, food):
#         return f"吃{food}"
#

# 七、设计一个形状类Shape,方法:求周长和求面积
# 形状类的子类:Rect(矩形),Circle(圆形)
# Rect类的子类:Square(正方形)
# 不同的子类会有不同的计算周长和面积的方法创建三个
# # 不同的形状对象,放在列表里,分别打印出每个对象的周长和面积
# import math
#
#
# class Shape:
#     def __init__(self):
#         pass
#
#     def perimeter(self):
#         pass
#
#     def area(self):
#         pass
#
#
# class Rect(Shape):
#     def __init__(self, width, height):
#         super().__init__()
#         self.width = width
#         self.height = height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#
# class Square(Rect):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()
#         self.radius = radius
#
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#
# rect1 = Rect(3, 5)
# square1 = Square(4)
# circle1 = Circle(2)
# print("矩形的周长为：", rect1.perimeter())
# print("矩形的面积为：", rect1.area())
#
# print("正方形的周长为：", square1.perimeter())
# print("正方形的面积为：", square1.area())
#
# print("圆形的周长为：", circle1.perimeter())
# print("圆形的面积为：", circle1.area())
