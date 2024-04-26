import random

import pygame

SIZE = (600, 900)
BORN = pygame.USEREVENT + 100
SUPPLY_BORN = pygame.USEREVENT + 101


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image):
        """
        只负责渲染图片！
        """
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()


class BgSprite(BaseSprite):
    def __init__(self, iamge, top):
        super().__init__(iamge)
        self.rect.top = top

    def update(self) -> None:
        self.rect.bottom -= 3
        if self.rect.bottom < 0:
            self.rect.top = SIZE[1]


class BgManage:
    def __init__(self, gm):
        self.gm = gm

        self.bg_group = pygame.sprite.Group()

        self.bg_sprite1 = BgSprite("87.bg1.jpg", 0)
        self.bg_sprite1.add(self.bg_group)
        self.bg_sprite2 = BgSprite("87.bg2.jpg", SIZE[1])
        self.bg_sprite2.add(self.bg_group)

    def update(self):
        """
        仅更新绘制！
        :return: None
        """
        self.bg_group.draw(self.gm.screen)
        self.bg_group.update()


class BulletSprite(BaseSprite):
    def __init__(self, image, pos, speed):
        super().__init__(image)
        self.rect.center = pos
        self.speed = speed

    def update(self, ) -> None:
        self.rect.top -= self.speed
        if self.rect.bottom < 0 or self.rect.top > SIZE[1]:
            self.kill()


class BulletManage:
    def __init__(self, gm):
        self.gm = gm
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.bullet_group.draw(self.gm.screen)
        self.bullet_group.update()


class PlayerSprite(BaseSprite):
    def __init__(self, gm, iamges: tuple, die_images, center):
        super().__init__(iamges[0])

        self.gm = gm
        self.cur_die_show = -1
        self.hp = self.max_hp = 5
        self.images = (pygame.image.load(iamges[0]), pygame.image.load(iamges[1]))  # 仅仅是存储的！
        self.die_images = [pygame.image.load(i) for i in die_images]  # 仅仅是存储的！

        self.image = self.images[0]  # 要展示的
        self.cur_skin = 0

        self.rect = self.images[0].get_rect()
        self.rect.center = center

        self.speed = 5

        # 玩家的子弹管理对象
        self.fire_cd = 25
        self.super_bullet_count = 0
        self.bullet_m = BulletManage(gm)

    def hp_show(self):
        if self.hp > 0:
            pygame.draw.rect(gm.screen, "red", (self.rect.left, self.rect.top - 10, self.rect.width, 5))
            pygame.draw.rect(gm.screen, "green",
                             (self.rect.left, self.rect.top - 10, self.rect.width * self.hp / self.max_hp, 5))

    def hurt(self):
        self.hp -= 1
        if self.hp <= 0:
            # exit()
            pass

    def fire(self):
        bullet_center = (self.rect.centerx, self.rect.top)
        BulletSprite("87.bullet.png", bullet_center, 12).add(self.bullet_m.bullet_group)
        if self.super_bullet_count:
            bullet_center = (self.rect.centerx + 50, self.rect.top)
            BulletSprite("87.bullet.png", bullet_center, 12).add(self.bullet_m.bullet_group)
            bullet_center = (self.rect.centerx - 50, self.rect.top)
            BulletSprite("87.bullet.png", bullet_center, 12).add(self.bullet_m.bullet_group)
            self.super_bullet_count -= 1

    def update(self, ) -> None:
        # 死亡特效
        if self.hp <= 0:
            self.cur_die_show += 1
            self.image = self.die_images[(self.cur_die_show % (len(self.die_images) * 20)) // 20]

            if self.cur_die_show > len(self.die_images) * 20 + 1:
                self.kill()
                exit()
        self.hp_show()
        if self.hp > 0:
            # 玩家自动开火！
            self.fire_cd -= 1
            if self.fire_cd < 0:
                self.fire()
                self.fire_cd = 25
            # 玩家换肤皮！
            self.cur_skin += 1
            self.cur_skin %= 100
            self.image = self.images[self.cur_skin // 50]
            # 玩家移动！
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_LEFT]:
                self.rect.left -= self.speed
                if self.rect.left <= 0:
                    self.rect.left = 0
            elif key_pressed[pygame.K_RIGHT]:
                self.rect.left += self.speed
                if self.rect.left >= SIZE[0] - 60:
                    self.rect.left = SIZE[0] - 60


class PlayerManage:
    def __init__(self, gm, ):
        self.gm = gm

        self.player_group = pygame.sprite.Group()

        self.player = PlayerSprite(gm, ("87.player_skin1.png", "87.player_skin2.png"),
                                   ("plane.images/me_destroy_2.png",
                                    "plane.images/me_destroy_3.png",
                                    "plane.images/me_destroy_4.png"),
                                   (SIZE[0] // 2, SIZE[1] - 100))
        self.player.add(self.player_group)

    def update(self):
        self.player_group.draw(self.gm.screen)
        self.player_group.update()


class EnemySprite(BaseSprite):
    def __init__(self, gm, images, die_images, speed, hp):
        super().__init__(images[0])
        self.cur_skin = 0
        self.gm = gm
        self.images = [pygame.image.load(i) for i in images]
        self.die_images = [pygame.image.load(i) for i in die_images]
        self.speed = speed
        self.hp = hp
        self.max_hp = hp
        self.rect.left = random.randint(0, SIZE[0] - self.rect.width)

        self.cur_die_show = 0
        self.fire_cd = 40

    def hp_show(self):
        if self.hp > 0:
            pygame.draw.rect(gm.screen, "red", (self.rect.left, self.rect.top - 10, self.rect.width, 5))
            pygame.draw.rect(gm.screen, "green",
                             (self.rect.left, self.rect.top - 10, self.rect.width * self.hp / self.max_hp, 5))

    def hurt(self):
        if self.hp > 0:
            self.hp -= 1
        if self.hp <= 0:
            pass

    def fire(self):
        bullet_center = (self.rect.centerx, self.rect.bottom)
        BulletSprite("87.bullet.png", bullet_center, -8).add(self.gm.enemy_m.bullet_group)

    def draw_skin(self):
        if self.hp > 0:
            self.cur_skin += 1
            self.image = self.images[self.cur_skin % len(self.images)]
        if self.hp <= 0:
            self.cur_die_show += 1
            self.image = self.die_images[(self.cur_die_show % (len(self.die_images) * 10)) // 10]
            if self.cur_die_show > len(self.die_images) * 10 + 1:
                self.kill()

    def update(self, ) -> None:
        self.draw_skin()
        if self.hp > 0:
            # 敌方的移动
            self.rect.top += self.speed
            if self.rect.top > SIZE[1]:
                self.kill()
            # 敌方的开火
            self.fire_cd -= 1
            if self.fire_cd < 0:
                self.fire_cd = 40
                self.fire()
            self.hp_show()


class EnemyManage:
    def __init__(self, gm):
        self.gm = gm
        self.enemy_group = pygame.sprite.Group()
        pygame.time.set_timer(BORN, 2000)

        # 敌方的全部子弹管理实例
        self.bullet_group = pygame.sprite.Group()

    def born(self):
        value = random.random()
        if value < 0.5:
            enemy1 = EnemySprite(gm, ("plane.images/enemy1.png",),
                                 ("plane.images/enemy1_down1.png",
                                  "plane.images/enemy1_down2.png",
                                  "plane.images/enemy1_down3.png",
                                  "plane.images/enemy1_down4.png"), 3, 2)
            enemy1.add(self.enemy_group)
        elif value < 0.9:
            enemy2 = EnemySprite(gm, ("plane.images/enemy2.png",),
                                 ("plane.images/enemy2_down1.png",
                                  "plane.images/enemy2_down2.png",
                                  "plane.images/enemy2_down3.png",
                                  "plane.images/enemy2_down4.png"), 4, 3)
            enemy2.add(self.enemy_group)
        else:
            enemy3 = EnemySprite(gm, ("plane.images/enemy3_n1.png", "plane.images/enemy3_n2.png"),
                                 ("plane.images/enemy3_down5.png",
                                  "plane.images/enemy3_down5.png",
                                  "plane.images/enemy3_down6.png",
                                  "plane.images/enemy3_down6.png"), 2, 5)
            enemy3.add(self.enemy_group)

    def born_b(self):
        self.enemy_b = EnemySprite(gm, ("87.b_enemy.jpg",), (), 5, 1000)
        self.enemy_b.add(self.enemy_group)

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_5]:
            self.gm.enemy_m.born_b()
        self.enemy_group.draw(self.gm.screen)
        self.enemy_group.update()
        self.bullet_group.draw(self.gm.screen)
        self.bullet_group.update()


class PropSprite(BaseSprite):
    def __init__(self, image, p_type):
        super().__init__(image)
        self.rect.left = random.randint(0, SIZE[0] - self.rect.width)

        self.p_type = p_type

    def update(self):
        self.rect.top += 5
        if self.rect.top > SIZE[1]:
            self.kill()
        self.rect.left += random.randint(-5, 5)


class PropManage:
    def __init__(self, gm):
        self.gm = gm
        self.prop_group = pygame.sprite.Group()

        pygame.time.set_timer(SUPPLY_BORN, 2000)

    def bron(self):
        value = random.random()
        if value > 0.5:
            prop2 = PropSprite("plane.images/bomb_supply.png", 2)
            prop2.add(self.prop_group)
        else:
            prop1 = PropSprite("plane.images/bullet_supply.png", 1)
            prop1.add(self.prop_group)

    def update(self):
        # for e in pygame.event.get():
        #     if e.type == SUPPLY_BORN:
        #         self.bron()
        self.prop_group.draw(self.gm.screen)
        self.prop_group.update()


class GameManage:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SIZE)

        self.bg_m = BgManage(self)
        self.player_m = PlayerManage(self)
        self.enemy_m = EnemyManage(self)
        self.prop_m = PropManage(self)
        # self.player_group = pygame.sprite.Group()
        # self.player1 = PlayerSprite(self, ".\\image\\huohuo.jpg", 300, 300)

    def run(self):
        while 1:
            self.clock.tick(50)
            self.check_event()
            self.check_collide()
            self.draw()

    def draw(self):
        self.bg_m.update()
        self.player_m.update()
        self.enemy_m.update()
        self.player_m.player.bullet_m.update()
        self.enemy_m.bullet_group.update()
        self.prop_m.update()
        pygame.display.flip()

    def check_collide(self):
        # 玩家子弹与敌人飞机碰撞检测 销毁玩家子弹 敌人掉血
        collider_info = pygame.sprite.groupcollide(self.player_m.player.bullet_m.bullet_group, self.enemy_m.enemy_group,
                                                   True,
                                                   False)
        for enemys in collider_info.values():
            for enemy in enemys:
                enemy.hurt()
        # 敌人子弹与玩家碰撞
        collider_info = pygame.sprite.spritecollide(self.player_m.player, self.enemy_m.bullet_group, True)
        if collider_info:
            self.player_m.player.hurt()

        # 子弹与子弹碰撞
        # pygame.sprite.groupcollide(self.player_m.player.bullet_m.bullet_group, self.enemy_m.bullet_group, True, True)

        # 玩家与敌人碰撞检测
        # collider_info = pygame.sprite.groupcollide(self.player_m.player_group, self.enemy_m.enemy_group, False, False)
        # if collider_info:
        #     pygame.quit()
        #     exit()

        # # 玩家与道具碰撞检测
        # collider_info = pygame.sprite.groupcollide(self.player_m.player_group, self.prop_m.prop_group, False, True)
        # for pros in collider_info.values():
        #     for prop in pros:
        #         if prop.p_type == 1:
        #             self.player_m.player.super_bullet_count = 5
        #         if prop.p_type == 2:
        #             self.enemy_m.enemy_group.empty()

    def check_event(self):
        for e in pygame.event.get():
            if e.type == 256:
                pygame.quit()
                exit()
            elif e.type == BORN:
                self.enemy_m.born()
            elif e.type == SUPPLY_BORN:
                self.prop_m.bron()
            # 按住空格开火！
            # elif e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
            #     self.player_m.player.fire()


gm = GameManage()
gm.run()
