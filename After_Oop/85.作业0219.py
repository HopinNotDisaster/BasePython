# 一、按照以下流程完成tkinter绘图软件
# # 1. 空窗体 初始化 标题 logo
# # 2. 初始化 菜单 画布 状态栏
# # 3. 添加菜单事件  绘制矩形 直线 圆形  撤销 清除 退出
# # 4. 添加鼠标事件 左键点击 左键拖拽 左键抬起 右键抬起
# # 5. 当前选择图形 当前选择颜色  状态栏
# # 6. 鼠标点下绘制图形  鼠标拖拽更新绘制  鼠标抬起结束绘制

# import tkinter as tk
#
# window = tk.Tk()
#
#
# def init_window():
#     window.title("My Window.")
#     window.geometry("800x400")
#     icon = tk.PhotoImage(file="firefly.ico")
#     window.wm_iconphoto(True, icon)
#     window.configure(bg="blue")
#
#
# max_id = 0
# start_x = None
# start_y = None
# cur_figure = ""
# init_window()
# canvas_bg_colour = tk.StringVar()
# # print(type(canvas_bg_colour))  # tkinter.StringVar类型
# canvas_bg_colour.set("lightgreen")
# canvas = tk.Canvas(window, width=700, height=300)
# canvas.configure(bg=canvas_bg_colour.get())
# canvas.pack()
#
# label = tk.Label(window, text="暂无绘制图形！")
# label.pack(side="left")
#
#
# def draw_rectangle():
#     global cur_figure, label
#     cur_figure = "矩形"
#     canvas.bind("<ButtonPress-1>", start_draw)  # 点击事件
#     canvas.bind("<B1-Motion>", drawing)
#     label.config(text="正在绘制矩形！")
#
#
# def draw_circle():
#     global cur_figure, label
#     cur_figure = "圆形"
#     canvas.bind("<ButtonPress-1>", start_draw)  # 点击事件
#     canvas.bind("<B1-Motion>", drawing)
#     label.config(text="正在绘制圆形！")
#
#
# def start_draw(event):
#     global start_x, start_y, max_id, cur_figure
#     start_x = event.x
#     start_y = event.y
#     if cur_figure == "矩形":
#         max_id = canvas.create_rectangle(start_x, start_y, event.x, event.y, )
#         # canvas.create_rectangle(start_x, start_y, start_x, start_y, )
#     elif cur_figure == "圆形":
#         max_id = canvas.create_oval(start_x, start_y, event.x, event.y)
#         # canvas.create_oval(start_x, start_y, start_x, start_y, )
#
#
# def drawing(event):
#     global start_x, start_y, max_id, cur_figure
#     start_x = float(start_x)
#     start_y = float(start_y)
#     if cur_figure == "矩形":
#         canvas.coords(max_id, start_x, start_y, event.x, event.y)  # 更新矩形轮廓的坐标
#     elif cur_figure == "圆形":
#         canvas.coords(max_id, start_x, start_y, event.x, event.y)
#
#
# def revocation():
#     global max_id
#     if max_id == 0:
#         pass
#     else:
#         canvas.delete(max_id)
#         max_id -= 1
#
#
# menu_bar = tk.Menu(window)
# # 添加“绘图”菜单
# draw_menu = tk.Menu(menu_bar, tearoff=0)  # draw_menu想在menu_bar上
# draw_menu.add_command(label="矩形", command=draw_rectangle)
# draw_menu.add_command(label="圆形", command=draw_circle)
# menu_bar.add_cascade(label="绘图", menu=draw_menu)  # menu_bar同意add
# # 添加'其他'菜单
# other_menu = tk.Menu(menu_bar, tearoff=0)
# other_menu.add_command(label="撤销", command=revocation)
# menu_bar.add_cascade(label="其他", menu=other_menu)
#
# window.config(menu=menu_bar)
#
# window.mainloop()

# 二、按照以下流程学习pygame
# 1. 使用pygame 完成一个可以关闭的窗体
# 2. 给窗体添加一个背景色，并在背景层上添加一个有颜色的矩形和一张图片
# 3. 给窗体添加logo与标题
# # 4. 让窗体中的图片可以上下往复移动
# # 5. 添加空格按键事件 可以控制图片运动暂停与音乐音效
# import sys
# import pygame
#
# pygame.init()
# SIZE = (829, 826)
#
# screen = pygame.display.set_mode(SIZE)
# screen.fill("pink")
# eff = pygame.mixer.Sound("effect.mp3")
# ico_image = pygame.image.load("firefly.ico")
# # circle_rect = pygame.draw.circle(screen, "black", (300, 10), 10)  # 返回一个Rect类型！
# # print(type(circle))
# # print(circle.top, circle.left)
# bg_image = ico_image
# highest = pygame.Surface((100, 100), pygame.SRCALPHA)
# pygame.draw.circle(highest, "lightgreen", (50, 50), 50)  # 绘制圆形
# ly1y = 0
# ly2y = 826
# running = 1
# while 1:
#     for event in pygame.event.get():
#         # print(event)
#         if event.type == 256:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
#             eff.play()
#             running = not running
#     if running:
#         ly1y -= 5
#         if ly1y < -826:
#             ly1y = 826
#         ly2y -= 5
#         if ly2y < -826:
#             ly2y = 826
#         screen.blit(bg_image, (0, ly1y))
#         screen.blit(bg_image, (0, ly2y))
#         screen.blit(highest, (150, 100))
#         pygame.display.set_icon(ico_image)
#         pygame.display.flip()  # 全部更新
#         # pygame.display.update()  # 可以部分更新


import pygame


class Exercise_Pygame:
    def __init__(self):
        pygame.init()
        self.running = True
        self.SIZE = (1000, 900)
        self._init_screen()
        self.stop_audio()
        self.firefly_1()
        self.huohuo_2()
        self.hp_3()
        self.flip()

    def firefly_1(self):
        self.image_surface_1 = pygame.image.load("firefly.ico")

    def huohuo_2(self):
        self.image_surface_2 = pygame.image.load("huohuo.png")
        self.huohuo_y = 500

    def hp_3(self):
        self.hpp_surface_3 = pygame.Surface((200, 15))
        self.hpp_surface_3.fill((127, 127, 127))
        self.hp_surface_3 = pygame.Surface((100, 15))
        self.hp_surface_3.fill("green")

    def stop_audio(self):
        self.eff = pygame.mixer.Sound("effect.mp3")

    def _init_screen(self):
        self.screen = pygame.display.set_mode(self.SIZE)

    def flip(self):
        while 1:
            for e in pygame.event.get():
                print(e)
                if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                    self.eff.play()
                    self.running = not self.running
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if self.running:
                self.screen.fill((127, 127, 127), )
                # self.screen.blit(center_surface, (100, 20))
                self.screen.blit(self.image_surface_1, (100, 20))
                self.huohuo_y -= 3
                if self.huohuo_y < -200:
                    self.huohuo_y = 900
                self.screen.blit(self.image_surface_2, (200, self.huohuo_y))
                self.screen.blit(self.hpp_surface_3, (200, self.huohuo_y - 30))
                self.screen.blit(self.hp_surface_3, (200, self.huohuo_y - 30))

                pygame.display.flip()


ep = Exercise_Pygame()

# center_surface = pygame.Surface((400, 200))
# center_surface.fill("green")
