import os
import json

datas = {
    'students': [
        {"id": 101, "name": 12, "age": 18, "sex": "男"}
    ],
    'user': [
        {'id': 11, 'name': 'aa', 'pwd': '123456'},
        {'id': 12, 'name': 'bb', 'pwd': '111222'}
    ]
}
# user_id = 13
# course_id = 1002
student_id_order = 102
file_name = "file_name"


def load_datas():
    global datas, student_id_order
    if os.path.exists(file_name):
        with open(file_name, "r+", encoding="utf-8") as f:
            lines = f.readlines()
            student_id_order = int(lines[-1])
            f.writelines(lines[:-1])
            datas = json.load(f)
    else:
        # 如果没有文件，也就是第一次执行程序。
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(datas, f)
        with open(file_name, "a", encoding="utf-8") as f:
            str_line = "\n" + json.dumps(student_id_order)
            f.write(str_line)


def save_datas():
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(datas, f)
    with open(file_name, "a", encoding="utf-8") as f:
        str_line = "\n" + json.dumps(student_id_order)
        f.write(str_line)







# def course():
#     global course_id
#     if n == 6:  # 添加课程
#         while 1:
#             tem_na = input("输入课程的名字,长度为2或者3：")
#             if len(tem_na) > 3 or len(tem_na) < 2:
#                 print("名字不合法！")
#             else:
#                 break
#         datas["course"].append({"id": course_id, "name": tem_na})
#         course_id += 1
#         print("添加课程完成！")
#     elif n == 7:  # 删除课程
#         delete_id = int(input("输入要删除课程的ID："))
#         for di in datas["course"]:
#             if di["id"] == delete_id:
#                 datas["course"].remove(di)
#                 print("删除课程完成！")
#         print("未查到此课程，删除课程失败！")
#     elif n == 8:  # 修改课程
#         modified_id = int(input("输入需要修改课程的id"))
#         for di in datas["course"]:
#             if di["id"] == modified_id:
#                 while 1:
#                     tem_na = input("输入新名字,长度为2或者3：")
#                     if len(tem_na) > 3 or len(tem_na) < 2:
#                         print("名字不合法！")
#                     else:
#                         break
#                 di.update({"name": tem_na})
#                 print("修改完成！")
#                 break
#         else:
#             print("查找课程失败，无法修改！")
#     # 下面是查看指定课程id信息
#     elif n == 9:
#         looked_id = int(input("输入需要查看课程的id"))
#         for di in datas["course"]:
#             if di["id"] == looked_id:
#                 print(di)
#                 break
#         else:
#             print("查找失败！")
#
#     elif n == 10:
#         print(datas["course"])


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


def delete_student():
    deleted_student_id = int(input("请输入要删除学生的id:"))
    if isexist_student(deleted_student_id):
        for di in datas["students"]:
            if di["id"] == deleted_student_id:
                datas["students"].remove(di)
                count = len(datas["students"])
                save_datas()
                print(f"删除成功！现在还有{count}个学生。")
                return
    else:
        print("删除失败！")


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


# print(inf1)


def show_user_interface():
    print(f"欢迎来到学生管理系统".center(30, "$"))
    print("0. 退出程序")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 修改指定学生信息")
    print("4. 查看指定学生信息")
    print("5. 查看所有学生信息")


def select_check(tip, scope):
    option = int(input(tip))
    if option in scope:
        return True, option
    else:
        print("输入内容不合法！请重新输入！")
        return False, None


def quit_process():
    print("感谢使用！欢迎下次再来！")
    exit()


def view_all_students():
    if isexist_student():
        for st in datas["students"]:
            print(st)
    print("所有学生信息显示完毕！")


def isexist_student(student_id=0):
    if student_id == 0:
        if len(datas["students"]) == 0:
            print("该学生管理系统中还未有学生。")
            return False
        else:
            return True
    else:
        for stu in datas["students"]:
            if stu["id"] == student_id:
                return True
        print(f"未找到id为{student_id}的学生！")
        return False


def input_three_items():
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
    return tem_na, tem_ag, tem_se


def add_student():
    global student_id_order
    base_information = input_three_items()
    if isexist_student():
        new_student = {"id": student_id_order, "name": base_information[0],
                       "age": base_information[1],
                       "sex": base_information[2]}

    else:
        new_student = {"id": student_id_order, "name": base_information[0],
                       "age": base_information[1],
                       "sex": base_information[2]}
    # noinspection PyTypeChecke
    student_id_order += 1
    datas['students'].append(dict(new_student))
    save_datas()
    print("添加成功！")


def main():
    load_datas()
    while 1:
        show_user_interface()
        # n = input("请选择登录,注册还是退出:")
        ret_option = select_check("尊敬的用户请选择你的操作:", [i for i in range(6)])
        if ret_option[0]:
            if ret_option[1] == 0:
                quit_process()
            elif ret_option[1] == 1:
                add_student()
            elif ret_option[1] == 2:
                delete_student()
            elif ret_option[1] == 3:
                pass
            elif ret_option[1] == 4:
                pass
            elif ret_option[1] == 5:
                view_all_students()
        # add_student()
        #     delete_id = int(input("输入要删除学生的ID："))
        #     if delete_student(delete_id):
        #         print("删除成功！")
        #     else:
        #         print("未找到该学生，删除失败！")
        #
        #
        #     view()
        # elif select == 11:
        # elif select == 12:
        # elif select == 13:
        # elif select == 14:
        # elif select == 15:
        # elif select == 16:
        else:
            pass
    # else:
    #     exit()
    # # pass
    # elif n == "2":
    # enroll()
    # else:
    # break


main()
