# 一、手写以下知识点理论知识
# 迭代器
# 生成器
# 装饰器
# 二、编码实现以下知识点案例
# 异常处理
# try:
#     prin()
# except SyntaxError:
# #     print("犯了一个SyntaxError错误！")
# # except Exception:
# #     print("try里面的内容出错！")
# #
# # else:
# #     pass
# # finally:
# #     pass
# # 可迭代
# from collections.abc import Iterable, Iterator
#
#
# # 可迭代
# # 可迭代的不一定是迭代器
# # 可迭代的不一定可以用for
# class MyIterable:
#     def __iter__(self):
#         pass
#
#     def iter(self):
#         return self
#
#
# my_iterable = MyIterable()
# print(isinstance(my_iterable, Iterable))  # 是可迭代的但不是迭代器
# print(isinstance(my_iterable, Iterator))
#

# for i in my_iterable:     # 不可以使用for循环进行遍历！
#     print(i)
# 迭代器


# 生成器
# 装饰器
# def decorator(f):
#     def check():
#         print("执行前的检验！")
#         f()
#         print("执行后的检验！")
#
#     return check
#
#
# @decorator
# def fun():
#     print("111")
#
#
# fun()
# 三、学习网盘贪吃蛇源代码
# Z:\share\python2401\第一阶段\素材\贪吃蛇
# 自己按照功能实现进行复原
# 四、修改完善自己小游戏

# import random
from enum import Enum, unique
# from math import sqrt
from random import randint
import pygame

SIZE = (800, 600)


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


class BallSprite(pygame.sprite.Sprite):
    def __init__(self, gm, rect, sx, sy, color):
        super().__init__()
        self.gm = gm
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True
        self.image = pygame.Surface((rect.width, rect.height))
        self.rect = rect

    def move(self, ):
        # if self.alive:
        """移动"""
        self.rect.left += self.sx
        self.rect.top += self.sy
        if self.rect.right > SIZE[0]:
            self.rect.right = SIZE[0]
            self.sx = -self.sx
        elif self.rect.left < 0:
            self.rect.left = 0
            self.sx = -self.sx
        if self.rect.bottom > SIZE[1]:
            self.rect.bottom = SIZE[1]
            self.sy = -self.sy
        elif self.rect.top < 0:
            self.rect.top = 0
            self.sy = -self.sy

    # else:
    #     self.kill()

    def update(self, ) -> None:
        self.move()
        # self.eated()
        self.image.fill(self.color)


class BallManage:
    def __init__(self, gm):
        self.gm = gm
        self.ball_group = pygame.sprite.Group()

    @staticmethod
    def eat(sp1, sp2):
        """吃其它球"""
        if sp1.rect.width * sp1.rect.height > sp2.rect.width * sp2.rect.height:
            # other.alive = False
            sp2.kill()
            # increment = random.randint(1, 10)
            # sp1.rect.width += sp2.rect.width
            # sp1.rect.height += sp2.rect.height
            cur_center = sp1.rect.center
            sp1.image = pygame.Surface((sp1.rect.width + sp2.rect.width, sp1.rect.height + sp2.rect.height))
            sp1.rect = sp1.image.get_rect()
            sp1.rect.center = cur_center
        # elif self.rect.width * self.rect.height < other.rect.width * other.rect.height:
        #     self.kill()
        #     # increment = random.randint(1, 10)
        #     other.rect.width += self.rect.width
        #     other.rect.height += self.rect.height

    def check_collision(self):
        collision_dict = pygame.sprite.groupcollide(self.ball_group, self.ball_group, False, 0)
        # print(collision_dict)
        # 打印碰撞结果
        for sprite, collided_sprites in collision_dict.items():
            if len(collided_sprites) == 1:
                pass
            else:
                self.eat(collided_sprites[0], collided_sprites[1])
        #         print("与精灵 {} 发生碰撞的精灵：".format(sprite))
        #         for collided_sprite in collided_sprites:
        #             print("    {}".format(collided_sprite))
        #     else:
        #         print("000")

    def born(self, event):
        x, y = event.pos
        radius = randint(10, 100)
        sx, sy = randint(-10, 10), randint(-10, 10)
        color = Color.random_color()

        ball = BallSprite(self.gm, pygame.Rect(x, y, radius, radius), sx, sy, color)
        ball.add(self.ball_group)

    def update(self):
        self.check_collision()
        self.ball_group.draw(self.gm.screen)
        self.ball_group.update()

    # def draw(self, screen):
    #     pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('大球吃小球')
        self.clock = pygame.time.Clock()
        # 显示窗口并设置窗口尺寸
        self.screen = pygame.display.set_mode(SIZE)

        self.ball_m = BallManage(self)

    # 加载图片
    # ball_img = pygame.image.load('ball.png')
    # 在窗口上渲染图片
    # screen.blit(ball_img, (50, 50))
    def run(self):
        while 1:
            self.clock.tick(25)
            self.check_event()
            self.draw()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.ball_m.update()
        pygame.display.flip()

    def check_event(self):
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            # 鼠标事件
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.ball_m.born(event)
        # 获取鼠标点击的位置

        # 设置窗口的背景色RGB

        # for ball in balls:
        #     if ball.alive:
        #         ball.draw(screen)
        #     else:
        #         balls.remove(ball)
        # # 刷新当前窗口（渲染窗口将绘制的图形呈现出来）
        #
        # # 每隔50毫秒就改变小球的位置在刷新窗口
        # pygame.time.delay(50)
        # for ball in balls:
        #     ball.move(screen)
        #     for other in balls:
        #         ball.eat(other)


game = Game()
game.run()
