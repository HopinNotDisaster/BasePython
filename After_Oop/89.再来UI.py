import pygame

SIZE = (480, 700)


class LabelSprite(pygame.sprite.Sprite):
    def __init__(self, text, center, size=20):
        super().__init__()
        font = pygame.font.Font("plane.images/font.ttf", size=size)
        self.image = font.render(text, True, "blue")
        self.rect = self.image.get_rect()
        self.rect.center = center


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()


class PlayerSprite(BaseSprite):
    def __init__(self, gm, images, die_images=(), center=(240, 600)):
        super().__init__(images[0])
        self.gm = gm

        # self.cur_die_show = -1
        self.hp = self.max_hp = 5
        self.images = [pygame.image.load(_) for _ in images]  # 仅仅是存储的！
        # self.die_images = [pygame.image.load(i) for i in die_images]  # 仅仅是存储的！
        self.cur_skin = -1
        self.rect.center = center
        self.speed = 10
        # 玩家的子弹管理对象
        # self.fire_cd = 25
        # self.super_bullet_count = 0
        # self.bullet_m = BulletManage(gm)

    # def hp_show(self):
    #     if self.hp > 0:
    #         pygame.draw.rect(gm.screen, "red", (self.rect.left, self.rect.top - 10, self.rect.width, 5))
    #         pygame.draw.rect(gm.screen, "green",
    #                          (self.rect.left, self.rect.top - 10, self.rect.width * self.hp / self.max_hp, 5))

    # def hurt(self):
    #     self.hp -= 1
    #     if self.hp <= 0:
    #         # exit()
    #         pass

    # def fire(self):
    #     bullet_center = (self.rect.centerx, self.rect.top)
    #     BulletSprite("87.bullet.png", bullet_center, 12).add(self.bullet_m.bullet_group)
    #     if self.super_bullet_count:
    #         bullet_center = (self.rect.centerx + 50, self.rect.top)
    #         BulletSprite("87.bullet.png", bullet_center, 12).add(self.bullet_m.bullet_group)
    #         bullet_center = (self.rect.centerx - 50, self.rect.top)
    #         BulletSprite("87.bullet.png", bullet_center, 12).add(self.bullet_m.bullet_group)
    #         self.super_bullet_count -= 1

    def change_form(self):
        if self.hp > 0:
            # 玩家换肤皮！
            self.cur_skin += 1
            self.cur_skin %= len(self.images) * 100
            self.image = self.images[self.cur_skin // 100]

    def move(self):
        # 玩家移动！
        key_pressed = pygame.key.get_pressed()  # 按着的键！！！
        if key_pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.left -= self.speed
        elif key_pressed[pygame.K_RIGHT] and self.rect.right < SIZE[0]:
            self.rect.left += self.speed
        elif key_pressed[pygame.K_UP] and self.rect.top > 0:
            self.rect.top -= self.speed
        elif key_pressed[pygame.K_DOWN] and self.rect.bottom < SIZE[1]:
            self.rect.bottom += self.speed

    def update(self, ) -> None:
        self.change_form()
        self.move()
    # # 死亡特效
    # if self.hp <= 0:
    #     self.cur_die_show += 1
    #     self.image = self.die_images[(self.cur_die_show % (len(self.die_images) * 20)) // 20]
    #
    #     if self.cur_die_show > len(self.die_images) * 20 + 1:
    #         self.kill()
    #         exit()
    # self.hp_show()
    # if self.hp > 0:
    #     # 玩家自动开火！
    #     self.fire_cd -= 1
    #     if self.fire_cd < 0:
    #         self.fire()
    #         self.fire_cd = 25


class PlayerManage:
    def __init__(self, gm, ):
        self.gm = gm

        self.player_group = pygame.sprite.Group()

    def reset_player(self):
        self.player = PlayerSprite(gm, ("plane.images\\me1.png ",), )
        self.player.add(self.player_group)

    def clear(self):
        self.player_group.empty()

    def update(self):
        self.player_group.draw(self.gm.screen)
        self.player_group.update()


class UiSprite(BaseSprite):
    def __init__(self, image, left=0, top=0):
        super().__init__(image)
        # ui图标一定是在指定top的居中位置！
        self.rect.left = (SIZE[0] - self.rect.width) // 2
        self.rect.top = top

    def is_clicked(self, ):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return 1
        else:
            return 0

    def update(self):
        pass


class UiManage:
    def __init__(self, gm):
        self.gm = gm
        bg_ui = UiSprite("plane.images/background.png", 0, 0)

        # 添加开始的UI
        self.ready_group = pygame.sprite.Group()
        bg_ui.add(self.ready_group)
        self.begin_btn = UiSprite("plane.images/start.png", 125, 100)
        self.begin_btn.add(self.ready_group)
        # 添加进行的UI
        self.gaming_group = pygame.sprite.Group()
        bg_ui.add(self.gaming_group)

        self.score_label = LabelSprite(f"Score: {100}", (350, 30))
        self.score_label.add(self.gaming_group)
        # 添加结束的UI
        self.end_group = pygame.sprite.Group()
        bg_ui.add(self.end_group)
        # bg = UISprite("plane/images/background.png", 0, 0)
        # bg.add(self.ui_end_group)
        self.restart_btn = UiSprite("plane.images/restart.png", 150, 100)
        self.restart_btn.add(self.end_group)

    def check_click(self):
        if self.gm.game_state == "ready" and self.begin_btn.is_clicked():
            self.gm.game_state = "gaming"
            self.gm.player_m.reset_player()

        elif self.gm.game_state == "end" and self.restart_btn.is_clicked():
            self.gm.game_state = "ready"

    def update(self):
        if self.gm.game_state == "ready":
            # print("ready")
            self.ready_group.draw(self.gm.screen)
            self.ready_group.update()
            # 检测鼠标是否点击了开始

            # if Util.check_click(self.begin_btn):
            #     self.gm.game_state = "gaming"


        elif self.gm.game_state == "gaming":
            # print("gaming................")
            self.gaming_group.draw(self.gm.screen)
            self.gaming_group.update()
            # self.plane_game.run()

        elif self.gm.game_state == "end":
            # print("end")

            self.end_group.draw(self.gm.screen)
            self.end_group.update()

            # if Util.check_click(self.restart_btn):
            #     self.gm.game_state = "ready"


class GameManage:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("再来一次UI")
        self.clock = pygame.time.Clock()

        self.game_state = "ready"

        self.ui_m = UiManage(self)
        self.player_m = PlayerManage(self)

    def check_event(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            elif e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                self.ui_m.check_click()
            elif e.type == pygame.KEYUP and e.key == pygame.K_k:
                print("k")
                self.game_state = "end"
                self.player_m.clear()

    def draw(self):
        self.ui_m.update()
        self.player_m.update()
        pygame.display.flip()

    def mainloop(self):
        while 1:
            self.clock.tick(50)
            self.check_event()
            self.draw()


gm = GameManage()
gm.mainloop()
