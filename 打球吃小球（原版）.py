import pygame

from enum import Enum, unique
from math import sqrt
from random import randint


@unique
class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return r, g, b


class Ball:
    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy

        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = - self.sx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = - self.sy

    def eat(self, other):
        """吃其它球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)


def main():
    # 所有球
    balls = []

    pygame.init()
    # 设置窗口标题
    pygame.display.set_caption('大球吃小球')

    # 显示窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))

    # 加载图片
    # ball_img = pygame.image.load('ball.png')
    # 在窗口上渲染图片
    # screen.blit(ball_img, (50, 50))
    # 开启一个事件循环：用于处理发生的事件
    running = True
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 鼠标事件
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获取鼠标点击的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)

        # 设置窗口的背景色RGB
        screen.fill((255, 255, 255))
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        # 刷新当前窗口（渲染窗口将绘制的图形呈现出来）
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置在刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()
