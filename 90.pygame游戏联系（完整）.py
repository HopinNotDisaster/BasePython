import random
import sys

import pygame

SIZE = (480, 700)
BORN_ENEMY = pygame.USEREVENT + 1
BORN_PROP = pygame.USEREVENT + 2


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()


class AnimateSpriteMixin:
    def __init__(self, normal_images=None, destroy_images=None, callback=None):
        if destroy_images is None:
            destroy_images = []
        if normal_images is None:
            normal_images = []
        self.normal_index = 0
        self.normal_images = [pygame.image.load(name) for name in normal_images]
        self.destroy_index = 0
        self.destroy_images = [pygame.image.load(name) for name in destroy_images]
        self.callback = callback

    def update_skin(self):
        if self.hp > 0:
            self.image = self.normal_images[self.normal_index // 5]
            self.normal_index += 1
            if self.normal_index == len(self.normal_images) * 5:
                self.normal_index = 0

        else:
            if self.destroy_index < len(self.destroy_images) * 5:
                self.image = self.destroy_images[self.destroy_index // 5]
                self.destroy_index += 1
            elif self.destroy_index == len(self.destroy_images) * 5:
                if self.callback:
                    self.callback()


class EnemySprite(BaseSprite, AnimateSpriteMixin):
    def __init__(self, gm, image, hp, speed, normal_images, destroy_images):
        self.gm = gm
        super().__init__(image)
        AnimateSpriteMixin.__init__(self, normal_images, destroy_images, self.destroy_animate_finish)
        self.hp = self.max_hp = hp
        self.speed = speed
        self.rect.left = random.randint(0, SIZE[0] - self.rect.width)
        self.cd_time = 20

    def destroy_animate_finish(self):
        self.kill()

    def hurt(self):
        self.hp -= 1
        if self.hp <= 0:
            self.gm.player_manage.player.add_score(10)
            self.gm.ui_manage.update_score()

    def fire(self):
        bullet = BulletSprite("plane.images/bullet2.png", self.rect.centerx, self.rect.bottom + 5, -10)
        bullet.add(self.gm.enemy_manage.enemy_bullet_group)

    def fire_cd(self):
        self.cd_time -= 1
        if self.cd_time <= 0:
            self.fire()
            self.cd_time = 10

    def draw_hp(self):
        pygame.draw.rect(self.gm.screen, "pink", (self.rect.left, self.rect.top, self.rect.width, 3))
        pygame.draw.rect(self.gm.screen, "green",
                         (self.rect.left, self.rect.top, self.rect.width * self.hp / self.max_hp, 3))

    def update(self):
        if self.hp > 0:
            self.rect.top += 1
            if self.rect.top > SIZE[1]:
                self.kill()

            self.fire_cd()

            self.draw_hp()

        self.update_skin()


class EnemyManage:
    def __init__(self, gm):
        self.gm = gm
        self.enemy_group = pygame.sprite.Group()
        self.enemy_bullet_group = pygame.sprite.Group()

    def reset(self):
        pygame.time.set_timer(BORN_ENEMY, 3000)

    def clear(self):
        self.enemy_group.empty()
        self.enemy_bullet_group.empty()
        pygame.time.set_timer(BORN_ENEMY, 0)

    def born(self):
        value = random.random()
        if value < 0.5:
            enemy = EnemySprite(self.gm, "plane.images/enemy1.png", 1, 3, ("plane.images/enemy1.png",), (
                "plane.images/enemy1_down1.png", "plane.images/enemy1_down2.png", "plane.images/enemy1_down3.png",
                "plane.images/enemy1_down4.png"))
            enemy.add(self.enemy_group)
        elif value < 0.85:
            enemy = EnemySprite(self.gm, "plane.images/enemy2.png", 3, 7, ("plane.images/enemy2.png",), (
                "plane.images/enemy2_down1.png", "plane.images/enemy2_down2.png", "plane.images/enemy2_down3.png",
                "plane.images/enemy2_down4.png"))
            enemy.add(self.enemy_group)
        # else:
        #     enemy = EnemySprite(self.gm, "plane.images/enemy3_n1.png", 10, 5,
        #                         ("plane.images/enemy3_n1.png", "plane.images/enemy3_n2.png"), (
        #                             "plane.images/enemy3_down1.png",))
        #     enemy.add(self.enemy_group)

    def update(self):
        self.enemy_group.draw(self.gm.screen)
        self.enemy_group.update()
        self.enemy_bullet_group.draw(self.gm.screen)
        self.enemy_bullet_group.update()


class BulletSprite(BaseSprite):
    def __init__(self, image, centerx, centery, speed):
        super().__init__(image)
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.speed = speed

    def update(self):
        self.rect.top -= self.speed
        if self.rect.bottom < 0 or self.rect.top > SIZE[1]:
            self.kill()


class PlayerSprite(BaseSprite, AnimateSpriteMixin):
    def __init__(self, gm, image, center, speed, hp, normal_images, destroy_images):
        self.gm = gm
        super().__init__(image)
        AnimateSpriteMixin.__init__(self, normal_images, destroy_images, self.destroy_animate_finish)
        self.rect.center = center
        self.speed = speed
        self.hp = self.max_hp = hp
        self.player_bullet_group = pygame.sprite.Group()
        self.cd_time = 10
        self.score = 0

    def add_score(self, score):
        self.score += score

    def hurt(self):
        self.hp -= 1

    def destroy_animate_finish(self):
        self.kill()
        self.gm.game_state = "end"
        self.gm.player_manage.clear()
        self.gm.enemy_manage.clear()
        self.score = 0
        self.gm.ui_manage.update_score()

    def fire(self):
        bullet = BulletSprite("plane.images/bullet2.png", self.rect.centerx, self.rect.top - 10, 10)
        bullet.add(self.player_bullet_group)

    def fire_cd(self):
        self.cd_time -= 1
        if self.cd_time <= 0:
            self.fire()
            self.cd_time = 10

    def update_input(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.left -= self.speed
        if key_pressed[pygame.K_RIGHT] and self.rect.right < SIZE[0]:
            self.rect.right += self.speed
        if key_pressed[pygame.K_UP] and self.rect.top > 0:
            self.rect.top -= self.speed
        if key_pressed[pygame.K_DOWN] and self.rect.bottom < SIZE[1]:
            self.rect.bottom += self.speed

    def update_bullet(self):
        self.player_bullet_group.draw(self.gm.screen)
        self.player_bullet_group.update()

    def draw_hp(self):
        pygame.draw.rect(self.gm.screen, "pink", (self.rect.left, self.rect.bottom + 5, self.rect.width, 3))
        pygame.draw.rect(self.gm.screen, "green",
                         (self.rect.left, self.rect.bottom + 5, self.rect.width * self.hp / self.max_hp, 3))

    def update(self):
        self.update_input()
        self.update_bullet()
        self.fire_cd()
        self.update_skin()
        self.draw_hp()


class PlayerManage:
    def __init__(self, gm):
        self.gm = gm
        self.player_group = pygame.sprite.Group()

    def reset(self):
        self.player = PlayerSprite(self.gm, "plane.images/me1.png", (240, 600), 10, 10,
                                   ("plane.images/me1.png", "plane.images/me2.png"), (
                                       "plane.images/me_destroy_2.png", "plane.images/me_destroy_3.png",
                                       "plane.images/me_destroy_4.png"))
        self.player.add(self.player_group)

    def clear(self):
        self.player_group.empty()

    def update(self):
        if self.gm.game_state == "gaming":
            self.player_group.draw(self.gm.screen)
            self.player_group.update()


class UISprite(BaseSprite):
    def __init__(self, image, left, top):
        super().__init__(image)
        self.rect.left = left
        self.rect.top = top

    def has_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        return False


class FontSprite(pygame.sprite.Sprite):
    def __init__(self, text, left, top, color="red", size=20):
        super().__init__()
        self.font = pygame.font.Font("plane.images/font.ttf", size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

    def set_score(self, text):
        self.image = self.font.render(str(text), True, "red")


class UIManage:
    def __init__(self, gm):
        self.gm = gm

        self.ui_ready_group = pygame.sprite.Group()
        self.ui_gaming_group = pygame.sprite.Group()
        self.ui_end_group = pygame.sprite.Group()

        self.start_btn = UISprite("plane.images/start.png", 125, 300)
        self.start_btn.add(self.ui_ready_group)

        self.score_label = FontSprite(f"Score: {0}", 350, 10)
        self.score_label.add(self.ui_gaming_group)

        self.restart_btn = UISprite("plane.images/restart.png", 194, 300)
        self.restart_btn.add(self.ui_end_group)

    def update_score(self):
        self.score_label.set_score(self.gm.player_manage.player.score)

    def check_event(self):
        if self.start_btn.has_click() and self.gm.game_state == "ready":
            self.gm.player_manage.reset()
            self.gm.enemy_manage.reset()
            self.gm.game_state = "gaming"

        elif self.restart_btn.has_click() and self.gm.game_state == "end":
            self.gm.game_state = "ready"

    def update(self):
        if self.gm.game_state == "ready":
            self.ui_ready_group.draw(self.gm.screen)
            self.ui_ready_group.update()
        elif self.gm.game_state == "gaming":
            self.ui_gaming_group.draw(self.gm.screen)
            self.ui_gaming_group.update()
        elif self.gm.game_state == "end":
            self.ui_end_group.draw(self.gm.screen)
            self.ui_end_group.update()


class BGSprite(BaseSprite):
    def __init__(self, image, top=0, speed=0):
        super().__init__(image)
        self.rect.top = top
        self.speed = speed

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > SIZE[1]:
            self.rect.bottom = 0


class BGManage:
    def __init__(self, gm):
        self.gm = gm
        self.bg_ready_group = pygame.sprite.Group()
        self.bg_gaming_group = pygame.sprite.Group()
        self.bg_end_group = pygame.sprite.Group()

        self.ready_bg = BGSprite("plane.images/background.png", )
        self.ready_bg.add(self.bg_ready_group)

        self.gaming_bg1 = BGSprite("plane.images/background.png", speed=2)
        self.gaming_bg2 = BGSprite("plane.images/background2.png", top=SIZE[1], speed=2)
        self.gaming_bg1.add(self.bg_gaming_group)
        self.gaming_bg2.add(self.bg_gaming_group)

        self.end_bg = BGSprite("plane.images/background.png")
        self.end_bg.add(self.bg_end_group)

    def update(self):
        if self.gm.game_state == "ready":
            self.bg_ready_group.draw(self.gm.screen)
            self.bg_ready_group.update()
        elif self.gm.game_state == "gaming":
            self.bg_gaming_group.draw(self.gm.screen)
            self.bg_gaming_group.update()
        elif self.gm.game_state == "end":
            self.bg_end_group.draw(self.gm.screen)
            self.bg_end_group.update()


class GameManage:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("我的游戏")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SIZE)
        self.game_state = "ready"
        self.bg_manage = BGManage(self)
        self.player_manage = PlayerManage(self)
        self.ui_manage = UIManage(self)
        self.enemy_manage = EnemyManage(self)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.ui_manage.check_event()

            if event.type == BORN_ENEMY:
                self.enemy_manage.born()

            if event.type == pygame.KEYUP and event.key == pygame.K_k:
                self.player_manage.player.hp -= 1

    def update_draw(self):
        self.bg_manage.update()
        self.ui_manage.update()
        self.enemy_manage.update()
        self.player_manage.update()

        pygame.display.flip()

    def check_collider(self):
        if hasattr(self.player_manage, "player"):
            # 玩家子弹与敌人子弹都销毁
            pygame.sprite.groupcollide(self.player_manage.player.player_bullet_group,
                                       self.enemy_manage.enemy_bullet_group, True, True)

        # 敌人子弹与玩家
        collider_info = pygame.sprite.groupcollide(self.enemy_manage.enemy_bullet_group,
                                                   self.player_manage.player_group, True, False)
        if collider_info:
            self.player_manage.player.hurt()

        # 玩家子弹与敌人
        if hasattr(self.player_manage, "player"):
            collider_info = pygame.sprite.groupcollide(self.player_manage.player.player_bullet_group,
                                                       self.enemy_manage.enemy_group, True, False)
            for enemys in collider_info.values():
                for enemy in enemys:
                    enemy.hurt()

    def mainloop(self):
        while True:
            self.clock.tick(25)
            self.check_event()
            self.update_draw()
            self.check_collider()


gm = GameManage()
gm.mainloop()
