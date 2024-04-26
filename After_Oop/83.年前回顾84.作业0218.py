# 一，什么叫python解释器，什么叫IDE
# python解释器是一个程序，是一个可以将我们写出来的python代码翻译成计算机可以看懂的语言的程序。
# IDE（Integrated Development Environment）
# 是集成开发环境。是一个应用程序可以提供编程和开发过程中的一体化工具。

# 二，常见的进制有哪些？int bin oct hex的作用和用法。
# 十进制，二进制，八进制，十六进制。
# int可以将字符串转为特定进制的整数。
# int("101", base=8)
# a = 0b10
# print(a, type(a))
# b = 10
# c = 0xA2B  # 十六进制
# print(c, type(c))
# d = oct(20)
# print(d)

# 三，什么是解释性语言，什么是编译型语言？
# 解释性语言就是解释器是一行一行的编译，当编译到某行时会即刻执行。执行效率较低。
# 编译型语言是将整个文件编译成一个可执行的机器码文件，再在相应的平台上执行。

# 四，python的输入与输出！
# a = input("进行输入吧！")
# print(a)

# 五，python的五种基本数据类型
# i = 10
# f = 3.17
# b = True
# n = None
# s = "1asdf1a"
# 以及在他们之间可以进行特定的相互转化！
# print(n, type(n))

# 六， python中所有的运算符汇总！
# 1.基本的算数运算符+，-，*，/，**，//，%
# 2.比较运算符==，>,>= ,<,<=，!=
# 3.逻辑运算符and,or,not
# 4.赋值运算符
# 5.位运算符 & | ~ ^ >> <<
# 6.成员运算符
# 7.身份运算符
# 8.其他运算符： (),[],{}

# 七，什么是顺序结构，循环结构，分支结构
# 顺序结构就是程序按照从上到下，从左到右的顺序进行解释和执行程序代码。
# 循环结构就是当给出的条件是True的时候，进入循环体，当循环体执行完毕之后在进行条件判断。
# 分支结构就是先进行条件判断，如果当前的条件是真，就执行下面的代码块，否则就执行else后的代码块或者下面的代码块。

# 八，字符串，列表，元组，字典的常用方法！
# 字符串：
# print("".find(""))
# "".title()
# "".center()
# "".format()
# "".count()
# 列表
# [].count()
# [].remove()
# [].append()
# [].sort()
# [].pop()
# [].clear()
# 元组
# (1,).count()
# (1,).index()
# 字典
# {}.clear()
# 集合
# s = set()
# s.update((1, 2,))
# s.pop()
# print(s)
# dic = {"A": 10, "B": 20}
# dic.clear()  # Remove all items from dic
# print(dic)
# {}.pop()
# dic.pop("A")  # 删除指定的键值对，（）里面只填入键即可！
# print(dic)
# {}.get()
# print(dic.get("A"))  # 有返回值，（）里面填入键，返回一个改键对应的值。
# {}.update()
# dic.update({"A": 'a', "C": '12'})
# 没有返回值，（）里面填入一个字典，新字典中的键也在原字典中，
# 则将原字典中的值进行覆盖。
# 若不在，则添加！
# print(dic)
# {}.items()
# dic = {"A": 10, "B": 11, "C": 12}
# for i in dic.items():
#     print(i, type(i))
# dic.items()  # 是一个可迭代类型！可以用于循环
# {}.setdefault()
# {}.popitem()
# {}.values()
# {}.fromkeys()
# {}.keys()
# 集合

# 九， 变量的类型转化方法
# 1.谁可以转化为int
# # float类型
# f = 1.0
# i = int(f)
# print(i)
# # str类型
# # bool类型
# b = True
# i0 = int(b)
# print(i0)
# # NoneType类型(不可以！！！)
# n = None
# i1 = int(n) # 该步骤报错！
# print(i1)
# 2.谁可以转化成float类型
# int类型
# i3 = 3
# f0 = float(i3)
# print(f0)
# str类型
# bool类型
# b = False
# f0 = float(b)
# print(f0)
# # NoneType类型(不可以！！！)
# n = None
# f1 = float(n)  # 该步骤报错！
# print(f1)
# 3.谁可以转化成str类型
# 4.谁可以转化成bool类型
# 5.谁可以转化成NoneType类型
# 在Python中，以下情况的值可以被转化为NoneType类型：
# 显式地使用None关键字来表示空值。
# 一个函数没有显式返回任何值时，默认返回None。
# 用del语句删除一个变量后，该变量的值会变成None。

# 十，切片的各种使用方法！
# 字符串切片
# s = "asdfghjklqwertyuiop"
# print(s[3:5])
# # 列表切片
# l0 = ["a", "d"]
# print(l0[::-1])
# # 十一，列表，元组，字典，集合的推导式
# l1 = [i for i in range(0, 100)]
# print(l1)
# t0 = (_ for _ in range(0, 100))

# 十二，函数定义，调用，实参，返回值
# 十三，参数的类型：位置参数，关键字参数，默认参数，可变列表参数，可变元组参数
# 可变元组参数传入的是k1 = 110,这样的，传入时时字典形式！
# def fun(num, key=5, much="一", *nums, ):
#     for i in range(0, num):
#         print(f"定义{much}个函数！")
#     print(f"key的值是{key}")
#
#
# fun(3, key=3)

# 十四，递归函数，匿名函数，闭包，装饰器
# def wai(f):
#     def nei():
#         print("aaaa")
#         f()
#
#     return nei
#
#
# @wai
# def fun():
#     print("原本的功能！")
#
#
# fun()

# def fun1(n):
#     if n == 1:
#         return 1
#     print("a")
#     return n * fun1(n - 1)
#
#
# print(fun1(3))

# 1.编写一个程序，输入梯形的上底 下底 和高 ，计算出来梯形的面积并显示出来。
# a1 = int(input("上底:"))
# a2 = int(input("下底:"))
# h = int(input("高:"))
# print(f"该梯形的面积为：{(a1 + a2) * h / 2}")
# 2.编程实现计算输入指定的天数(如46天)是几周零几天
# total_days = 46
# print(f"周数：{46 // 7}")
# print(f"余下的天数：{46 % 7}")
# 3.提示用户输入年龄，如果大于等于18，则告知用户可以查看，
# 如果小于10岁，则告知不允许查看，如果大于等于10岁并且小于18，
# 则提示用户是否继续查看（yes、no），如果输入的是yes则提示用户请查看，
# 否则提示"退出,你放弃查看"。
# age = int(input("输入你的年龄："))
# if age >= 18:
#     print("可以查看！")
# elif age >= 10:
#     choice = input("你真的要看吗？(请输入'yes'或者'no'。)")
#     if choice == 'yes':
#         print("请您查看！")
#     else:
#         print("退出！")
# else:
#     print("您不可查看！")
#
# 4.在400--500之间求一个数,它被2除余1,被5除余3,被9除余1,这个数是多少?
# for i in range(400, 501):
#     if i % 2 == 1 and i % 5 == 3 and i % 9 == 1:
#         print(i)
# 5.打印9*9乘法表（for循环嵌套）
# tem = 0
# for i in range(1, 10):
#     for j in range(1, i):
#         print(f"{i}*{j}={i * j}", end='\t')
#         tem = j
#     print(f"{i}*{tem + 1}={i * (tem + 1)}")
# 6.封装函数求1000以内最大的n个能同时被3和6整除的数的和。
# def fun6(n):
#     ret = 0
#     num = 0
#     for i in range(999, 0, -1):
#         if i % 3 == 0 and i % 6 == 0:
#             ret += i
#             num += 1
#             if num == n:
#                 return ret
#
#
# print(fun6(6))
#
#
# 7.使用for与while两种方法计算n的阶乘和   5的阶乘和 =5！+4！+3！+2！+1！
# total = 0
# for i in range(1, 6):
#     total += factorial(i)
# print(total)
# 8.找到1000以内相差为6的质数对（5,11）（7,13）...


# 9.封装函数求斐波那契数列第n个数字

# 10.封装函数判断一个字符串是否为回文字符串
# 回文：”abcdcba”, “1234554321”     不是回文：”abcdcdba”


# 11.随机出来10个不同的位于10-30之间的数放入数组，总共随机了多少次

# 12.找出一个二维数组每列的最大值
# arr = [
#     [1, 5, 9],
#     [2, 3, 6],
#     [7, 5, 3]
# ]
# #  7 5 9
# for i in range(len(arr)):
#     max_j = arr[0][i]
#     for j in range(1, len(arr[i])):
#         if arr[j][i] > max_j:
#             max_j = arr[j][i]
#     print(max_j)
# 13.使用冒泡与选择对以下列表进行排序
# nums = [10, 50, 20, 60, 40, 30]
# for i in range(len(nums) - 1):
#     for j in range(0, len(nums) - 1 - i):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
# print(nums)

# nums = [10, 50, 20, 60, 40, 30]
# for i in range(len(nums) - 1):
#     max_index = 0
#     for j in range(1, len(nums) - i):
#         if nums[j] > nums[max_index]:
#             max_index = j
#     nums[max_index], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[max_index]
# print(nums)
# 14.编写学生管理系统，实现以下需求
# 输入数字1，添加学生信息（名字，年纪，性别）
# 输入数字2，查看所有学生信息
# 输入数字3，统计学生平均年纪
# 输入数字4，统计学生性别比例
# 输入数字5，退出系统

# 15.常见模块的使用 keyword random math
# os sys datetime time
# calendar turtle
# import calendar
#
# year = 2024
# cal = calendar.TextCalendar(calendar.SUNDAY)
# # 创建一个 TextCalendar 对象，设置每周的起始日为星期天
# print(cal.formatyear(year, 2, 1, 1, 3))  # 打印该年份的日历
# year = 2024
# month = 2
# cal = calendar.TextCalendar(calendar.SUNDAY)
# print(type(cal))  # calendar.TextCalendar类   cal的类型！
# print(cal.formatmonth(year, month))
# weekday, days_in_month = calendar.monthrange(2024, 2)
# print("第一天是星期几：", weekday)
# print("该月总共有多少天：", days_in_month)


# 十六，使用open来读写文件

# with open("exercise.txt", "w") as f:
#     f.write("1223.3213231")
#     f.write("\n45.54")
# lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']

# import json

# data = {"name": "John", "age": 30, "city": "New York"}

# with open("data.json", "w") as f:
#     json.dump(data, f)

# import json
#
# with open("data.json", "r") as f:
#     data = json.load(f)  # load之后跟文件指针！loads之后是具体的数据！

# print(data, type(data))

# import pickle

# # 创建一个对象
# data = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# # 将对象序列化为字节流
# serialized_data = pickle.dumps(data)

# # 将字节流保存到文件
# with open('data.pickle', 'rb') as file:
#     print(file.read())

# 十八，oop
# 定义动物类
# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
#
#     def make_sound(self):
#         print(f"The {self.name} says {self.sound}")


# class Dog(Animal):
#     def __init__(self, name, sound):
#         Animal.__init__(self, name, sound)


# 创建动物对象
# dog = Animal("dog", "woof")
# cat = Animal("cat", "meow")

# 调用方法
# dog.make_sound()  # 输出对应的叫声！！！！
# cat.make_sound()  # 输出对应的叫声！！！！


# 十九，魔法方法！
# 就是形式上带有__的方法，在使用上，不需要自己调用，在某些特定的语句中会自动调用！
# class MyClass:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"My name is {self.name}"
#
#     def __del__(self):
#         pass


# obj = MyClass("Bob")
# print(obj)  # 输出：My name is Bob

# class MyList:
#     def __new__(cls, *args, **kwargs):
#         if hasattr(cls, "obj"):
#             return cls.obj
#         else:
#             obj = object.__new__(cls)
#             setattr(cls, "obj", obj)
#             return obj
#
#     def __init__(self, data):
#         self.data = data
#
#     def __len__(self):
#         return len(self.data)


# lst = MyList([1, 2, 3, 4, 5])
# print(len(lst))  # 输出：5

# # 二十，属性
# # 属性是属性，方法也是属性
# # 多继承，多个父类！
# class Grandfather:
#     pass
#
#
# print("爷类继承object类！")
#
#
# class Father(Grandfather):
#     pass
#
#
# print("父类继承爷类！")
#
#
# class Son(Father):
#     pass
#
#
# print("儿类继承父类！")
# # 属性有类属性和对象属性！

class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # 将函数name变成了属性性质
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


p1 = People("ZX", "18")
print(p1.name)
p1.name = "zx"
print(p1.name)
