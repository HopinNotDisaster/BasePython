# # 一、封装函数求1+2+3+...+100的和
# def fun1(n):
#     return sum(range(n + 1))
#
#
# print(fun1(100))

# # 二、封装函数包含两个形参start与end 返回start到end之间奇数的和
# def fun2(start, end):
#     if start % 2 == 0:
#         return sum(range(start + 1, end + 1, 2))
#     else:
#         return sum(range(start, end + 1, 2))
#
#
# print(fun2(2, 10))  # 3 5 7 9

# # 三、封装函数：可以判断一个数是否是质数
def fun3(x):
    """
    判断x是否为质数
    :param x:
    :return:
    """
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


#
#
# print(fun3(5))

# 四、封装函数：求1000以内的质数对
# def fun4(n):
#     """
#     返回一个列表，里面包含1000以内的所有质数
#     :param n:
#     :return:
#     """
#     ret = []
#     for i in range(2, n):
#         if fun3(i):
#             ret.append(i)
#     return ret


# print(fun4(50))

# 五、编写函数求start到end以内所有的相差为step的素数对
def fun5(start, end, step):
    """
    :param end:
    :param start:
    :param step:
    :return:
    """
    ans = []
    for i in range(start, end):
        if fun3(i) and fun3(i + step):
            ans.append([i, i + step])
    return ans


# print(fun5(2, 100, 4))

# 六、编写函数返回斐波那契数列的第n个数
# 斐波那契数列指的是这样一个数列：1，1，2，3，5，8，13，21，34，55，89...
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#

# print(fibonacci(7))

# 七、编写一个函数，接受一个数字n作为参数，该函数可以随机生成n个整数，并返回	所有整数的最大值
# import random

#
# def fun7(n):
#     ret = random.randint(0, 9)
#     for i in range(n - 1):
#         tem = random.randint(0, 9)
#         ret = ret if ret >= tem else tem
#     return ret


# print(fun7(5))

# 八、编写一个 Python 函数，接受一个字符串作为参数，并返回该字符串中所有大写字母的数量

def fun8_1(s):
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    return count


# print(fun8_1("ASFTGsdfgdsfgSDGSDG"))


# 编写函数，接受一个字符串和一个字符作为参数，并返回该字符串中该字符出现的次数。
def fun8_2(s, c):
    count = 0
    for i in s:
        if i == c:
            count += 1
    return count


# print(fun8_2("sdfggfsdds", "g"))

# 九、编写学生管理系统Z:\share\python2401\第一阶段\60学生管理.exe 完整版

datas = {
    'students': [
        {"ID": 101, "Name": 12, "Age": 18, "Sex": "男"}
    ],
    'course': [{"id": 1001, "name": "math"}
               ],
    'score': [],
    'user': [
        {'id': 11, 'name': 'aa', 'pwd': '123456'},
        {'id': 12, 'name': 'bb', 'pwd': '111222'}
    ]
}
user_id = 13
student_id = 102
course_id = 1002


def course():
    global course_id
    if n == 6:  # 添加课程
        while 1:
            tem_na = input("输入课程的名字,长度为2或者3：")
            if len(tem_na) > 3 or len(tem_na) < 2:
                print("名字不合法！")
            else:
                break
        datas["course"].append({"id": course_id, "name": tem_na})
        course_id += 1
        print("添加课程完成！")
    elif n == 7:  # 删除课程
        delete_id = int(input("输入要删除课程的ID："))
        for di in datas["course"]:
            if di["id"] == delete_id:
                datas["course"].remove(di)
                print("删除课程完成！")
        print("未查到此课程，删除课程失败！")
    elif n == 8:  # 修改课程
        modified_id = int(input("输入需要修改课程的id"))
        for di in datas["course"]:
            if di["id"] == modified_id:
                while 1:
                    tem_na = input("输入新名字,长度为2或者3：")
                    if len(tem_na) > 3 or len(tem_na) < 2:
                        print("名字不合法！")
                    else:
                        break
                di.update({"name": tem_na})
                print("修改完成！")
                break
        else:
            print("查找课程失败，无法修改！")
    # 下面是查看指定课程id信息
    elif n == 9:
        looked_id = int(input("输入需要查看课程的id"))
        for di in datas["course"]:
            if di["id"] == looked_id:
                print(di)
                break
        else:
            print("查找失败！")

    elif n == 10:
        print(datas["course"])


def enroll():
    global user_id
    # 注册成功[{'id': 11, 'name': 'ab', 'pwd': '123456'}]
    tem_name = input("输入你的名字：")
    tem_pwd = input("输入你的密码：")
    datas["user"].append({"id": user_id, "name": tem_name, "pwd": tem_pwd})
    user_id += 1
    print("注册成功")


def login():
    tem_name = input("输入你的用户名：")
    tem_pwd = input("输入你的密码：")
    for u in datas["user"]:
        if u["name"] == tem_name and u["pwd"] == tem_pwd:
            print("登陆成功！")
            print("**********欢迎来到用户界面！**********", end="")
            return True
    else:
        print("用户名或者密码错误！")
        return False


def add_student():
    global student_id
    while 1:
        tem_na = input("输入名字,长度为2或者3：")
        if len(tem_na) > 3 or len(tem_na) < 2:
            print("名字不合法！")
        else:
            break
    while 1:
        tem_se = input("输入性别，男或者女：")
        if tem_se != '男' and tem_se != '女':
            print("性别不合法！")
        else:
            break
    while 1:
        tem_ag = int(input("输入年龄，15-25之间："))
        if tem_ag >= 25 or tem_ag <= 15:
            print("年龄不合法！")
        else:
            break
    # noinspection PyTypeChecker
    datas['students'].append({"ID": int(student_id),
                              "Name": tem_na,
                              "Age": tem_ag,
                              "Sex": tem_se})
    student_id += 1
    print("添加成功！")

    # noinspection PyTypeChecke


def delete_student(student_id: int):
    """

    :type student_id: int
    """
    for di in datas["students"]:
        if di["ID"] == student_id:
            datas["students"].remove(di)
            return True
    return False


def view():
    for st in datas["students"]:
        print(st)
        print("所有学生信息显示完毕！")


inf2 = """
0. 退出程序
1. 添加学生
2. 删除学生
3. 修改学生信息
4. 查看指定学生详细信息
5. 查看所有学生列表
6. 添加课程
7. 删除课程
8. 修改课程
9. 查看指定课程详细信息
10. 查看所有课程信息
11. 添加成绩
12. 删除成绩
13. 修改成绩
14. 查看指定成绩详细信息
15. 查看所有成绩信息
16. 查看所有不及格的成绩信息
"""  # 用户界面
inf1 = """
0. 退出程序
1. 登录
2. 注册
"""  # 登录界面
print(inf1)
while 1:
    n = input("请选择登录,注册还是退出:")
    if n == "1":
        if login():
            print(inf2)
            while 1:
                select = int(input("尊敬的用户请选择你的操作:"))
                if select == 1:
                    add_student()
                elif select == 2:
                    delete_id = int(input("输入要删除学生的ID："))
                    if delete_student(delete_id):
                        print("删除成功！")
                    else:
                        print("未找到该学生，删除失败！")

                # elif select == 3:
                # elif select == 4:
                elif select == 5:
                    view()
            # elif select == 6:
            # elif select == 7:
            # elif select == 8:
            # elif select == 9:
            # elif select == 10:
            # elif select == 11:
            # elif select == 12:
            # elif select == 13:
            # elif select == 14:
            # elif select == 15:
            # elif select == 16:
            # else:
            #     exit()
            # pass
    elif n == "2":
        enroll()
    else:
        break

# 1.自己编写方法对列表进行升序排列(冒泡，选择排序)
# [10,50,20,60,40,30]

# 冒泡！
# 进行n-1趟比较
# 每一次比较都将较大的那个置后，则每一趟都会得出本趟最大值放到本趟的最后一位
# nums = [10, 50, 20, 60, 40, 30]
# n = len(nums)
# for i in range(n - 1):
#     for j in range(0, n - 1 - i):
#         if nums[j + 1] > nums[j]:
#             pass
#         else:
#             nums[j + 1], nums[j] = nums[j], nums[j + 1]

# 选择！
#
# for i in range(n - 1):
#     min_index = i
#     for j in range(i + 1, n):
#         min_index = min_index if nums[min_index] < nums[j] else j
#     nums[min_index], nums[i] = nums[i], nums[min_index]


# print(nums)
