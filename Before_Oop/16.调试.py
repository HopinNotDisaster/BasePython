# 1231546
# 1221223
# 2121231
# 123

# CTRL+ / 注释快捷键

# CTRL+ / 注释快捷键
# CTRL+ / 注释快捷键
# CTRL+ / 注释快捷键
# CTRL+ / 注释快捷键
# CTRL+ / 注释快捷键
# CTRL+ / 注释快捷键
# CTRL+ / 注释快捷键
# print()
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)

#
# x = int(input("0.0:"))
# if x % 2:
#     print("1")
# else:
#     print("0")

# 计算1+2+3+...+100
# ans = 0
# for i in range(101):
#     ans += i
# print(ans)

# for i in range(10):
#     if i == 3:
#         continue
#     if i == 5:
#         break

import tkinter as tk


def start_drawing(event):
    global start_x, start_y, rect_id
    start_x = event.x
    start_y = event.y
    rect_id = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="black")  # 创建一个黑色矩形轮廓


def draw_rectangle(event):
    global start_x, start_y, rect_id
    end_x = event.x
    end_y = event.y
    canvas.coords(rect_id, start_x, start_y, end_x, end_y)  # 更新矩形轮廓的坐标


start_x = 0
start_y = 0
rect_id = 0
root = tk.Tk()
root.title("拖拽绘制矩形示例")

# 创建画布
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# 绑定鼠标点击事件
canvas.bind("<ButtonPress-1>", start_drawing)

# 绑定鼠标拖拽事件
canvas.bind("<B1-Motion>", draw_rectangle)

root.mainloop()
