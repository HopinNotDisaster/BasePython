import pygame

SIZE = (600, 600)


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, gm):
        super().__init__()
        self.gm = gm
        self.image = pygame.image.load("huohuo.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.centery = 500

        self.my_bullet_group = pygame.sprite.Group()

    def update(self, ) -> None:
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.rect.left -= 2
            if self.rect.left <= 0:
                self.rect.left = 0
        elif key_pressed[pygame.K_RIGHT]:
            self.rect.left += 2
            if self.rect.left >= 500:
                self.rect.left = 500
        self.my_bullet_group.draw(self.gm.screen)
        self.my_bullet_group.update()

    def fire(self):
        # 生成一个子弹 并且加入子弹组
        bullet = self.My_Bullet(self.rect.centerx, self.rect.centery - 50)
        bullet.add(self.my_bullet_group)

    class My_Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("huohuosbullet.png")
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y

        def update(self, ) -> None:
            self.rect.top -= 5
            if self.rect.top == 0:
                self.kill()


class BgSprite(pygame.sprite.Sprite):
    def __init__(self, image, top):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.top = top

    def update(self) -> None:
        self.rect.top -= 2
        if self.rect.top < -SIZE[1]:
            self.rect.top = 600


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SIZE)

        self.bg_group = pygame.sprite.Group()
        self.bg1 = BgSprite("firefly.ico", 0)
        self.bg1.add(self.bg_group)
        self.bg2 = BgSprite("Type-C.png", 600)
        self.bg2.add(self.bg_group)

        self.player_group = pygame.sprite.Group()
        self.player1 = PlayerSprite(self)
        self.player1.add(self.player_group)

        self.run()

    def run(self):
        while 1:
            self.clock.tick(50)
            for e in pygame.event.get():
                if e.type == 256:
                    pygame.quit()
                    exit()
                if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                    self.player1.fire()

            self.draw()

    def draw(self):
        self.bg_group.draw(self.screen)
        self.bg_group.update()
        self.player_group.draw(self.screen)
        self.player_group.update()

        pygame.display.flip()


game = Game()
