import pygame

class Lifebar:
    def __init__(self, width):
        super().__init__()
        self.image = pygame.image.load("assets/lifebar3.png")  # Load player image
        self.image = pygame.transform.scale(self.image, (125, 22))  # Scale image to new width
        self.rect = self.image.get_rect()  # Get rect object representing image dimensions and position
        self.rect.center = (width - 70, 15)  # Set initial position of player

    def updateScore(self,score):
        if(score == 4):
            self.image = pygame.image.load("assets/lifebar3.png")  # Load player image
        elif(score == 3):
            self.image = pygame.image.load("assets/lifebar2.png")  # Load player image
        elif(score == 2):
            self.image = pygame.image.load("assets/lifebar1.png")  # Load player image
        elif(score == 1):
            self.image = pygame.image.load("assets/lifebar.png")  # Load player image