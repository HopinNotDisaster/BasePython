import json
import os


# 7.编写完整版管理系统，包含学生，课程，成绩


# 1.编写open函数读写文本文件与图片，使用各种模式

# f = open("test1.txt", "w", encoding='GBK')
# context = "使用open的W模式来创建和写入文本"
# f.write(context)
# f.close()
# with open("test1.txt", "r") as f:
#     tem_text = f.read()
#     print(tem_text)

# f = open("test1.txt", "a", encoding='GBK')
# context = "\n再来二行\n已经换行了"
# f.write(context)
# f.close()

# with open("C:\\Users\\QK\\Desktop\\1682652260525.jpg", 'rb') as f:
#     tem = f.read()
#     f1 = open("syq.txt", "wb",encoding="utf8")
#     f1.write(tem)
#     f1.close()

# f = open("test1.txt", "w", encoding='GBK')
# context = "使用open的W模式来创建和写入文本"
# f.write(context)
# f.close()
# with open("test1.txt", "r") as f:
#     tem_text = f.read()
#     print(tem_text)
# 2.编写json模块中dumps、loads、dump、load基础用法

#
# dic = {
#     "aaa": 111,
#     "bbb": 222
# }
# # f = open("test1.txt", "a", encoding='GBK')
# # tem = json.dumps(dic)
# # f.write(f"\n{tem}")
# # f.close()
# with open("test1.txt", "r", encoding='GBK') as f:
#     tem = f.readlines()
#     tem_ = tem[1]
#     dict_ = json.loads(tem_)
#     print(dict_, type(dict_))
# print(dic)
# 3.编写案例每次都可以读取现有学生信息，可以添加学生信息，并将学生信息保存到文件，方便下次读取
# import os
#
# students = [
#     {"id": 101, "name": "aaa"},
#     {"id": 102, "name": "bbb"}
# ]
# stu_id = 103
#
# if os.path.exists("student_3.txt"):
#     tem = {"id": stu_id, "name": input("请输入名字：")}
#     tem_s = json.dumps(tem)
#     with open("student_3.txt", 'w') as f:
#         f.write(tem_s)
#         f.close()
# else:
#     with open("student_3.txt", 'a') as f:
#         tem = {"id": 101, "name": input("请输入名字：")}
#         tem_s = json.dumps(tem)
#         f.write(f"\n{tem_s}")
#         f.close()
#
# with open("student_3.txt", 'r') as f:
#     tem_s = f.read()
#     tem = json.loads(tem_s)
#     print(tem)

#
# 4.编写代码演示装饰器语法的思路
# 1.要有函数嵌套！
# 2.要有内部函数使用外部函数的局部变量
# 3.要返回一个函数
# 5.编写时间统计与用户校验装饰器
# def decorator(f):
#     def time_cal():
#         begin = time.time()
#         f()
# #         print(time.time() - begin)
# #     return time_cal
# def decorator_2(f):
#     def chark():
#         user = input("输入：")
#         if user == "aaa":
#             f()
#         else:
#             print("输入错误！")

# 8.自学os模块

#
# 在 Python 中，os 模块是用于与操作系统进行交互的模块，它提供了许多函数
# 用于执行操作系统相关的任务，例如文件和目录操作、进程管理、环境变量等。可以使用以下方式导入 os 模块：
#
# python
# import os
# 下面是一些常用的 os 模块函数：
#
# 文件和目录操作：
#
# os.getcwd()：获取当前工作目录的路径。
# os.chdir(path)：更改当前工作目录到指定的路径。
# os.listdir(path)：返回指定目录下的所有文件和文件夹列表。
# os.mkdir(path)：创建一个新的目录。
# os.rmdir(path)：删除指定的目录。
# 路径操作：
#
# os.path.join(path1, path2, ...)：将多个路径组合成一个有效路径。
# os.path.abspath(path)：返回指定路径的绝对路径。
# os.path.exists(path)：检查路径是否存在。
# os.path.isfile(path)：判断给定路径是否为文件。
# os.path.isdir(path)：判断给定路径是否为目录。
# 环境变量：
#
# os.environ：一个包含环境变量的字典。
# os.getenv(key)：获取指定环境变量的值。
# os.putenv(key, value)：设置指定环境变量的值。
# 执行系统命令：
#
# # os.system(command)：在子shell中执行系统命令。
# # 这只是 os 模块中的一些常用函数，还有其他更多的函数可供使用。你可以通过查阅 Python 官方文档或使用 help(os) 命令来了解更多详细信息。
#
# # # print(help("os"))
# # # 6.学生管理系统，对学生完成增删改查(参考完整版中的学生相关功能)
# # students = [
# #
# # ]
# inf = """
# 0. 退出程序
# 1. 添加学生
# 2. 删除学生
# 3. 修改学生信息
# 4. 查看指定学生详细信息
# 5. 查看所有学生列表
# """
#
#
# def addstu():
#     if os.path.exists("student_small.txt"):  # 有文件
#         with open("student_small.txt", 'r') as f:
#             lines = f.readlines()
#             stu_id = int(lines[0])
#         with open("student_small.txt", 'a') as f:
#             tem = {"id": stu_id, "name": input("请输入名字：")}
#             # for i in range(1,len(lines)):
#             #     students.append(json.loads(lines[i]))
#             s_tem = json.dumps(tem) + "\n"
#             lines.append(s_tem)
#         lines[0] = str(stu_id + 1) + "\n"
#         with open("student_small.txt", 'w') as f:
#             f.writelines(lines)
#     else:  # 没有文件
#         with open("student_small.txt", 'w') as f:
#             tem = {"id": 101, "name": input("请输入名字：")}
#             f.write('102')
#         with open("student_small.txt", 'a') as f:
#             j_str = json.dumps(tem)
#             f.write(f"\n{j_str}\n")
#     print("添加完成！")
#
#
# def delstu():
#     with open("student_small.txt", 'r') as f:
#         lines = f.readlines()
#     with open("student_small.txt", 'w') as f:
#         delid = int(input("输入要删除的id："))
#         for i in range(1, len(lines)):
#             dic = json.loads(lines[i])
#             if dic["id"] == delid:
#                 lines.pop(i)
#                 break
#         else:
#             print("未找到该学生，删除失败")
#             return None
#         f.writelines(lines)
#     print("删除成功！")
#
#
# def lookstu():
#     with open("student_small.txt", 'r') as f:
#         lines = f.readlines()
#         for i in range(1, len(lines)):
#             dic_line = json.loads(lines[i])
#             print(dic_line)
#
#
# print(inf)
# while 1:
#     sel = int(input("输入你要进行的操作:"))
#     if sel == 1:
#         addstu()
#     elif sel == 2:
#         delstu()
#     elif sel == 5:
#         lookstu()
#     else:
#         exit()


# with open("test1.txt", "r") as f:
#     tem = f.readlines()
#     # print(tem[1], type(tem[1]))
#     di = json.loads(tem[1])
#     print(di, type(di))

# 用闭包给函数添加新功能
#
# # def fun(f):
#
#
# def cart():
#     print("欢迎来到购物车！")
#
#
# def f1(f):
#     def chark():
#         user = input("请输入用户名")
#         if user == "abc":
#             f()
#         else:
#             print("登陆失败")
# # check
#     return chark
# cart = f1(cart)
# cart()

