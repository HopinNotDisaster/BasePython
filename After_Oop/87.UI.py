"""
1.
2.
3.
"""

import pygame
import _plane

SIZE = (480, 700)


class Util:
    @staticmethod
    def check_click(sprite):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            return sprite.rect.collidepoint(mouse_pos)


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()


class UISprite(BaseSprite):
    def __init__(self, image, left, top):
        super().__init__(image)
        self.rect.left = left
        self.rect.top = top


class UIManage:
    """
    管理三个ui——group
    """

    def __init__(self, gm, plane_game):
        self.gm = gm

        self.plane_game = plane_game
        self.ui_ready_group = pygame.sprite.Group()
        bg_ui = UISprite("plane.images/background.png", 0, 0)
        bg_ui.add(self.ui_ready_group)
        self.begin_btn = UISprite("plane.images/start.png", 150, 400)
        self.begin_btn.add(self.ui_ready_group)

        self.ui_gaming_group = pygame.sprite.Group()
        # bg1 = UISprite("plane/images/background.png", 0, 3)
        # bg1.add(self.ui_gaming_group)
        # bg2 = BGSprite("plane/images/background2.png", SIZE[1], 3)
        # bg2.add(self.ui_gaming_group)
        # score_label = LabelSprite(f"Score: {100}", (420, 30))
        # score_label.add(self.ui_gaming_group)

        self.ui_end_group = pygame.sprite.Group()
        # bg = UISprite("plane/images/background.png", 0, 0)
        # bg.add(self.ui_end_group)
        self.restart_btn = UISprite("plane.images/restart.png", 150, 600)
        self.restart_btn.add(self.ui_end_group)

    def update(self):
        if self.gm.game_state == "ready":
            print("ready")
            self.ui_ready_group.draw(self.gm.screen)
            self.ui_ready_group.update()
            # 检测鼠标是否点击了开始
            if Util.check_click(self.begin_btn):
                self.gm.game_state = "gaming"


        elif self.gm.game_state == "gaming":
            # print("gaming................")
            #
            # self.ui_gaming_group.draw(self.gm.screen)
            # self.ui_gaming_group.update()
            self.plane_game.run()

        elif self.gm.game_state == "end":
            print("end")

            self.ui_end_group.draw(self.gm.screen)
            self.ui_end_group.update()

            if Util.check_click(self.restart_btn):
                self.gm.game_state = "ready"


class GameManage:
    def __init__(self, plane_game):
        pygame.init()
        self.plane_game = plane_game
        self.screen = pygame.display.set_mode(SIZE)

        self.game_state = "ready"
        self.ui_m = UIManage(self, plane_game)

    def check_event(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            elif e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                self.game_state = "end"

    def draw(self):
        self.ui_m.update()
        pygame.display.flip()

    def run(self):
        while 1:
            self.check_event()
            self.draw()


plane_game = _plane.GameManage()
gm = GameManage(plane_game)
gm.run()
