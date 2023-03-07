import pygame 
from random import randint
import time
interval = 0.4
start = 0
pygame.font.init()
font_message = pygame.font.Font(None, 72)
class Counter():
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.lost_enemy = 0
        self.kill_enemy = 0
        self.LEL = self.font.render("пропущенно: " + str(self.lost_enemy), 1, WHITE)
        self.KEL = self.font.render("уничтоженно: " + str(self.kill_enemy), 1, WHITE)

    def c_update(self,window):
        window.blit(self.LEL, (0,10))
        window.blit(self.KEL, (0,50))

    def result(self):
        self.lost_enemy += 1
        self.LEL = self.font.render("пропущенно: " + str(self.lost_enemy), 1, WHITE)
    def kill(self):
        self.kill_enemy += 1
        self.KEL = self.font.render("уничтоженно: " + str(self.kill_enemy), 1, WHITE)


bullets = pygame.sprite.Group()
WZ=(700,500)
FPS = 60
pl_size = (65, 65)
lost_enemy = 0
kill_enemy = 0
WHITE = (255,255,255)
counter = Counter()
window = pygame.display.set_mode(WZ)
pygame.mixer.init()
FS = pygame.mixer.Sound("fire.ogg")
class Gamesprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed, pos_x, pos_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_name), pl_size)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(Gamesprite):
    def update_position(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < WZ[0] - pl_size[0]:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < WZ[1] - pl_size[1]:
            self.rect.y += self.speed


    def fire(self):
        keys = pygame.key.get_pressed()
        new_t = time.time()
        global start
        if keys[pygame.K_SPACE] and new_t - start > interval:
            start = time.time()
            FS.play()
            bullet = Bullet('bullet.png', 5, self.rect.x, self.rect.y)
            bullets.add(bullet)


class Enemy(Gamesprite):
    def __init__(self, image_name, speed, pos_x, pos_y, is_destroy):
        super().__init__(image_name, speed, pos_x, pos_y)
        self.is_destroy = is_destroy

    def update(self):
        global counter
        self.rect.y += self.speed
        if self.rect.y >= WZ[1]:
            self.rect.y = 0
            self.rect.x = randint(0, WZ[0] - pl_size[0])
            self.speed = randint(1, 3)
            if self.is_destroy:
                counter.result()
    
class Bullet(Gamesprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()