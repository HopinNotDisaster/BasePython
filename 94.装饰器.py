"""
闭包：
1.外部函数嵌套内部函数
2.外部函数把内部函数返回！ 外部函数不是执行内部函数！
3.内部函数可以访问保存外部函数的局部变量！
"""
import time


# def decorator(f):
#     def check():
#         print("已经")
#         f()
#
#     return check

def time_cost(f):
    def calc():
        print(time.time())
        f()
        print(time.time())

    return calc


def login_check(f):
    def calc():
        name = input("0.0:")
        if name == "111":
            f()
        else:
            print("name输入错误！")

    return calc


@login_check
@time_cost
def center():
    print("个人中心！")


@login_check
@time_cost
def cart():
    print("购物车！")


center()
cart()
"""
装饰器的本质是闭包+语法糖
在被装饰的函数上方使用@来装饰函数的名字！
作用：不改变原函数的内容，给函数添加新功能！
满足开闭限制：面向 扩展开放！面向 修改关闭！
"""
