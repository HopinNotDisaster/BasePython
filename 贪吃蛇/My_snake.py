from typing import Any

import pygame

SIZE = (400, 600)
DICT = {
    "U": "img/up.png",
    "L": "img/left.png",
    "D": "img/down.png",
    "R": "img/right.png",
    "N": "img/body.png"
}


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, is_head, center):
        super().__init__()
        self.image = pygame.image.load(DICT[is_head])
        self.rect = self.image.get_rect()
        self.rect.center = center

    def move(self):





    def update(self, *args: Any, **kwargs: Any) -> None:
        pass



class UiSprite(pygame.sprite.Sprite):
    def __init__(self, image, center=(SIZE[0] // 2, SIZE[0] // 2)):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self, *args: Any, **kwargs: Any) -> None:
        pass


class UiManage:
    def __init__(self, gm):
        self.gm = gm
        self.bg_group = pygame.sprite.Group()
        UiSprite("img/bg.png").add(self.bg_group)

        self.ready_group = pygame.sprite.Group()
        self.begin_btn = UiSprite("img/begin_btn.jpg")
        self.begin_btn.add(self.ready_group)

        self.gaming_group = pygame.sprite.Group()

        self.end_group = pygame.sprite.Group()
        self.end_btn = UiSprite("img/replay_btn.png")
        self.end_btn.add(self.end_group)

    @staticmethod
    def click_check(sprite):
        """
        精灵的点击检测
        """
        if pygame.mouse.get_pressed()[0]:
            if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False

    def update(self):
        self.bg_group.update()
        self.bg_group.draw(gm.screen)
        if gm.game_state == "ready":
            self.ready_group.update()
            self.ready_group.draw(gm.screen)
            if UiManage.click_check(self.begin_btn):
                self.gm.game_state = "gaming"
        elif gm.game_state == "gaming":
            print("gaming")

        else:
            self.end_group.update()
            self.end_group.draw(gm.screen)
            if UiManage.click_check(self.end_btn):
                self.gm.game_state = "ready"


class GameManage:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("从零开始的贪吃蛇世界！")

        self.game_state = "ready"
        self.ui_m = UiManage(self)

    def draw(self):
        self.ui_m.update()
        pygame.display.flip()

    def check_event(self):
        for e in pygame.event.get():
            # print(e.type)
            if e.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            elif e.type == pygame.KEYUP and e.key == pygame.K_r:
                self.game_state = "end"

    def run(self):
        while 1:
            self.check_event()
            self.draw()


gm = GameManage()
gm.run()
