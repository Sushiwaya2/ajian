import pygame
import random
import tkinter as tk
from tkinter import messagebox
# 游戏设置
WIDTH = 800
HEIGHT = 600
FPS = 60

# 定义颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 初始化Pygame和创建窗口
pygame.init()
pygame.mixer.init()  # 初始化混音器模块
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 加载并播放背景音乐
pygame.mixer.music.load(r'D:\vscode\跑酷\2\111.mp3')
pygame.mixer.music.play(loops=-1)  # 循环播放

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'D:\vscode\跑酷\2\13.jpg')  # 加载图像
        self.image = pygame.transform.scale(self.image, (50, 50))  # 调整图像大小
        self.rect = self.image.get_rect()
        self.rect.center = (60, HEIGHT / 2)

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'D:\vscode\跑酷\2\12.jpg')  # 加载图像
        self.image = pygame.transform.scale(self.image, (50, random.randrange(50, 100)))  # 调整图像大小
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        self.rect.x = random.randrange(WIDTH + 40, WIDTH + 100)
        self.speedx = random.randrange(-8, -1)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.rect.y = random.randrange(HEIGHT - self.rect.height)
            self.rect.x = random.randrange(WIDTH + 40, WIDTH + 100)
            self.speedx = random.randrange(-8, -1)

all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    o = Obstacle()
    all_sprites.add(o)
    obstacles.add(o)

# 游戏循环
running = True
game_over = False
while running:
    if game_over:
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        play_again = messagebox.askyesno("亲爱的阿坚", "你被我逮捕啦！！！")
        if play_again:
            all_sprites = pygame.sprite.Group()
            obstacles = pygame.sprite.Group()
            player = Player()
            all_sprites.add(player)
            for i in range(8):
                o = Obstacle()
                all_sprites.add(o)
                obstacles.add(o)
            game_over = False
        else:
            running = False
        root.destroy()  # 销毁窗口
    else:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, obstacles, False)
        if hits:
            game_over = True

        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()

pygame.quit()