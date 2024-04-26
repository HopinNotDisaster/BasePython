# 使用函数封装完成以下题目
# 一、创建一个名为 Person 的类，拥有 name 和 age 两个属性。实例化几个 Person 对象，并打印它们的属性。
class Person:
    # 在调用类之后先去执行这个初始化函数。
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return f"name:{self.name},age:{self.age}"

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


p1 = Person("a", 18)
p2 = Person("b", 20)
print(p1, p2, sep="\n")
import random

# 二、创建一个名为 BankAccount 的类，拥有 balance 属性
# 和 deposit()、withdraw() 两个方法。实例化一个 BankAccount 对象，然后进行一些存款和取款操作。
# class BankAccount:
#     # 在调用类之后先去执行这个初始化函数。
#     def __init__(self, balance):
#         self.balance = balance
#
#     def deposit(self, n):
#         self.balance += n
#
#     def withdraw(self, n):
#         self.balance -= n
#
#     def __str__(self):
#         return f"当前的资产还有：{self.balance}"
#
#
# ba1 = BankAccount(1000)
# ba1.deposit(10000)
# print(ba1)

# 三、创建一个名为 Car 的类，拥有 brand 和 color 两个属性，
# 以及 start() 和 stop() 两个方法。实例化一个 Car 对象，并调用 start() 和 stop() 方法。

# class Car:
#     def __init__(self, brand, colour):
#         self.colour = colour
#         self.brand = brand
#
#     def start(self):
#         print(f"{self.colour}{self.brand}车开始行驶。")
#
#     def stop(self):
#         print(f"{self.colour}{self.brand}车停止行驶。")
#
#
# c1 = Car("玛莎拉蒂", "蓝色的")
# c1.start()
# c1.stop()
# 四、创建一个名为 Employee 的类，拥有 name、salary 和 hire_date 三个属性。
# 实现一个计算员工服务年限的方法，并打印出员工的名字、薪水和服务年限。

# 看不懂！

# class Employee:
#     def __init__(self, name, salary, hire_date):
#         self.hire_date = hire_date
#         self.salary = salary
#         self.name = name


# 五、创建一个名为 Student 的类，拥有 name、id 和 scores 三个属性。
# scores 是一个字典，包含多个科目的成绩。为 Student 实现一个名为 average_score() 的方法，
# 计算该学生的平均分数
# class Student:
#     def __init__(self, name, student_id, scores):
#         self.name = name
#         self.id = student_id
#         self.scores = scores
#
#     def average_score(self):
#         total_score = 0
#         num_subjects = 0
#         for subject, score in self.scores.items():
#             total_score += score
#             num_subjects += 1
#         return total_score / num_subjects
#
#
# student_scores = {'Math': 90, 'English': 85, 'Science': 95}
# student1 = Student('A', '001', student_scores)
#
# # 计算平均分数并输出结果
# average = student1.average_score()
# print(f"The average score of {student1.name} is {average}")

# 六、编写汽车类（颜色，速度）
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
# # c1 = Car("白", 110)
# # print(c1)
#
#
# class People:
#     def __init__(self, name, car):
#         self.car = car
#         self.name = name
#
#     # def display(self):
#     #     return f"{self.car}0.0"
#
#     def __str__(self):
#         return f"我叫{self.name},我的车{self.car}"
#
#
# datas = []
# for i in range(3):
#     colour = input(f"第{i}个人车的颜色：")
#     speed = random.uniform(100, 120)
#     datas.append(People(str(i), Car(colour, speed)))
#     print(datas[i])

# 七、编写学生类，课程类，成绩类 以及对应的管理类完成学生管理系统实现
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
#         self.students = [stu1]
#
#     def how_many_student(self):
#         return len(self.students)
#
#     def isexist_student(self, stu_id):
#         for stu in self.students:
#             if stu.stu_id == stu_id:
#                 return True
#         print(f"未找到id为{stu_id}的学生！")
#         return False
#
#     def add_student(self):
#         base_information = input_three_items()
#         new_student = Student(101 if self.how_many_student() == 0
#                               else 1 + self.students[-1].stu_id,
#                               base_information[0],
#                               base_information[1],
#                               base_information[2])
#         # noinspection PyTypeChecke
#         self.students.append(new_student)
#         for st in self.students:
#             print(st)
#         print("添加成功！")
#
#     def show_all_students(self):
#         if self.how_many_student():
#             for st in self.students:
#                 print(st)
#             print("展示完毕！")
#         else:
#             print("无学生。")
#
#     def show_appointed_student(self, stu_id):
#         if self.how_many_student():
#             for st in self.students:
#                 if st.stu_id == stu_id:
#                     print(st)
#                     break
#             else:
#                 print("未找到！")
#         else:
#             print("无学生。")
#
#     def delect_student(self, stu_id):
#         if self.how_many_student():
#             for st in self.students:
#                 if st.stu_id == stu_id:
#                     self.students.remove(st)
#                     break
#             else:
#                 print("未找到！")
#         else:
#             print("无学生。")
#
#
# class Curriculum:
#     def __init__(self, cur_id, name, ):
#         self.cur_id = cur_id
#         self.name = name
#
#     def __str__(self):
#         return f"课程id:{self.cur_id}\t课程姓名:{self.name}"
#
#
# class CurriculumManage:
#     def __init__(self):
#         self.curriculums = [cur1, cur2]
#
#     def isexist_curriculum(self, cur_id):
#         for stu in self.curriculums:
#             if stu.cur_id == cur_id:
#                 return True
#         print(f"未找到id为{cur_id}的课程！")
#         return False
#
#     def how_many_curriculum(self):
#         return len(self.curriculums)
#
#     def add_curriculum(self):
#         tem_na = input("输入课程名字,长度为2或者3：")
#         new_curriculum = Curriculum(101 if self.how_many_curriculum() == 0
#                                     else 1 + self.curriculums[-1].cur_id,
#                                     tem_na)
#         # noinspection PyTypeChecke
#         self.curriculums.append(new_curriculum)
#         for st in self.curriculums:
#             print(st)
#         print("添加成功！")
#         # save_datas()
#
#     def show_all_curriculums(self):
#         if self.how_many_curriculum():
#             for st in self.curriculums:
#                 print(st)
#             print("展示完毕！")
#         else:
#             print("无课程。")
#
#     def show_appointed_curriculum(self, cur_id):
#         if self.how_many_curriculum():
#             for st in self.curriculums:
#                 if st.cur_id == cur_id:
#                     print(st)
#                     break
#             else:
#                 print("未找到！")
#         else:
#             print("无课程。")
#
#     def delect_curriculum(self, cur_id):
#         if self.how_many_curriculum():
#             for st in self.curriculums:
#                 if st.cur_id == cur_id:
#                     self.curriculums.remove(st)
#                     break
#             else:
#                 print("未找到！")
#         else:
#             print("无课程。")
#
#
# class Score:
#     def __init__(self, sco_id, stu_id, cur_id, score):
#         self.score = score
#         self.cur_id = cur_id
#         self.stu_id = stu_id
#         self.sco_id = sco_id
#
#     def __str__(self):
#         return f"学生id:{self.stu_id}\t学生成绩id:{self.sco_id}\t" \
#                f"该成绩对应课程id:{self.cur_id}\t成绩:{self.score}"
#
#
# class ScoreManage:
#     def __init__(self, ):
#         self.scores = [sco1]
#         self.cm = cm
#         self.sm = sm
#
#     def isexist_sid_cid_score(self, score_sid, score_cid):
#         for stu in self.scores:
#             if stu.stu_id == score_sid and stu.cur_id == score_cid:
#                 return True
#         return False
#
#     def add_score(self):
#         score = int(input("请输入该学生该门课程的成绩："))
#         score_cid = int(input("请输入课程的id："))
#         score_sid = int(input("请输入学生的id："))
#         if self.sm.isexist_student(score_sid) and \
#                 self.cm.isexist_curriculum(score_cid):
#             if self.isexist_sid_cid_score(score_sid, score_cid):
#                 print("该学生的该门成绩已经存在了！")
#             else:
#                 self.scores.append(Score(1 + self.scores[-1].sco_id
#                                          if len(self.scores) != 0 else 1,
#                                          score_sid,
#                                          score_cid, score))
#                 print("添加成功！")
#
#     def isexist_score(self, score_id):
#         for c in self.scores:
#             if c.sco_id == score_id:
#                 return True
#         print(f"未找到id为{score_id}的成绩！")
#         return False
#
#     def delete_score(self):
#         deleted_score_id = int(input("请输入要删除成绩的id:"))
#         if self.isexist_score(deleted_score_id):
#             for di in self.scores:
#                 if di.sco_id == deleted_score_id:
#                     self.scores.remove(di)
#                     count = len(self.scores)
#                     print(f"删除成功！现在还有{count}个成绩。")
#                     return
#         else:
#             print("删除失败！")
#
#     # def update_appointed_score_13():
#     #     score_cid = int(input("请输入课程的id："))
#     #     score_sid = int(input("请输入学生的id："))
#     #     if isexist_score_sid_cid(score_sid, score_cid):
#     #         score = input_score()
#     #         for c in datas["score"]:
#     #             if c['cid'] == score_cid and c["sid"] == score_sid:
#     #                 c["score"] = score
#     #                 break
#     #         save_datas()
#     #         print("修改成功！")
#     #
#     # def watch_appointed_score_14():
#     #     watch_id = int(input("请输入你要查看成绩的id:"))
#     #     if isexist_score(watch_id):
#     #         for c in datas["score"]:
#     #             if c["id"] == watch_id:
#     #                 print(c)
#     #                 return
#
#     def view_all_scores(self):
#         if len(self.scores):
#             for c in self.scores:
#                 print(c)
#         print("所有课程信息显示完毕！")
#
#
# cur1 = Curriculum(1001, "C++")
# cur2 = Curriculum(1002, "Java")
# sco1 = Score(1, 101, 1001, 98)
# stu1 = Student(101, "aaa", 19, "男")
# cm = CurriculumManage()
# sm = StudentManage()
# # sm.add_student()
# sco_m = ScoreManage()
# sco_m.view_all_scores()
# 八、使用turtle模块结合类封装一下功能，
# 绘制圆形，绘制矩形，绘制三角形
# from turtle import Turtle, Screen
#
#
# class Painter:
#     def __init__(self):
#         self.pen = Turtle()
#         self.canvas = Screen()
#
#     def paint_circle(self, radius):
#         self.pen.circle(radius=radius)
#         self.canvas.exitonclick()
#
#     def paint_ractangle(self, wight, height):
#         # 绘制矩形
#         self.pen.forward(wight)
#         self.pen.left(90)
#         self.pen.forward(height)
#         self.pen.left(90)
#         self.pen.forward(wight)
#         self.pen.left(90)
#         self.pen.forward(height)
#         self.canvas.exitonclick()
#
#     def paint_triangle(self, side):
#         # 绘制三角形
#         self.pen.forward(side)
#         self.pen.left(120)
#         self.pen.forward(side)
#         self.pen.left(120)
#         self.pen.forward(side)
#         self.canvas.exitonclick()
# painter1 = Painter()
# # painter1.paint_circle(100)
# painter1.paint_ractangle(50, 100)
# painter1.paint_triangle(300)
# 九、编写装饰器两个案例（统计时间开销，添加权限校验），添加详细注释
# import time
#
#
# def time_cost(f):
#     def in_time_cost():
#         start = time.time()
#         f()
#         print(f"花费时间为：{time.time() - start}")
#
#     return in_time_cost
#
#
# def add_permission_check(f):
#     def in_add_permission_check():
#         if input("请输入用户名：") == "aaa":
#             f()
#         else:
#             print("错误！")
#
#     return in_add_permission_check
#
#
# @add_permission_check
# @time_cost
# def case():
#     return input("请输入你想输入的内容：")
#
#
# case()

# 十、使用面向对象封装一个队列与栈
# 提供是否满、是否空、数量、入队出队，入栈出站对应方法
# class Queue:
#     def __init__(self, maxsize):
#         self.datas = []
#         self.maxsize = maxsize
#
#     def is_empty(self):
#         if len(self.datas) == 0:
#             return True
#         return False
#
#     def is_full(self):
#         if len(self.datas) == self.maxsize:
#             return True
#         return False
#
#     def enqueue(self, e):
#         if not self.is_full():
#             self.datas.append(e)
#         else:
#             print("已满队列！")
#
#     def dequeue(self):
#         if not self.is_empty():
#             self.datas.pop(0)
#         else:
#             print("已空队列！")
#
#     def size(self):
#         return len(self.datas)
#
#
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return not self.items
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[-1]
#
#     def size(self):
#         return len(self.items)
#
#
# q1 = Queue(10)
# q1.enqueue(3)
# print(q1.size())

# 十一、编写角色类，拥有血量【3000,5000】和攻击力【100,300】
#  随机10个角色（血量，攻击力随机）放入列表
#      列表中的角色依次攻击下一个（最后一个攻击第一个）
#  角色死亡后移除列表，输出最后存货角色信息
# class Hero:
#     def __init__(self, hp, atk, hid):
#         self.hid = hid
#         self.atk = atk
#         self.hp = hp
#
#     def attacked(self, hero):
#         self.hp -= hero.atk
#
#     def __str__(self):
#         return f"血量还有{self.hp},atk为{self.atk},编号为{self.hid}"
#
#
# class HeroManage:
#     def __init__(self):
#         self.heros = []
#
#     def update_heros(self):
#         for h in self.heros:
#             if h.hp <= 0:
#                 self.heros.remove(h)
#
#
# hm = HeroManage()
# for i in range(10):
#     hm.heros.append(Hero(random.randint(3000, 5000), random.randint(100, 300), i))
#     print(hm.heros[i])
#     if len(hm.heros) >= 2:
#         hm.heros[i].attacked(hm.heros[i - 1])
# begin = 0
# while len(hm.heros) != 1:
#     tem_len = len(hm.heros)
#     hm.heros[(begin + tem_len) % tem_len].attacked(hm.heros[(tem_len + begin - 1) % tem_len])
#     begin = (begin + 1) % tem_len
#     print(hm.heros[begin])
#     hm.update_heros()
#
# print(hm.heros[0])

# 十二、饲养员类
# 数据：名字
# 方法：喂养(动物，草)
#               行走()
# 动物类
# 数据：名字
# 方法：吃
#   行走
# 食物类
# 数据：名字
# 实现饲养员给动物喂食物。
# class Food:
#     def __init__(self, name):
#         self.name = name


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
# 十三、使用面向对象实现简易版本换装系统

# 性别（gender）、发型（hairstyle）、
# 武器（weapon）、头盔（helmet）、衣服(clothes)、护腕（wristband）、裤子（pants）和鞋子（shoes）
# 武器和防具分为普通、稀有、经典、传奇四种类型，每种类型有+1到+8   8种强化等级
# 提供管理类，添加对应的方法实现换装

# class Character:
#     def __init__(self, gender, hairstyle, weapon, helmet, clothes, wristband, pants, shoes):
#         self.gender = gender
#         self.hairstyle = hairstyle
#         self.weapon = weapon
#         self.helmet = helmet
#         self.clothes = clothes
#         self.wristband = wristband
#         self.pants = pants
#         self.shoes = shoes
#
#     def change_hairstyle(self, new_hairstyle):
#         self.hairstyle = new_hairstyle
#
#     def change_weapon(self, new_weapon):
#         self.weapon = new_weapon
#
#     def change_helmet(self, new_helmet):
#         self.helmet = new_helmet
#
#     def change_clothes(self, new_clothes):
#         self.clothes = new_clothes
#
#     def change_wristband(self, new_wristband):
#         self.wristband = new_wristband
#
#     def change_pants(self, new_pants):
#         self.pants = new_pants
#
#     def change_shoes(self, new_shoes):
#         self.shoes = new_shoes
#
#
# class Equipment:
#     def __init__(self, name, equipment_type, enhancement_level):
#         self.name = name
#         self.equipment_type = equipment_type
#         self.enhancement_level = enhancement_level
#
#     def enhance(self):
#         if self.enhancement_level < 8:
#             self.enhancement_level += 1
#             print(f"{self.name} 强化成功！强化等级：+{self.enhancement_level}")
#         else:
#             print(f"{self.name} 已达到最大强化等级！")
#
#     def __str__(self):
#         return f"名称：{self.name} 类型：{self.equipment_type} 强化等级：+{self.enhancement_level}"
#
#
# # 创建角色对象
# character = Character("男性", "短发", "普通剑", "普通头盔", "普通衣服", "普通护腕", "普通裤子", "普通鞋子")
#
# # 创建装备对象
# sword = Equipment("普通剑", "武器", 1)
# helmet = Equipment("普通头盔", "头盔", 1)
# clothes = Equipment("普通衣服", "衣服", 1)
# wristband = Equipment("普通护腕", "护腕", 1)
# pants = Equipment("普通裤子", "裤子", 1)
# shoes = Equipment("普通鞋子", "鞋子", 1)
#
# # 输出当前角色装备信息
# print("当前角色装备：")
# print(f"发型：{character.hairstyle}")
# print(character.weapon)
# print(character.helmet)
# print(character.clothes)
# print(character.wristband)
# print(character.pants)
# print(character.shoes)
#
# # 角色换装
# character.change_hairstyle("长发")
# character.change_weapon(sword)
# character.change_helmet(helmet)
# character.change_clothes(clothes)
# character.change_wristband(wristband)
# character.change_pants(pants)
# character.change_shoes(shoes)
#
# # 输出更换后的角色装备信息
# print("\n更换后的角色装备：")
# print(f"发型：{character.hairstyle}")
# print(character.weapon)
# print(character.helmet)
# print(character.clothes)
# print(character.wristband)
# print(character.pants)
# print(character.shoes)
#
# # 强化装备
# sword.enhance()
# sword.enhance()
# sword.enhance()

# 十四、根据tkinter 以及ai问答实现绘图软件
# 参考： Z:\share\python2401\第一阶段\90.GUI 绘图软件.exe
