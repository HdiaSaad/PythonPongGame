import pygame
import math

class Square:
    width, height = (60,20)
    visible = True
    x = 5
    y = 5

    def __init__(self,width,height,x,y):
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height

    def draw(self,screen):
        pygame.draw.rect(screen,pygame.Color(0,0,0), (self.x,self.y,60,20),0,3)

    def check_collision(self, ball):
        # Calculate the nearest point on the rectangle to the center of the ball
        nearest_x = max(self.x, min(ball.x, self.x + self.width))
        nearest_y = max(self.y, min(ball.y, self.y + self.height))
        
        # Calculate the distance between the nearest point and the center of the ball
        distance_x = ball.x - nearest_x
        distance_y = ball.y - nearest_y
        
        # Calculate the distance
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        
        # Check if the distance is less than or equal to the ball's radius
        return distance <= ball.radius