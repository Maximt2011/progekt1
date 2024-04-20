from pygame import *
 
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, img, w, h, speed=0):
        super().__init__()
        self.w = w
        self.h = h
        self.speed = speed
        self.image = transform.scale(image.load(img), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def render(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
 
class Ball(GameSprite):
    def __init__(self, x, y, img, w, h, speed_x, speed_y):
        self.w = w
        self.h = h
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.image = transform.scale(image.load(img), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.directH = 'r'
        self.directV = 'up'     
    def move(self):
        if self.rect.y >= 440:
            self.directV = 'up'
        if self.rect.y <= 10:
            self.directV = 'down'
        if self.directV == 'up':
            self.rect.y -= self.speed_y
        if self.directV == 'down':
            self.rect.y += self.speed_y
        self.rect.x += self.speed_x
 
class Played(GameSprite):
    def moving(self):
        keys = key.get_pressed()
        if keys[K_w]:
            if self.rect.y >= 10:
                self.rect.y -= self.speed
        if keys[K_s]:
            if self.rect.y <= 400:
                self.rect.y += self.speed
    def moving_2(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            if self.rect.y <= 10:
                self.rect.y -= self.speed
        if keys[K_DOWN]:
            if self.rect.y <= 400:
                self.rect.y += self.speed
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
clock = time.Clock()
 
ball = Ball(100, 100, 'ball_png.png', 70, 70, 3, 3)
platform = Played(10, 100, 'platform.png', 75, 100, 5)
platform1 = Played(630, 100, 'platform1.png', 75, 100, 5)
bg = transform.scale(image.load('pole.png'), (700, 500))
 
game = True
 
while game:
    #события

    if sprite.collide_rect(platform, ball):
        ball.speed_x *= -1
    if sprite.collide_rect(platform1, ball):
        ball.speed_x *= -1
    for ev in event.get():
        if ev.type == QUIT:
            game = False
    #Отрисовка
    window.blit(bg, (0, 0))
    ball.render()
    platform.render()
    platform1.render()
    #Вызов методов
    ball.move()
    platform.moving()
    platform1.moving_2()
    display.update()
    clock.tick(60)