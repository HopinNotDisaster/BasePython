"""import turtle

# 指定画笔宽度
turtle.width(10)
# 指定画笔颜色
turtle.color("green","blue") # 画笔颜色，填充颜色
# 开始填充 turtle.begin_fill()的作用是开始填充当前绘制的图形，
# 直到遇到与turtle.end_fill()相匹配的函数。
turtle.begin_fill() 

turtle.circle(100, 180) # 指定半径

turtle.end_fill() # 成对出现


# 设置循环
turtle.mainloop()

import turtle

# 创建一个画布对象
my_turtle = turtle.Turtle()
my_turtle.width(40)
# 开始填充
my_turtle.begin_fill()

# 绘制矩形
for i in range(2):
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)

# 结束填充
my_turtle.end_fill()

# 等待用户关闭窗口
turtle.done()
"""
import turtle

# 创建一个画布对象
my_turtle = turtle.Turtle()

# 设置画笔颜色和粗细
my_turtle.pensize(3)

# 绘制头部
my_turtle.circle(50)

# 绘制眼睛
my_turtle.penup()
my_turtle.goto(-20, 70)
my_turtle.pendown()
my_turtle.fillcolor("black")
my_turtle.begin_fill()
my_turtle.circle(10)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.goto(20, 70)
my_turtle.pendown()
my_turtle.fillcolor("black")
my_turtle.begin_fill()
my_turtle.circle(10)
my_turtle.end_fill()

# 绘制嘴巴
my_turtle.penup()
my_turtle.goto(0, 40)
my_turtle.pendown()
my_turtle.setheading(-60)
my_turtle.circle(30, 120)

# 绘制身体
my_turtle.penup()
my_turtle.goto(-50, -50)
my_turtle.pendown()
my_turtle.setheading(-90)
my_turtle.forward(100)

# 绘制胳膊
my_turtle.left(45)
my_turtle.forward(70)
my_turtle.backward(70)

my_turtle.right(90)
my_turtle.forward(70)
my_turtle.backward(70)

# 绘制腿部
my_turtle.left(45)
my_turtle.forward(100)
my_turtle.backward(100)

# 绘制帽子
my_turtle.penup()
my_turtle.goto(-50, 100)
my_turtle.pendown()
my_turtle.setheading(0)
my_turtle.fillcolor("red")
my_turtle.begin_fill()
my_turtle.forward(100)
my_turtle.left(120)
my_turtle.forward(100)
my_turtle.left(120)
my_turtle.forward(100)
my_turtle.end_fill()

# 绘制帽檐
my_turtle.penup()
my_turtle.goto(-50, 100)
my_turtle.pendown()
my_turtle.setheading(-90)
my_turtle.fillcolor("yellow")
my_turtle.begin_fill()
my_turtle.circle(50, 180)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.circle(50, 180)
my_turtle.end_fill()

# 等待用户关闭窗口
turtle.done()
