import sys
import pygame

pygame.init()

SIZE = (900, 900)

screen = pygame.display.set_mode(SIZE)
screen.fill("pink")
# pygame.mixer.music.load("339.mp3")
# pygame.mixer.music.play(loops=10)
eff = pygame.mixer.Sound("effect.mp3")

# bg = pygame.image.load("syq.ico")
# bg2 = pygame.image.load("syq.ico")  # 是Surface类型！
# screen.fill("purple", (0, 0, 100, 100))
# # screen.fill("")
#
# circle_rect = pygame.draw.circle(screen, "black", (300, 10), 10)  # 返回一个Rect类型！
# print(type(circle))
# print(circle.top, circle.left)
# circle_face = pygame.draw.circle("red", (300, 300), 20)  # 绘制圆形
face1 = pygame.Surface((100, 100))
face1.fill("pink")
# circle_rect1 = circle_face1.get_rect()
face2 = pygame.Surface((10, 10))
face2.fill("red")

x1 = 0
bg_y = 0
bg_y_2 = 900
x2 = 0
y2 = 0
running = 1
while 1:
    for event in pygame.event.get():
        # print(event)
        if event.type == 256:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            eff.play()
            running = not running
    if running:

        bg_y -= 1
        if bg_y < -900:
            bg_y = 900
        bg_y_2 -= 1
        if bg_y_2 < -900:
            bg_y_2 = 900
        # screen.blit(,)
        # 更新
        x1 += 1
        if x1 > 900:
            x1 = 0
        x2 += 1
        y2 += 1
        if x2 > 900:
            x2 = 0
            y2 = 0
    screen.blit(face1, (x1, 450))
    screen.blit(face2, (x2, y2))
    pygame.display.flip()  # 全部更新
    # pygame.display.update()  # 可以部分更新
