import pygame

class player:
    width, height = (60,20)
    alive = True
    x = 400
    y = 20
    score = 0
    rect_speed = 5
    touched = False

    def __init__(self,screen,width,height):
        self.score = self.score
        self.x = self.x 
        self.y = self.y 
        self.alive = self.score
        self.window = screen
        self.width = width
        self.height = height
        self.touched = False
    def draw(self,screen):
        if self.x < -60:
            self.x = 690
            pygame.draw.rect(screen,pygame.Color(0,0,0), (self.x,480-21,60,20),0,3)
        elif self.x > 750:
            self.x = 0
            pygame.draw.rect(screen,pygame.Color(0,0,0), (self.x,480-21,60,20),0,3)
        else:
            pygame.draw.rect(screen,pygame.Color(0,0,0), (self.x,480-21,60,20),0,3)

    def update(self,score,row):
        self.score = score
        if row == "left":
            self.x -= 3.2
        elif row == "right":
            self.x += 3.2
    def setTouched(self,val):
        self.touched = val