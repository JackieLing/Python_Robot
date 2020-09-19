# 【Python项目】外星人入侵~

# 作者：Code_Linghu-令狐

# 1、Windows系统中安装Pygame

## 1.1检查python环境是否安装成功

- 打开 **CMD**命令行输入

```xml
python 
```

| 执行成功的截图，说明python安装成功！                         |
| ------------------------------------------------------------ |
| ![](https://cdn.jsdelivr.net/gh/JackieLing/mage1/img/20200830165919.png) |

- 如果你没有安装python环境和开发工具则打开如下链接：

大家按照如下教程，安装实验环境
1、python3.7安装

https://www.cnblogs.com/djtang/articles/13320959.html

2、pycharm安装
https://www.cnblogs.com/temari/p/13048977.html

## 1.2pip install whell

**CMD**命令行键入：

```xml
pip install whell
```

| 执行成功如图：                                               |
| ------------------------------------------------------------ |
| ![](https://cdn.jsdelivr.net/gh/JackieLing/mage1/img/20200830171240.png) |

## 1.3安装pygame

- 点击https://www.lfd.uci.edu/~gohlke/pythonlibs/安装对应的pygame包
- 小哥找到的对应的包版本为 **pygame-1.9.3-cp37-cp37m-win_amd64.whl** 下载

| 小哥根据自己安装的python环境来选择对应版本的pygame包版本     |
| ------------------------------------------------------------ |
| ![](https://cdn.jsdelivr.net/gh/JackieLing/mage1/img/20200830172504.png) |

- 下载成功之后，我们首先为本次游戏项目新建一个项目**文件夹**，取名 `alien_invasion`,然后将上面下载成功的**pygame包**放到这个文件夹内！

|                                                              |
| ------------------------------------------------------------ |
| ![](https://cdn.jsdelivr.net/gh/JackieLing/mage1/img/20200830172819.png) |

- 打开CMD命令，首先进入到这个项目文件夹目录下，然后对应下图输入：

|                                                              |
| ------------------------------------------------------------ |
| ![](https://cdn.jsdelivr.net/gh/JackieLing/mage1/img/20200830173142.png) |

# 2、开始游戏项目

## 2.1新建一个alien_invasion文件

```python
import sys
import pygame

def run_game():
    #初始化游戏创建一个屏幕对象
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

- 我们这一步创建的是一个游戏窗口及用户交互界面

| 游戏界面窗口：                                               |
| ------------------------------------------------------------ |
| ![](https://cdn.jsdelivr.net/gh/JackieLing/mage1/img/20200830174306.png) |

## 2.2设置背景颜色

```python
import sys
import pygame

def run_game():
    #初始化游戏创建一个屏幕对象
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    #设置背景颜色
    bg_color=(230,230,230)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

         #每次循环绘制屏幕
        screen.fill(bg_color)

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

| 改变颜色后的界面：                                           |
| ------------------------------------------------------------ |
| ![](https://cdn.jsdelivr.net/gh/JackieLing/mage1/img/20200830174739.png) |

## 2.3创建设置类

**settings.py**

```python
class Settings():
    """存储《外星人入侵》的所有设置类"""

    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

```

**alien_invasion.py**

```python
import sys
import pygame
from Settings import Settings

def run_game():
    #初始化游戏创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")



    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

         #每次循环绘制屏幕
        screen.fill(ai_settings.bg_color)

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

## 2.4添加飞船图像

- 在项目目录下新建一个文件夹 `images`，存入素材图片：

|                                                              |
| ------------------------------------------------------------ |
| ![](https://cdn.jsdelivr.net/gh/JackieLing/mage1/img/20200831201129.png) |

## 2.5创建ship类

```python
import pygame

class Ship():
    def __init__(self):
        self.screen=screen

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx

```

## 2.6在屏幕上绘制飞船

```python
import pygame

class Ship():
    def __init__(self,screen):
        self.screen=screen

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image,self.rect)
```

# 3、重构：模块game_functions

## 3.1函数check_events（）

**game_functions.py**:

```python
import sys
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            
```

## 3.2函数update_screen()

```python
def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
```

# 4、驾驶飞船

## 4.1响应按键

```python
import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.rect.centerx +=1

def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
```

```python
import sys
import pygame
from Settings import Settings
from Ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship=Ship(screen)

    #开始游戏的主循环
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings,screen,ship)

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

         #每次循环绘制屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

## 4.2允许不断移动

```python
import pygame

class Ship():
    def __init__(self,screen):
        self.screen = screen

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
    def blitme(self):
        self.screen.blit(self.image,self.rect)
```

```python
import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False


def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
```

```python
import sys
import pygame
from Settings import Settings
from Ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship=Ship(screen)

    #开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

         #每次循环绘制屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

## 4.3左右移动

```python
import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center=float(self.rect.centerx)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx=self.center
    def blitme(self):
        self.screen.blit(self.image,self.rect)
```

```python
import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
```

## 4.4调整飞船速度

**setings.py**：

```python
class Settings():
    """存储《外星人入侵》的所有设置类"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5

```

```python
import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center=float(self.rect.centerx)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx=self.center
    def blitme(self):
        self.screen.blit(self.image,self.rect)
```

**alien_invasion.py**

```python
import sys
import pygame
from Settings import Settings
from Ship import Ship
import game_functions as gf

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

    #开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

         #每次循环绘制屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

## 4.5限制飞船活动范围

```python
import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center=float(self.rect.centerx)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx=self.center
    def blitme(self):
        self.screen.blit(self.image,self.rect)
```

## 4.6重构check_events()

```python
import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()


def check_keydown_events(event,ship):
    """"响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


```

# 5.射击

## 5.1添加子弹设置

```python
class Settings():
    """存储《外星人入侵》的所有设置类"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60

```

## 5.2创建Bullet类

**bullet.py**

```python
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen

        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
                              ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
```

## 5.3将子弹存储在编组中

**alien_invasion.py**

```python
import sys
import pygame
from Settings import Settings
from Ship import Ship
import game_functions as gf
from pygame.sprite import Group

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
    bullets=Group()

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

         #每次循环绘制屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

## 5.4射击

**game_functions.py**

```python
import sys
import pygame
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """"响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key ==  pygame.K_SPACE:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


```

## 5.5删除已经消失的子弹

**alien_invasion.py**

```python
import sys
import pygame
from Settings import Settings
from Ship import Ship
import game_functions as gf
from pygame.sprite import Group

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
    bullets=Group()

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
       # gf.update_screen(ai_settings,screen,ship,bullets)

        #删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings,screen,ship,bullets)

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

         #每次循环绘制屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

## 5.6限制子弹数量

```python
import sys
import pygame
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """"响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key ==  pygame.K_SPACE:
        if len(bullets)<ai_settings.bullets_allowed:
             new_bullet = Bullet(ai_settings,screen,ship)
             bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


```

## 5.7创建函数update_bullets()

```python
import sys
import pygame
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """"响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key ==  pygame.K_SPACE:
        if len(bullets)<ai_settings.bullets_allowed:
             new_bullet = Bullet(ai_settings,screen,ship)
             bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

```

# 6、外星人

## 6.1创建第一个外星人

**Alien.py**

```python
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

def blitme(self):
    self.screen.blit(self.image,self.rect)

```

**alien_invasion.py**

```python
import sys
import pygame
from Settings import Settings
from Ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

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
    bullets=Group()

    #创建一个外星人
    alien = Alien(ai_settings,screen)


    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()

        gf.update_screen(ai_settings,screen,ship,alien,bullets)
        bullets.update()
       # gf.update_screen(ai_settings,screen,ship,bullets)

        #删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings,screen,ship,bullets)

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

         #每次循环绘制屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```



