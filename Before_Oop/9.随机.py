# # import keyword
# #print(keyword.kwlist)
#
# # 编写应用程序经常使用随机模块
#
# import random
# # 随机选取一个数字在[0,1)
# print(random.random())
# #随机取一个整数[a,b]
# print(random.randint(1,3))
#
# # 从列表中选择
# print(random.choice(["1", "2" ,"3"]))
# print(random.choices(["52", "545", "45"], [0.8, 0.1,0.1], k = 2))
# print(random.sample(["11", "113", "444"],  k = 2))
#
#
#


from turtle import Turtle, Screen

# turtle 是个包  Turtle是海龟类！ Screen是屏幕类！
# 创建Turtle对象和Screen对象
turtle = Turtle()
screen = Screen()

# 绘制矩形
turtle.forward(200)  # 向前移动200个单位
turtle.right(90)  # 右转90度
turtle.forward(100)  # 向前移动100个单位
turtle.right(90)  # 右转90度
turtle.forward(200)  # 向前移动200个单位
turtle.right(90)  # 右转90度
turtle.forward(100)  # 向前移动100个单位

# 关闭窗口
screen.exitonclick()
# input("按任意键关闭窗口！")
