from pygame import *
from random import randint

win_width = 500
win_height = 700

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, size_x, size_y, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT]:
            self.rect.x += 10
        if keys_pressed[K_LEFT]:
            self.rect.x -= 10

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            Player.lost += 1

background = transform.scale(image.load("fon.jpg"), (win_width, win_height))

player = Player('rocket.png',100, 80, 320,400,10)

window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")

game = True
clock = time.Clock()
FPS = 60
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        player.draw()
        player.update()
        window.blit(background, (0, 0))
        display.update()
    clock.tick(FPS)