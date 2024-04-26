# class Person:
#     pass
#
#
# # 命名规则
# # 类名 +（）默认返回一个实例
#
#
# a = 12
# p120 = Person()
# p40 = Person()
# p30 = Person()
# p20 = Person()
# p10 = Person()
# p = Person()
# p8 = Person()
# # p7 = Person()
# # p6 = Person()
# # p5 = Person()
# # p4 = Person()
# # p3 = Person()
# # p2 = Person()
# # p1 = Person()
#
# class Person:
#     # 在调用Person后会先去执行__init__初始化函数
#
#     def __init__(self):  # 初始化函数！
#         print(id(self))
#         self.name = 17
#
#
# p1 = Person()
# # print(p1.name)
# # i1 = 12
# # print(i1)
#
# import tkinter as tk
#
#
# def on_canvas_click(event):
#     x = event.x
#     y = event.y
#     canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")  # 在点击位置绘制一个红色圆形
#
#
# root = tk.Tk()
# root.title("绘制图形示例")
#
# canvas = tk.Canvas(root, width=400, height=400)
# canvas.pack()
#
# canvas.bind("<Button-1>", on_canvas_click)  # 绑定鼠标左键点击事件到函数 on_canvas_click
#
# root.mainloop()

import tkinter as tk


def on_canvas_press(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y


def on_canvas_release(event):
    end_x = event.x
    end_y = event.y
    canvas.create_rectangle(start_x, start_y, end_x, end_y, outline="black")  # 通过鼠标拖动绘制矩形


root = tk.Tk()
root.title("通过鼠标拖动绘制图形示例")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

canvas.bind("<Button-1>", on_canvas_press)  # 绑定鼠标左键按下事件到函数 on_canvas_press
canvas.bind("<ButtonRelease-1>", on_canvas_release)  # 绑定鼠标左键释放事件到函数 on_canvas_release

root.mainloop()
