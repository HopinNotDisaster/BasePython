# 使用函数封装完成以下题目
# 一、根据tkinter
# 以及ai问答实现绘图软件
# 按照以下流程编写
# # 1. 空窗体 初始化 标题 logo
# # 2. 初始化 菜单 画布 状态栏
# # 3. 添加菜单事件  绘制矩形 直线 圆形  撤销 清除 退出
# # 4. 添加鼠标事件 左键点击 左键拖拽 左键抬起 右键抬起
# # 5. 当前选择图形 当前选择颜色  状态栏
# # 6. 鼠标点下绘制图形  鼠标拖拽更新绘制  鼠标抬起结束绘制
#
# import tkinter as tk
# from tkinter import colorchooser
# from tkinter import font
#
#
# class Draw_Gui:
#     def __init__(self):
#         self.str_current_shape = ""
#         self.max_id = 0
#         self.current_color = "black"
#         self.init_root()
#         self.init_canvas()
#         self.init_status()
#         self.init_menu()
#         self.init_event()
#
#     def init_root(self):
#         self.root = tk.Tk()
#         self.root.title("My draw")
#
#     def init_status(self):
#         self.status = tk.Label(self.root, text="请选择你要绘制的图形。")
#         self.status.pack(side="left")
#
#     def init_canvas(self):
#         self.canvas = tk.Canvas(self.root, width=500, height=300, )
#         self.canvas.pack()
#
#     def init_event(self):
#         self.canvas.bind("<Button-1>", self.on_press)
#         self.canvas.bind("<B1-Motion>", self.on_drag)
#         self.canvas.bind("<ButtonRelease-3>", self.on_press_3)
#
#     def init_menu(self):
#         self.menu_bar = tk.Menu(self.root)
#
#         self.draw_menu = tk.Menu(self.menu_bar, tearoff=0)
#         self.draw_menu.add_command(label="矩形", command=lambda: self.change_current_shape("矩形"))  # 添加“矩形”选项
#         self.draw_menu.add_command(label="圆形", command=lambda: self.change_current_shape("圆形"))  # 添加“圆形”选项
#         self.menu_bar.add_cascade(label="绘图", menu=self.draw_menu)
#
#         self.colour_menu = tk.Menu(self.menu_bar, tearoff=0)
#         self.colour_menu.add_command(label="紫色", command=self.set_color)
#         self.colour_menu.add_separator()
#         self.colour_menu.add_command(label="自定义", command=self.select_color)
#         self.menu_bar.add_cascade(label="颜色", menu=self.colour_menu)
#
#         self.other_menu = tk.Menu(self.menu_bar, tearoff=0)
#         self.other_menu.add_command(label="清除", command=self.other_clear)
#         self.other_menu.add_command(label="撤销", command=self.other_undo)
#         self.other_menu.add_command(label="退出软件", command=self.other_exit)
#         self.menu_bar.add_cascade(label="其他", menu=self.other_menu)
#
#         # self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
#         # self.file_menu.add_command(label="保存图片", command=self.save_image)
#         # # self.file_menu.add_command(label="撤销", command=self.other_undo)
#         # # self.file_menu.add_command(label="退出软件", command=self.other_exit)
#         # self.menu_bar.add_cascade(label="文件", menu=self.file_menu)
#
#         self.root.config(menu=self.menu_bar)
#
#         # 创建一个空白图像
#
#         # 使用PIL库将PostScript文件转换为PNG格式的图片
#         # img = Image.open("D:\\python2401\\python基础语法\\canvas_image.ps")
#         # img.save("D:\\python2401\\python基础语法\\canvas_image.png")
#         # self.image = PIL.Image.new("RGB", (300, 200), "white")
#         # self.draw = PIL.ImageDraw.Draw(self.image)
#         #
#         # # 从画布中获取内容并绘制到图像上
#         # x0, y0, x1, y1 = self.canvas.bbox("all")
#         # self.image.paste(self.canvas.postscript(colormode="color"), (int(x0), int(y0)))
#         #
#         # # 保存图像文件
#         # self.image.save("canvas_content.png", "PNG")
#
#     def set_color(self):
#         self.current_color = "purple"
#
#     def select_color(self):
#         color = colorchooser.askcolor()
#         if color[1]:
#             self.current_color = color[1]
#
#     def other_clear(self):
#         self.canvas.delete("all")
#         self.max_id = 0
#
#     def other_undo(self):
#         if self.max_id >= 1:
#             self.canvas.delete(self.max_id)
#             self.max_id -= 1
#         elif self.max_id == 0:
#             my_font = font.Font(size=16)
#             popup = tk.Toplevel(self.root, )
#             popup.title("警告！")
#             # 创建一个自定义字体
#             # 创建一个Label来显示文本，并使用自定义字体
#             label = tk.Label(popup, text="当前没有可以撤销的图形。", font=my_font)
#             label.pack(pady=20)
#
#             # 设置弹窗的大小和位置
#             popup.geometry("300x100+200+200")
#             # messagebox._show("提示", "这是一个具有自定义字体大小的消息框！", messagebox.INFO, "info", font=my_font)
#             # messagebox.showinfo("警告", "当前没有可以撤销的图形。", font=my_font)
#             # message_label = tk.Label(self.root, text="这是一个具有自定义字体大小的消息框！", font=my_font)
#             # message_label.pack(pady=20)
#
#     def other_exit(self):
#         self.canvas.quit()
#
#     def change_current_shape(self, shape):
#         self.str_current_shape = shape
#         self.status.config(text="正在绘制:" + self.str_current_shape)
#
#     def on_press(self, event):
#         self.start_x = event.x
#         self.start_y = event.y
#         if self.str_current_shape == "矩形":
#             self.max_id = self.canvas.create_rectangle(event.x, event.y,
#                                                        event.x, event.y, outline=self.current_color)
#         elif self.str_current_shape == "圆形":
#             self.max_id = self.canvas.create_oval(event.x, event.y,
#                                                   event.x, event.y, outline=self.current_color)
#
#     def on_drag(self, event):
#         if self.str_current_shape:
#             self.canvas.coords(self.max_id, self.start_x, self.start_y,
#                                event.x, event.y)
#
#     def on_press_3(self, ):
#         self.str_current_shape = ""
#         self.status.config(text="请选择你要绘制的图形。" + self.str_current_shape)
#
#     def run(self):
#         self.root.mainloop()
#
#
# d = Draw_Gui()
# d.run()

# 二、根据自己理解解释以下概念，文字总结
# 面向过程
# 就是第一步干什么，第二步干什么
# 面向对象
# 就是他会干什么什么什么，有什么什么 ，他会干什么什么什么，有什么什么
# 类
# class People:
#     pass
#
#
# class Dog:
#     # 类属性
#     species = "mammal"
#
#     # 类属性就是你定义实例时所有实例都会有。
#     def __init__(self, name, age):
#         # 实例属性
#         self.name = name
#         self.age = age
#
#
# # 创建两个Dog类的实例
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Molly", 5)
#
# # 访问类属性
# print(Dog.species)  # 输出: mammal
#
# # 访问实例属性
# print(dog1.name, dog1.age)  # 输出: Buddy 3
# print(dog2.name, dog2.age)  # 输出: Molly 5
#
# p1 = People()
# print(p1)
#

# 就是一个 类，一类东西的类，物以类聚，人以群分的类
# 实例
# 就是一类中的一个具体的实例
# 初始化方法
# 就是在你条用这个类时就会去自动执行的方法
# 魔法方法 就是在你干某些事情时就会去自动执行，不需要自己调用
# 字符串方法 是一种魔法方法，在print对象时调用
# self 就是即将要出生的一个对象
# 数据、属性、操作、行为 数据就是属性，操作就是行为
# 父类、基类、超类 父类就是超类，可以派生出子类
# 子类、派生类 一样的，可以继承父类的所有
# 多态
# python没有多态
# python到处都是多态
# 重载多态
# 重写多态


# 三、使用面向对象编写图书管理
# 类：学生（学号，姓名，邮箱，手机号）
# 类：图书（图书编号， 书名， 作者， 出版日期， 当前状态（是否可接））

# 类：管理类
# 图书列表、学生列表、借阅列表
# 添加学生，移除学生
# 添加图书，移除图书
# 借书，还书
# 展示所有借阅记录
# #
# # 添加测试实例，对以上系统进行测试
# from datetime import datetime


# class Student:
#     def __init__(self, stu_id, name, mile, phone):
#         self.phone = phone
#         self.mile = mile
#         self.name = name
#         self.stu_id = stu_id
#
#     def __str__(self) -> str:
#         return f"学生id:{self.stu_id}\t学生姓名:{self.name}\t学生邮箱号:{self.mile}\t学生手机号:{self.phone}"
#
#
# class Book:
#     def __init__(self, book_id, name, author, publish_date, is_loan):
#         # 归还日期(未归还则为空)
#         self.name = name
#         self.is_loan = is_loan
#         self.publish_date = publish_date
#         self.author = author
#         self.book_id = book_id
#
#     def __str__(self):
#         return f"图书id:{self.book_id}\t图书姓名:{self.name}\t" \
#                f"图书作者:{self.author}\t图书的出版日期:{self.publish_date}\t" \
#                f"是否可以租借：{self.is_loan}"
#
#
# class Loan_Record:
#     def __init__(self, loan_id, stu_id, book_id, loan_date, back) -> None:
#         self.back = back
#         self.loan_date = loan_date
#         self.book_id = book_id
#         self.stu_id = stu_id
#         self.loan_id = loan_id
#
#
# class Student_Manage:
#     def __new__(cls, *args, **kwargs):
#         if hasattr(cls, "self"):
#             return cls.self
#         else:
#             self = object.__new__(cls)
#             cls.self = self
#             return self
#
#     def __init__(self):
#         self.students = []
#
#
#     @staticmethod
#     def input_three_items():
#         while 1:
#             tem_na = input("输入名字,长度为2或者3：")
#             if len(tem_na) > 3 or len(tem_na) < 2:
#                 print("名字不合法！")
#             else:
#                 break
#         while 1:
#             tem_mi = input("输入邮箱：")
#             if "@" not in tem_mi:
#                 print("邮箱格式不合法！")
#             else:
#                 break
#         while 1:
#             tem_ph = input("输入手机号：")
#             if len(tem_ph) < 5:
#                 print("手机号格式不合法！")
#             else:
#                 break
#         return tem_na, tem_mi, tem_ph
#
#     def add_student(self):
#         base_information = Student_Manage.input_three_items()
#         new_student = Student(101 if len(self.students) == 0
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
#     def isexist_student(self, student_id: int = 0):
#         """
#         如果不传参，则判断的是是否有学生。
#         如果传入参数，就是判断指定的学生是否存在。
#         :param student_id:
#         :return:
#         """
#         if student_id == 0:
#             if len(self.students) == 0:
#                 print("该学生管理系统中还未有学生。")
#                 return False
#             else:
#                 return True
#         else:
#             for stu in self.students:
#                 if stu.stu_id == student_id:
#                     return True
#             print(f"未找到id为{student_id}的学生！")
#             return False
#
#     def delect_student(self, stu_id):
#         if self.isexist_student(stu_id):
#             for stu in self.students:
#                 if stu.stu_id == stu_id:
#                     self.students.remove(stu)
#                     return
#
#
# class Book_Manage(object):
#     def __del__(self):
#         pass
#
#     def __init__(self):
#         self.books: list[Book] = []
#
#     @staticmethod
#     def input_four_items():
#         while 1:
#             tem_na: str = input("输入图书名字,长度为2或者3：")
#             if len(tem_na) > 3 or len(tem_na) < 2:
#                 print("名字不合法！")
#             else:
#                 break
#         while 1:
#             tem_author = input("输入作者：")
#             break
#         tem_public_date = datetime.strptime(input("请输入出版时间日期："), "%Y-%m-%d")
#
#         tem_is_loan: bool = bool(input("该书现在是否可借："))
#
#         return tem_na, tem_author, tem_public_date, tem_is_loan
#
#     def add_book(self):
#         base_information = Book_Manage.input_four_items()
#         new_book = Book(1001 if len(self.books) == 0
#                         else 1 + self.books[-1].book_id,
#                         base_information[0],
#                         base_information[1],
#                         base_information[2],
#                         base_information[2])
#         # noinspection PyTypeChecke
#         self.books.append(new_book)
#         for st in self.books:
#             print(st)
#         print("添加成功！")
#
#     def isexist_book(self, book_id=0):
#         """
#         :return:
#         """
#         if book_id == 0:
#             if len(self.books) == 0:
#                 print("还未有book。")
#                 return False
#             else:
#                 return True
#         else:
#             for stu in self.books:
#                 if stu.book_id == book_id:
#                     return True
#             print(f"未找到id为{book_id}的图书！")
#             return False
#
#     def delect_book(self, book_id) -> None:
#         if self.isexist_book(book_id):
#             for stu in self.books:
#                 if stu.book_id == book_id:
#                     self.books.remove(stu)
#                     return
#
#
# class Loan_Manage:
#     def __init__(self, bm: Book_Manage, sm: Student_Manage):
#         self.sm = sm
#         self.bm = bm
#         self.loans: list[Loan_Record] = []
#
#     def __del__(self):
#         pass
#
#     def isexist_loan_sid_bid(self, book_id, stu_id):
#         for loan in self.loans:
#             if loan.stu_id == stu_id and loan.book_id == book_id:
#                 print("该学生已经借阅了这本书")
#                 return True
#         else:
#             return False
#
#     def add_loan(self):
#         # 添加一条借走书的记录。
#         # loan_id, stu_id, book_id, loan_date, is_back
#         book_id = int(input("请输入图书的id："))
#         stu_id = int(input("请输入学生的id："))
#         if self.sm.isexist_student(stu_id) and self.bm.isexist_book(book_id):
#             if self.isexist_loan_sid_bid(book_id, stu_id):
#                 pass
#             else:
#                 loan_date = datetime.today()
#                 is_back = False
#                 self.loans.append(Loan_Record(1 + self.loans[-1].loan_id
#                                               if len(self.loans) != 0 else 10001,
#                                               stu_id, book_id, loan_date, is_back))
#                 print("添加成功！")
#
#     def isexist_book(self, book_id=0):
#         """
#         :return:
#         """
#         if 0 == book_id:
#             if len(self.bm.books) == 0:
#                 print("还未有book。")
#                 return False
#             else:
#                 return True
#         else:
#             for stu in self.bm.books:
#                 if book_id == stu.book_id:
#                     return True
#             print(f"未找到id为{book_id}的图书！")
#             return False
#
#     def give_back_book(self, ):
#         book_id = int(input("请输入图书的id："))
#         stu_id = int(input("请输入学生的id："))
#         if self.sm.isexist_student(stu_id) and self.bm.isexist_book(book_id):
#             if not self.isexist_loan_sid_bid(book_id, stu_id):
#                 print("该学生没有借该书。")
#                 pass
#             else:
#                 back_date = datetime.today()
#                 self.loans.(Loan_Record(1 + self.loans[-1].loan_id
#                                         if len(self.loans) != 0 else 10001,
#                                         stu_id, book_id, loan_date, is_back))
#                 print("添加成功！")
#
# #
# 在面向对象编程中，单例模式是一种创建只能有一个实例的类
# 的设计模式。在 Python 中，可以通过以下几种方式来实现单例类：
#
# 使用模块级别的变量：在 Python 中，
#
#
# 模块是天然的单例
#
#
# 因为模块只会被导入一次。你可以将需要单例的类定义在一个模块中，并在其他地方导入使用。
# python
# # singleton.py
# class SingletonClass:
#     def __init__(self):
#         pass
#
# singleton_instance = SingletonClass()

# # main.py
# from singleton import singleton_instance

# # 使用 singleton_instance 进行操作


# 使用装饰器：你可以编写一个装饰器函数，用于将类转换为单例。
# 装饰器可以在实例化类时检查是否已经存在实例，如果存在则返回现有实例，如果不存在则创建新实例。
# python
# def singleton(cls):
#     instances = {}
#
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = object.__new__(cls)
#             # instances[cls] = cls(*args, **kwargs)
#         print(id(instances[cls]))
#         return instances[cls]
#
#     return wrapper

def singleton(cls):
    instances = None

    def wrapper(*args, **kwargs):
        nonlocal instances
        if instances is None:
            instances = object.__new__(cls)
            # instances[cls] = cls(*args, **kwargs)
        print(id(instances))
        return instances

    return wrapper


@singleton
class SingletonClass:
    def __init__(self):
        pass


s1 = SingletonClass()
s2 = SingletonClass()
# # 使用 SingletonClass() 实例化
# 使用元类（metaclass）：元类是用于创建类的类，可以通过自定义元类来实现单例模式。通过重写元类的 __call__ 方法，在实例化类时检查是否已经存在实例。
# python
# class SingletonMeta(type):
#     instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls.instances:
#             cls.instances[cls] = super().__call__(*args, **kwargs)
#         return cls.instances[cls]
#
# class SingletonClass(metaclass=SingletonMeta):
#     def __init__(self):
#         pass
#
# # 使用 SingletonClass() 实例化
# 无论你选择哪种方式，单例模式都可以确保只有一个实例存在，并提供对该实例的全局访问点。但需要注意的是，单例模式可能会对代码的可测试性和可扩展性产生一定的影响，因此在使用时需要慎重考虑。
#
# 希望以上信息对你有所帮助！如果还有其他问题，请随时提问。
