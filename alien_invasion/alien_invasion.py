import sys
import pygame
from Settings import Settings
from Ship import Ship
import game_functions as gf
from pygame.sprite import Group
from Alien import Alien

def run_game():
    #初始化游戏创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    bullets = Group()

    #创建一个外星人
    alien = Alien(ai_settings,screen)


    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
       # gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,alien,bullets)

        bullets.update()
        # gf.update_screen(ai_settings,screen,ship,bullets)

        # 删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, alien, bullets)

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环绘制屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()