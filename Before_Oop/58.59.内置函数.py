import turtle

canvas = turtle.Screen()
pen = turtle.Turtle()

# 设置画笔属性
pen.fillcolor("red")
pen.pensize(3)

# 绘制爱心
pen.begin_fill()
pen.left(140)
pen.forward(224)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.left(120)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.forward(224)
pen.end_fill()

# 关闭画布
canvas.exitonclick()
