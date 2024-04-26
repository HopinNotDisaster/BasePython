# import tkinter as tk
#
#
# def first():
#     """
#     点击按钮，可以让文字显性与消失轮替。
#     :return:
#     """
#     window = tk.Tk()
#     window.title("My first window.")
#     window.geometry("500x200")  # 横×竖
#
#     var_text = tk.StringVar()
#
#     label = tk.Label(window, textvariable=var_text, font=("Arial", 18), bg="#800080", fg="white", width=15, height=2)
#     label.pack()
#
#     is_hit = False
#
#     def hit_me():
#         nonlocal is_hit
#         if not is_hit:
#             is_hit = True
#             var_text.set("you hit me.")
#         else:
#             is_hit = False
#             var_text.set("")
#
#     button = tk.Button(window, text="hit me",
#                        width=15, height=2, font=("Arial", 15),
#                        command=hit_me)
#     button.pack()
#     window.mainloop()
#
#
# from turtle import RawTurtle, TurtleScreen
#
#
# def draw_square():
#     turtle.pendown()
#     print(id(turtle))
#     for _ in range(4):
#         turtle.forward(100)
#         turtle.right(90)
#     turtle.penup()
#
#
# def paint_love():
#     # 创建一个画布和画笔
#
#     pen = turtle
#
#     # 设置画笔属性
#     pen.fillcolor("red")
#     pen.pensize(3)
#     pen.goto(0, -100)
#     # 绘制爱心
#     pen.begin_fill()
#     pen.left(140)
#     pen.forward(224)
#     for _ in range(200):
#         pen.right(1)
#         pen.forward(2)
#     pen.left(120)
#     for _ in range(200):
#         pen.right(1)
#         pen.forward(2)
#     pen.forward(224)
#     pen.end_fill()
#
#
# root = tk.Tk()
# canvas = tk.Canvas(root, width=1000, height=500)
# canvas.pack()
#
# screen = TurtleScreen(canvas)
# turtle = RawTurtle(screen)
# print(id(turtle))
# button = tk.Button(root, text="Draw Square", command=paint_love)
# button.pack()
#
# tk.mainloop()
#
# import tkinter as tk
#
#
# def draw_rectangle():
#     canvas.create_rectangle(50, 50, 150, 100, fill="blue")  # 在画布上绘制一个蓝色矩形
#
#
# def draw_oval():
#     canvas.create_oval(50, 150, 150, 200, fill="red")  # 在画布上绘制一个红色圆形
#
#
# root = tk.Tk()
# root.title("菜单示例")
# root.geometry("800x400")
#
# # 创建菜单栏
# menu_bar = tk.Menu(root)
#
# # 添加“绘图”菜单
#
# draw_menu = tk.Menu(menu_bar, tearoff=0)
# draw_menu.add_command(label="矩形", command=draw_rectangle)  # 添加“矩形”选项
# draw_menu.add_command(label="圆形", command=draw_oval)  # 添加“圆形”选项
# menu_bar.add_cascade(label="绘图", menu=draw_menu)
#
# # 创建画布
# canvas = tk.Canvas(root, width=200, height=300)
# canvas.pack()
#
# root.config(menu=menu_bar)
# root.mainloop()

#
# import tkinter as tk
#
# def start_drawing(event):
#     global start_x, start_y
#     start_x = event.x
#     start_y = event.y
#
# def draw_rectangle(event):
#     global start_x, start_y
#     end_x = event.x
#     end_y = event.y
#     canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="blue")  # 在画布上绘制一个蓝色矩形
#
# root = tk.Tk()
# root.title("绘制矩形示例")
#
# # 创建画布
# canvas = tk.Canvas(root, width=400, height=300)
# canvas.pack()
#
# # 绑定鼠标点击事件
# canvas.bind("<ButtonPress-1>", start_drawing)
#
# # 绑定鼠标释放事件
# canvas.bind("<ButtonRelease-1>", draw_rectangle)
#
# root.mainloop()

# import tkinter as tk
#
#
# def start_drawing(event):
#     global start_x, start_y, circle_id
#     start_x = event.x
#     start_y = event.y
#     circle_id = canvas.create_oval(start_x, start_y, start_x, start_y, outline="black")  # 创建一个黑色圆形轮廓
#
#
# def draw_circle(event):
#     global start_x, start_y, circle_id
#     end_x = event.x
#     end_y = event.y
#     radius = max(abs(end_x - start_x), abs(end_y - start_y))  # 计算半径
#     canvas.coords(circle_id, start_x - radius, start_y - radius, start_x + radius, start_y + radius)  # 更新圆形轮廓的坐标
#
#
# root = tk.Tk()
# root.title("拖拽绘制圆形示例")
#
# # 创建画布
# canvas = tk.Canvas(root, width=400, height=300)
# canvas.pack()
#
# # 绑定鼠标点击事件
# canvas.bind("<ButtonPress-1>", start_drawing)
#
# # 绑定鼠标拖拽事件
# canvas.bind("<B1-Motion>", draw_circle)
#
# root.mainloop()

# import tkinter as tk
#
#
# def on_press(event):
#     global start_x, start_y
#     start_x = event.x
#     start_y = event.y
#
#
# def on_drag(event):
#     global start_x, start_y
#     canvas.create_oval(start_x, start_y, event.x, event.y, fill=fill_color.get())
#
#
# root = tk.Tk()
# root.title("拖拽绘制圆形并填充颜色")
#
# canvas = tk.Canvas(root, width=400, height=300)
# canvas.pack()
#
# fill_color = tk.StringVar()
# fill_color.set("red")  # 设置初始填充颜色为红色
#
# color_entry = tk.Entry(root, textvariable=fill_color)
# color_entry.pack()
#
# canvas.bind("<Button-1>", on_press)
# canvas.bind("<B1-Motion>", on_drag)
#
# root.mainloop()

# import tkinter as tk
#
#
# def on_press(event):
#     global start_x, start_y
#     start_x = event.x
#     start_y = event.y
#
#
# def on_drag(event):
#     canvas.create_oval(start_x, start_y, event.x, event.y, fill=fill_color.get())
#
#
# root = tk.Tk()
# root.title("拖拽绘制圆形并填充颜色")
#
# canvas = tk.Canvas(root, width=400, height=300)
# canvas.pack()
#
# fill_color = tk.StringVar(value="red")  # 设置初始填充颜色为红色
#
# color_entry = tk.Entry(root, textvariable=fill_color)
# color_entry.pack()
#
# canvas.bind("<Button-1>", on_press)
# canvas.bind("<B1-Motion>", on_drag)
#
# # root.mainloop()
#
# import tkinter as tk
#
#
# def on_press(event):
#     global start_x, start_y
#     start_x = event.x
#     start_y = event.y
#
#
# def on_drag(event):
#     global start_x, start_y
#     canvas.delete("circle")  # 删除之前的圆形
#     canvas.create_oval(start_x, start_y, event.x, event.y, fill=fill_color.get(), tags="circle")
#
#
# root = tk.Tk()
# root.title("拖拽绘制圆形并填充颜色")
#
# canvas = tk.Canvas(root, width=400, height=300)
# canvas.pack()
#
# fill_color = tk.StringVar(value="red")  # 设置初始填充颜色为红色
#
# color_entry = tk.Entry(root, textvariable=fill_color)
# color_entry.pack()
#
# canvas.bind("<Button-1>", on_press)
# canvas.bind("<B1-Motion>", on_drag)
#
# root.mainloop()


import tkinter as tk
from tkinter import colorchooser


class Draw_Gui:
    def __init__(self):
        self.str_current_shape = ""
        self.max_id = 0
        self.current_color = "black"
        self.init_root()
        self.init_canvas()
        self.init_status()
        self.init_menu()
        self.init_event()

    def init_root(self):
        self.root = tk.Tk()
        self.root.title("My draw")

    def init_status(self):
        # if self.str_current_shape:
        #     self.status = tk.Label(self.root, text="正在绘制:" + self.str_current_shape)
        #     self.status.pack(side="left")
        # else:
        self.status = tk.Label(self.root, text="请选择你要绘制的图形。")
        self.status.pack(side="left")

    def init_canvas(self):
        self.canvas = tk.Canvas(self.root, width=500, height=300, bg="#500018")
        self.canvas.pack()

    def init_event(self):
        self.canvas.bind("<Button-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        # self.canvas.bind("<ButtonRelease-3>", self.on_release)

    def init_menu(self):
        self.menu_bar = tk.Menu(self.root)

        self.draw_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.draw_menu.add_command(label="矩形", command=lambda: self.change_current_shape("矩形"))  # 添加“矩形”选项
        self.draw_menu.add_command(label="圆形", command=lambda: self.change_current_shape("圆形"))  # 添加“圆形”选项
        self.menu_bar.add_cascade(label="绘图", menu=self.draw_menu)

        self.colour_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.colour_menu.add_command(label="紫色", command=self.set_color)
        self.colour_menu.add_separator()
        self.colour_menu.add_command(label="自定义", command=self.select_color)
        self.menu_bar.add_cascade(label="颜色", menu=self.colour_menu)

        self.other_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.other_menu.add_command(label="清除", command=self.other_clear)
        self.other_menu.add_command(label="撤销", command=self.other_undo)
        self.other_menu.add_command(label="退出软件", command=self.other_exit)
        self.menu_bar.add_cascade(label="其他", menu=self.other_menu)

        self.root.config(menu=self.menu_bar)

    def set_color(self):
        self.current_color = "purple"

    def select_color(self):
        color = colorchooser.askcolor()
        if color[1]:
            self.current_color = color[1]

    def other_clear(self):
        self.canvas.delete("all")
        self.max_id = 0

    def other_undo(self):
        self.canvas.delete(self.max_id)
        self.max_id -= 1

    def change_current_shape(self, shape):
        self.str_current_shape = shape
        self.status.config(text="正在绘制:" + self.str_current_shape)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.str_current_shape == "矩形":
            self.max_id = self.canvas.create_rectangle(event.x, event.y,
                                                       event.x, event.y, outline=self.current_color)
        elif self.str_current_shape == "圆形":
            self.max_id = self.canvas.create_oval(event.x, event.y,
                                                  event.x, event.y, outline=self.current_color)

    def on_drag(self, event):
        self.canvas.coords(self.max_id, self.start_x, self.start_y,
                           event.x, event.y)

    def other_exit(self):
        self.canvas.quit()

    def run(self):
        self.root.mainloop()


d = Draw_Gui()
d.run()
# d.init_canvas()
