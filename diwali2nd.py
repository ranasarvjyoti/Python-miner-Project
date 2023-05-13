import pygame
import random

pygame.init()
display=pygame.display.set_mode((1000,600))
clock=pygame.time.Clock()
FPS=90

class Firework():
    def __init__(self):
        self.x=random.randint(0,1000)
        self.velocity=random.uniform(3.5,7)

    def move(self):
        self.y-=self.velocity

    def draw(self):
        a=[self.x,int(self.y+15)]
        b=[self.x,int(self.y-15)]
        pygame.draw.line(display,(128,128,128),a,b,4)

def game():
    fireworks=[Firework()]
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        display.fill((0,0,0))
        
        for firework in fireworks:
            firework.move()
            firework.draw()
        pygame.display.update()
        clock.tick(FPS)

game()
pygame.quit()