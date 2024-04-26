import random
import sys
import pygame


# 游戏状态 ready 未开始  gameing  游戏中 end 游戏结束


class Util:
    """
    工具类： 提供静态方法
    """

    @staticmethod
    def click_check(sprite):
        """
        精灵的点击检测
        """
        if pygame.mouse.get_pressed()[0]:
            if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False


class BaseSprite(pygame.sprite.Sprite):
    """
    精灵父类
    """

    def __init__(self, name):
        super().__init__()
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()


class FoodSprite(BaseSprite):
    """
    食物类
    """

    def __init__(self, name, center):
        super().__init__(name)
        self.rect.center = center


class AudioManage:
    @staticmethod
    def play_bg_music():
        """
        背景音乐
        """
        pygame.mixer.music.load("sound/bgm.wav")
        pygame.mixer.music.play(True)

    @staticmethod
    def play_sound(name):
        """
        音效
        """
        sound = pygame.mixer.Sound(name)
        sound.play()


class FoodManage:
    def __init__(self, gm):
        self.gm = gm
        self.food_group = pygame.sprite.Group()

    def generate(self):
        """
        生成食物
        """
        name = "img/food.png" if random.random() > 0.5 else "img/food2.png"
        center = (random.randrange(25, 575, 25), random.randrange(25, 575, 25))
        FoodSprite(name, center).add(self.food_group)

    def clear(self):
        # 玩家死亡清除食物
        self.food_group.empty()

    def update(self):
        self.food_group.update()
        self.food_group.draw(self.gm.screen)


class PlayerSprite(BaseSprite):
    """
    玩家精灵
    """

    def __init__(self, name, center, is_head=False, type=0):
        super().__init__(name)
        self.type = type
        self.rect.center = center
        self.is_head = is_head
        if is_head:
            # 如果是舌头 则 加载四张对应的surface
            self.image_left = self.image
            self.image_up = pygame.image.load("img/up.png")
            self.image_right = pygame.image.load("img/right.png")
            self.image_down = pygame.image.load("img/down.png")


class PlayerManage:
    def __init__(self, gm):
        self.gm = gm
        self.count = 2
        self.player_group = pygame.sprite.Group()
        self.score = 0
        AudioManage.play_bg_music()

    def eat(self):
        # 在末尾右侧追加一个
        print("吃到了")
        self.last = PlayerSprite("img/body.png", self.last.rect.center)
        self.last.add(self.player_group)
        self.score += 1
        AudioManage.play_sound("sound/eat.mp3")

    def move(self, dir):
        if self.move_dir == "left" and dir == "right" or self.move_dir == "up" and dir == "down" or self.move_dir == "right" and dir == "left" or self.move_dir == "down" and dir == "up":
            return

        self.move_dir = dir
        # 更新每一个部件的位置  倒着更新
        for index in range(len(self.player_group) - 1, 0, -1):
            self.player_group.sprites()[index].rect.center = self.player_group.sprites()[index - 1].rect.center
        if self.move_dir == "left":
            self.head.rect.centerx -= 25
            self.head.image = self.head.image_left
        elif self.move_dir == "up":
            self.head.rect.centery -= 25
            self.head.image = self.head.image_up
        elif self.move_dir == "down":
            self.head.rect.centery += 25
            self.head.image = self.head.image_down
        elif self.move_dir == "right":
            self.head.rect.centerx += 25
            self.head.image = self.head.image_right

        if pygame.sprite.spritecollide(self.head, self.gm.food_manage.food_group, True):
            self.eat()
            self.gm.food_manage.generate()

        if self.head.rect.centerx <= 0 or self.head.rect.centerx >= 600 or self.head.rect.centery <= 0 or self.head.rect.centery >= 600:
            self.die()

        coll = pygame.sprite.groupcollide(self.player_group, self.player_group, False, False)
        # if len(coll[]) > 1:
        #     print("自己吃到自己了")
        for i, j in coll.items():  # 1 是食物
            if i.is_head and len(j) == 2:
                print("自己吃到自己了")
                self.die()

        # print(i, type(i), i.is_head)
        # print(j)

    def born(self):
        self.move_dir = "left"
        self.score = 0
        # 蛇头
        self.head = PlayerSprite("img/left.png", (300, 300), True, )
        self.head.add(self.player_group)

        for i in range(1, 4):
            self.last = PlayerSprite("img/body.png", (300 + 25 * i, 300))
            self.last.add(self.player_group)

        pygame.time.set_timer(6888, 500)

    def die(self):
        """
        玩家死亡  清空 停止计时 停止自动移动
        """
        self.player_group.empty()
        self.gm.state = "end"
        pygame.time.set_timer(6888, 0)
        AudioManage.play_sound("sound/die.wav")
        self.gm.food_manage.clear()

    def update(self):
        self.player_group.update()
        self.player_group.draw(self.gm.screen)


class UISprite(BaseSprite):
    """
    UI精灵类
    """

    def __init__(self, name, center):
        super().__init__(name)
        self.rect.center = center


class UIManage:
    def __init__(self, gm):
        self.gm = gm
        # UI字体
        self.font = pygame.font.Font("font/font.ttf", 32)

        # 开始前UI元素
        self.ready_group = pygame.sprite.Group()
        self.begin_btn = UISprite("img/begin_btn.png", (300, 300))
        self.begin_btn.add(self.ready_group)

        # 游戏中UI元素
        self.score_surface = self.font.render(f"Score:{self.gm.player_manage.score}", True, "#FF4500")

        # 游戏结束UI元素
        self.end_group = pygame.sprite.Group()
        self.replay_btn = UISprite("img/replay_btn.png", (300, 300))
        self.replay_btn.add(self.end_group)

    def update(self):
        if self.gm.state == "ready":
            # print("更新未开始游戏UI")
            self.ready_group.draw(self.gm.screen)
            if Util.click_check(self.begin_btn):
                AudioManage.play_sound("sound/click.mp3")
                self.gm.state = "gaming"
                self.gm.player_manage.born()
                self.gm.food_manage.generate()
        elif self.gm.state == "gaming":
            # print("更新游戏中UI")
            self.score_surface = self.font.render(f"Score:{self.gm.player_manage.score}", True, "#FF4500")
            self.gm.screen.blit(self.score_surface, (400, 20))
        elif self.gm.state == "end":
            # print("更新游戏结束UI")
            self.end_group.draw(self.gm.screen)
            if Util.click_check(self.replay_btn):
                AudioManage.play_sound("sound/click.mp3")
                self.gm.state = "gaming"
                self.gm.player_manage.born()
                self.gm.food_manage.generate()


class GameManage:
    def __init__(self, name):
        pygame.init()
        # 初始化游戏状态
        self.state = "ready"

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption(name)

        # 游戏中的玩家
        self.player_manage = PlayerManage(self)

        # 食物管理类
        self.food_manage = FoodManage(self)

        # 构建了一个 UI管理类的实例
        self.ui_manage = UIManage(self)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 自动移动
            if event.type == 6888:
                self.player_manage.move(self.player_manage.move_dir)

            # 手动换方向
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player_manage.move("left")
                elif event.key == pygame.K_UP:
                    self.player_manage.move("up")
                elif event.key == pygame.K_RIGHT:
                    self.player_manage.move("right")
                elif event.key == pygame.K_DOWN:
                    self.player_manage.move("down")

            # 测试功能 一键杀死  一键吃
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.state = "end"
                    self.player_manage.die()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.player_manage.eat()

    def run(self):
        while True:
            self.clock.tick(24)
            self.check_event()
            self.screen.fill("#FFFACD")
            self.ui_manage.update()

            if self.state == "gaming":
                self.player_manage.update()
                self.food_manage.update()

            pygame.display.flip()


gm = GameManage("贪吃蛇大作战")
gm.run()
