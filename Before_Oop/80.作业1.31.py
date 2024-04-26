# 使用函数封装完成以下题目
# CSDN编写博客，python类相关术语附带案例
# 面向对象
# 类

# 实例

# 初始化方法

# 魔法方法

# 字符串方法

# self

# 数据、属性、操作、行为

# 父类、基类、超类

# 子类、派生类

# 多态

# python没有多态

# python到处都是多态

# 重载多态

# 重写多态

# 实例属性

# 实例方法

# 类属性

# 类方法

# 静态方法

# 一、编写案例附加注释

# 初始化函数

# 析构函数

# 单例类的使用

# 二、编写案例附加注释

# 类属性

# 静态方法

# 类方法

# 实例属性

# 实例方法

# 三、编写案例附加注释

# Hasattr、setattr、getattr、delattr

# 分别操作类与实例

# 四、编写案例附加注释

# 普通成员、私有成员、保护成员

# 五、使用面向对象编写图书管理

# 类：学生（学号，姓名，邮箱，手机号）
# 类：图书（图书编号， 书名， 作者， 出版日期， 当前状态（是否可接））
# 类：借阅（记录id， 学生，图书，借阅日期，归还日期(未归还则为空)）
# 类：管理类
# 图书列表、学生列表、借阅列表
# 添加学生，移除学生
# 添加图书，移除图书
# 借书，还书
# 展示所有借阅记录
# 添加测试实例，对以上系统进行测试
from datetime import datetime


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


class Show:
    def __new__(cls):
        if hasattr(cls, "self"):
            return cls.self
        else:
            self = object.__new__(cls)
            return self

    def __init__(self):
        self.interface = """
        0.退出图书管理系统
        1.显示所有的学生信息
        2.显示所有的图书信息
        3.显示所有的借阅信息
        4.添加学生
        5.添加图书
        6.借书
        7.还书
        """

    def print_interface(self):
        print(self.interface)


class Student:
    def __init__(self, stu_id, name, mile, phone):
        self.phone = phone
        self.mile = mile
        self.name = name
        self.stu_id = stu_id

    def __str__(self) -> str:
        return f"学生id:{self.stu_id}\t学生姓名:{self.name}\t学生邮箱号:{self.mile}\t学生手机号:{self.phone}"


class Book:
    def __init__(self, book_id, name, author, publish_date, is_loan):
        self.name = name
        self.is_loan = is_loan  # 是否可以借阅！！！！
        self.publish_date = publish_date
        self.author = author
        self.book_id = book_id

    def __str__(self):
        return f"图书id:{self.book_id}\t图书姓名:{self.name}\t" \
               f"图书作者:{self.author}\t图书的出版日期:{self.publish_date}\t" \
               f"是否可以租借：{self.is_loan}"


class Loan:
    def __init__(self, loan_id, stu_id, book_id, loan_date, back_date) -> None:
        self.back_date = back_date
        self.loan_date = loan_date
        self.book_id = book_id
        self.stu_id = stu_id
        self.loan_id = loan_id

    def __str__(self):
        return f"借阅编号：{self.loan_id}\tid为{self.stu_id}的学生" \
               f"借阅了id为{self.book_id}的书。借阅时间为{self.loan_date}," \
               f"归还时间为{self.back_date}"


@singleton
class Student_Manage:
    def __new__(cls, *args, **kwargs):
        if hasattr(cls, "self"):
            return cls.self
        else:
            self = object.__new__(cls)
            cls.self = self
            return self

    def __init__(self):
        self.students = [
            Student(101, "我我我", "3315813594@qq.com", "13663900687"),
            Student(102, "jjj", "121@", "1233543"),
            Student(103, "kkk", "1353@", "5464686"),
        ]

    def show_all_students_1(self):
        if len(self.students) != 0:
            for stu in self.students:
                print(stu)
        else:
            print("暂无学生！")

    @staticmethod
    def input_three_items():
        while 1:
            tem_na = input("输入名字,长度为2或者3：")
            if len(tem_na) > 3 or len(tem_na) < 2:
                print("名字不合法！")
            else:
                break
        while 1:
            tem_mi = input("输入邮箱：")
            if "@" not in tem_mi:
                print("邮箱格式不合法！")
            else:
                break
        while 1:
            tem_ph = input("输入手机号：")
            if len(tem_ph) < 5:
                print("手机号格式不合法！")
            else:
                break
        return tem_na, tem_mi, tem_ph

    def add_student_4(self):
        base_information = self.input_three_items()
        new_student = Student(101 if len(self.students) == 0
                              else 1 + self.students[-1].stu_id,
                              base_information[0],
                              base_information[1],
                              base_information[2])
        # noinspection PyTypeChecke
        self.students.append(new_student)
        for st in self.students:
            print(st)
        print("添加成功！")

    def isexist_student(self, student_id: int = 0):
        """
        如果不传参，则判断的是是否有学生。
        如果传入参数，就是判断指定的学生是否存在。
        :param student_id:
        :return:
        """
        if student_id == 0:
            if len(self.students) == 0:
                print("该学生管理系统中还未有学生。")
                return False
            else:
                return True
        else:
            for stu in self.students:
                if stu.stu_id == student_id:
                    return True
            print(f"未找到id为{student_id}的学生！")
            return False

    def delect_student(self, stu_id):
        if self.isexist_student(stu_id):
            for stu in self.students:
                if stu.stu_id == stu_id:
                    self.students.remove(stu)
                    return


@singleton
class Book_Manage(object):
    def __del__(self):
        pass

    def __init__(self):
        self.books: list[Book] = [
            Book(1001, "一本好书", "呼哈", "2020-08-13", False),
            Book(1002, "啦啦啦", "牡蛎牡蛎", "2021-01-12", True),
        ]

    def book_id_is_loan(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book.is_loan

    @staticmethod
    def input_four_items():
        while 1:
            tem_na: str = input("输入图书名字,长度为2或者3：")
            if len(tem_na) > 3 or len(tem_na) < 2:
                print("名字不合法！")
            else:
                break
        while 1:
            tem_author = input("输入作者：")
            break
        tem_public_date = datetime.strptime(input("请输入出版时间日期："), "%Y-%m-%d")

        tem_is_loan: bool = bool(input("该书现在是否可借："))

        return tem_na, tem_author, tem_public_date, tem_is_loan

    def add_book_5(self):
        base_information = self.input_four_items()
        new_book = Book(1001 if len(self.books) == 0
                        else 1 + self.books[-1].book_id,
                        base_information[0],
                        base_information[1],
                        base_information[2],
                        base_information[2])
        # noinspection PyTypeChecke
        self.books.append(new_book)
        for book in self.books:
            print(book)
        print("添加成功！")

    def isexist_book(self, book_id=0):
        """
        :return:
        """
        if book_id == 0:
            if len(self.books) == 0:
                print("还未有book。")
                return False
            else:
                return True
        else:
            for stu in self.books:
                if stu.book_id == book_id:
                    return True
            print(f"未找到id为{book_id}的图书！")
            return False

    def delect_book(self, book_id) -> None:
        if self.isexist_book(book_id):
            for stu in self.books:
                if stu.book_id == book_id:
                    self.books.remove(stu)
                    return

    def show_all_books_2(self):
        if len(self.books) != 0:
            for book in self.books:
                print(book)
        else:
            print("暂无学生！")


@singleton
class Loan_Manage:
    def __new__(cls, *args, **kwargs):
        if hasattr(cls, "obj"):
            return cls.obj
        else:
            obj = object.__new__(cls)
            setattr(cls, "obj", obj)
            return obj

    def __init__(self, bm: Book_Manage, sm: Student_Manage):
        self.sm = sm
        self.bm = bm
        self.loans: list[Loan] = [
            Loan(10001, 101, 1001, "2021-09-10", False)
        ]

    def __del__(self):
        pass

    def update_loan_back(self):
        book_id = int(input("请输入你要归还图书的id："))
        stu_id = int(input("请输入归还者学生的id："))
        if self.isback_loan_sid_bid(book_id, stu_id):
            print("已经归还！！")
        else:
            # 先把loan改了。
            back_date = datetime.today()
            print(back_date, type(back_date))
            for i in range(len(self.loans)):
                if self.loans[i].stu_id == stu_id and self.loans[i].book_id == book_id:
                    self.loans[i] = Loan(self.loans[i].loan_id,
                                         stu_id, book_id, self.loans[i].loan_date, back_date)
                    break
            for loan in self.loans:
                print(loan)
            return book_id

    def back_book_7(self):
        book_id = self.update_loan_back()
        self.update_book_is_loan(book_id, True)

    def update_book_is_loan(self, book_id, is_loan_book):
        """
        但凡进入这个函数，book_id一定存在并且这本书的is_loan一定是False！！！！！
        :param is_loan_book:
        :param book_id:
        :return:
        """
        if self.bm.isexist_book(book_id):
            for book in self.bm.books:
                if book.book_id == book_id:
                    book.is_loan = is_loan_book
                    print("该书借阅\\归还成功！")
                    return

    def loan_book_6(self):
        book_id = self.add_loan()  # 在self.loans中添加一条新的记录 ，并且返回书的id
        if book_id == 0:
            pass
        else:
            self.update_book_is_loan(book_id, False)

    def show_all_loans_3(self):
        if len(self.loans) != 0:
            for loan in self.loans:
                print(loan)
        else:
            print("暂无借阅记录！")

    def isback_loan_sid_bid(self, book_id, stu_id):
        for loan in self.loans:
            if loan.stu_id == stu_id and loan.book_id == book_id:
                print("有该学生借阅该本书的记录！")
                return bool(loan.back_date)
        else:
            print("没有该学生与这本书的相关记录！")
            return False

    def add_loan(self) -> int:
        # 添加一条借走书的记录。
        # loan_id, stu_id, book_id, loan_date, is_back
        book_id = int(input("请输入你要借阅图书的id："))
        stu_id = int(input("请输入借阅者学生的id："))
        if self.sm.isexist_student(stu_id) and self.bm.isexist_book(book_id):
            if not self.bm.book_id_is_loan(book_id):
                print("有学生已经借过这本书了！")
                return 0
            else:
                loan_date = datetime.today()
                print(loan_date, type(loan_date))
                is_back = False
                self.loans.append(Loan(1 + self.loans[-1].loan_id
                                       if len(self.loans) != 0 else 10001,
                                       stu_id, book_id, loan_date, is_back))
                print("添加成功！")
                for loan in self.loans:
                    print(loan)
                return book_id
        else:
            return 0

    def isexist_book(self, book_id=0):
        """
        :return:
        """
        if 0 == book_id:
            if len(self.bm.books) == 0:
                print("还未有book。")
                return False
            else:
                return True
        else:
            for stu in self.bm.books:
                if book_id == stu.book_id:
                    return True
            print(f"未找到id为{book_id}的图书！")
            return False

    # def give_back_book(self, ):
    #     book_id = int(input("请输入图书的id："))
    #     stu_id = int(input("请输入学生的id："))
    #     if self.sm.isexist_student(stu_id) and self.bm.isexist_book(book_id):
    #         if not self.isexist_loan_sid_bid(book_id, stu_id):
    #             print("该学生没有借该书。")
    #             pass
    #         else:
    #             back_date = datetime.today()
    #             self.loans.(Loan_Record(1 + self.loans[-1].loan_id
    #                                     if len(self.loans) != 0 else 10001,
    #                                     stu_id, book_id, loan_date, is_back))
    #             print("添加成功！")


@singleton
class Books_Management_System:
    def __new__(cls, *args, **kwargs):
        if hasattr(cls, "obj"):
            return cls.obj
        else:
            obj = object.__new__(cls)
            setattr(cls, "obj", obj)
            return obj

    def __init__(self, sm, bm, lm):
        self.sm: Student_Manage = sm
        self.bm: Book_Manage = bm
        self.lm: Loan_Manage = lm

    @staticmethod
    def check_interface_option() -> tuple:
        option = int(input("尊敬的用户请进行你的选择:"))
        if option in [i for i in range(0, 8)]:
            return True, option
        else:
            print("输入内容不合法！请重新输入！")
            return False, None


def main():
    sm = Student_Manage()
    while 1:
        bm = Book_Manage()
        lm = Loan_Manage(bm, sm)
        bms = Books_Management_System(sm, bm, lm)
        show = Show()
        show.print_interface()
        option = bms.check_interface_option()
        if option[0]:
            if option[1] == 0:
                exit()
            elif option[1] == 1:
                # 1.显示所有的学生信息
                bms.sm.show_all_students_1()
            elif option[1] == 2:
                # 2.显示所有的图书信息
                bms.bm.show_all_books_2()
            elif option[1] == 3:
                # 3.显示所有的借阅信息
                bms.lm.show_all_loans_3()
            elif option[1] == 4:
                # 4. 添加学生
                bms.sm.add_student_4()
            elif option[1] == 5:
                # 5. 添加图书
                bms.bm.add_book_5()
            elif option[1] == 6:
                # 6. 借书
                bms.lm.loan_book_6()
            elif option[1] == 7:
                bms.lm.back_book_7()
                # 7.还书
                pass
        else:
            print("您的输入不合法，请再输入一次吧！")


# main()
# 六、自学pygame模块基础使用
"""
需求：
1.坦克类
    1.1我方坦克类
    1.2敌方坦克类
    坦克显示
    坦克移动
    坦克射击
2.子弹类
    显示子弹
    子弹移动
3.墙壁类
    显示墙壁
4.爆炸效果类
    显示爆炸效果
5.音效类
    背景音乐
6.游戏主窗口
    开始游戏
    结束游戏
"""


class Tank:
    def __init__(self):
        pass

    def display_tank(self):
        pass


import sys
import pygame


def get_text_surface(str_text: str) -> pygame.Surface:
    pygame.font.init()
    font = pygame.font.SysFont("kaiti", 20)  # 定义一个字体！
    return font.render(str_text, True, TEXT_COLOR)


def get_event() -> None:
    for event in pygame.event.get():
        if event.type == 256:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print("按下键盘！")


pygame.init()

TEXT_COLOR = pygame.Color(0, 0, 25)

icon = pygame.image.load("syq.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("坦克大战1.0")

screen = pygame.display.set_mode((1080, 640))
screen.fill("azure")  # azure 天蓝色

# print(pygame.font.get_fonts())
while 1:
    get_event()
    screen.blit(get_text_surface(f"敌方坦克数量还剩余：  辆。"), (0, 0))
    pygame.display.flip()
