# # 浮点数  小数点  科学计数法
# f0 = 3.14
# print(type(f0))
# f1 = .34
# print (type(f1))
# # 若小数点前省略，省略的是0
# # 小数点后省略，代表此数据为浮点数。
# f3 = 314e87
# print(f3 , type (f3))
# f4 = 314e-2
# print(f4 , type (f4))
#
# # 整数
# i0 = 100
# print(i0 ,type(i0))
#
# # 二进制表示整数  只能出现0和1
#
# i1 = 0b10110
# print(i1 ,type (i1))
#
# # \\192.168.10.55\
# # ip:有四部分组成，每一位都是0-255（8位的2进制）
# # 端口： 0-65535
# i4=0b1111111111111111
# print(i4)
#
# # 16进制 可以出现0 1 2 3 4 5 6 7 8 9 A B C D E F
# i5= 0x1135AF
# print(i5)
#
# # 十六进制常表示颜色
#
# # 八进制
# # 逢八进一 只能出现0-7
# i6=0o77
# print(i6)
#
# # 从右侧起，第n个数m的值是m*10的（n-1）次方
#
#
#
# 编写登录 注册模块
#
# 0.退出
#
# 1.登录
#
# 2.注册
#
#
#
# 登录 可以检测用户名密码是否正确
#
# 注册可以检测用户名是否存在， 密码是否一致
#


datas = [
    {
        "id": 101,
        "name": "abc",
        "pwd": "123456"
    }
]


def login():
    name = input("请输入用户名: ")
    pwd = input("请输入密码: ")

    for data in datas:
        if data["name"] == name and data["pwd"] == pwd:
            print("登录成功！")
            return
    else:
        print("用户名或密码错误！")


def enroll():
    name = input("请输入用户名: ")
    pwd1 = input("请输入密码: ")
    pwd2 = input("请再次输入密码: ")

    for data in datas:
        if data["name"] == name:
            print("用户名已存在！")
            return

    if pwd1 != pwd2:
        print("两次输入的密码不一样")
        return

    data = {
        "id": datas[-1]["id"] + 1,
        "name": name,
        "pwd": pwd1
    }
    datas.append(data)
    print("注册成功！")


info = """
0.退出
1.登录
2.注册
"""


def main():
    print(info)
    sel = int(input("请输入你的选择："))
    if sel == 0:
        return
    elif sel == 1:
        login()
    elif sel == 2:
        enroll()


main()
