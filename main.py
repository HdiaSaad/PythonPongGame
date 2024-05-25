import pygame
import player
from ball import Ball
from lifebar import Lifebar
from square import Square
import random

class Main:

    
    width, height = (750, 480)
    running = False
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    ball = pygame.Rect(0, 0, 0, 0)
    p = pygame.Rect(0, 0, 0, 0)
    bar = pygame.Rect(0, 0, 0, 0)
    sq = pygame.Rect(0, 0, 0, 0)
    squares =  pygame.Rect(0, 0, 0, 0)
    score = 4
    LevelIsGenerated = False
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Py Game 1.0")
        self.clock = pygame.time.Clock()
        self.bar = Lifebar(self.width)
        self.squares = self.creatLevel()
        self.score = 4

    def check_score(self):
        if self.score <= 1:
            self.pause_game("Game Over")
        else:
            self.score -= 1
            self.bar.updateScore(self.score)
            self.ball = Ball(self.screen, self.RED, random.randint(20, self.width-10), random.randint(20, self.height // 2), 15, (3, 3),self.check_score)

    def pause_game(self,message):
        # Pause the game
        paused = True
        # Font for the message
        font = pygame.font.SysFont(None, 40)
        text = font.render(message, True, self.BLACK)
        text_rect = text.get_rect(center=(self.width//2, self.height//2 - 100))
        # Create restart button
        restart_button = pygame.Rect(self.width//2 - 78, self.height//2 + 50, 160, 50)
        # Create quite button
        quit_button = pygame.Rect(self.width//2 - 78, self.height//2 + 120, 160, 50)
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_button.collidepoint(mouse_pos):
                        paused = False
                        self.ball = Ball(self.screen, self.RED, random.randint(20, self.width-10), random.randint(20, self.height // 2), 15, (3, 3),self.check_score)
                        self.score = 4
                        self.squares = self.g
                        self.bar.updateScore(self.score)
                    if quit_button.collidepoint(mouse_pos):
                        pygame.display.quit()
                        pygame.quit()
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
            # Clear the screen
            self.screen.fill(self.WHITE)
            # Draw message and button
            pygame.draw.rect(self.screen, self.BLACK, restart_button)
            self.screen.blit(text, text_rect)
            restart_text = font.render("RESTART", True, self.WHITE)
            self.screen.blit(restart_text, (self.width//2 - 60, self.height//2 + 65))
            pygame.draw.rect(self.screen, self.BLACK, quit_button)
            quit_text = font.render("QUITER", True, self.WHITE)
            self.screen.blit(quit_text, (self.width//2 - 50, self.height//2 + 135))
            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            pygame.time.Clock().tick(60)
        

    def setRuning(self,runing):
        self.running = runing

    def beforStart(self):
        # Load images
        image1 = pygame.image.load("assets/b_start_3.png")
        image2 = pygame.image.load("assets/b_start_2.png")
        image3 = pygame.image.load("assets/b_start_1.png")
        pygame.mixer.music.load("assets/starting.mp3")
        # Calculate positions to center images
        center_x = self.width // 2
        center_y = self.height // 2
        image1_rect = image1.get_rect(center=(center_x, center_y))
        self.screen.fill("grey")
        # Display images
        self.screen.blit(image1, image1_rect)
        pygame.display.flip()
        pygame.mixer.music.play()
        pygame.time.wait(1000)
        self.screen.blit(image2, image1_rect)
        pygame.display.flip()
        pygame.mixer.music.play()
        pygame.time.wait(1000)
        self.screen.blit(image3, image1_rect)
        pygame.display.flip()
        pygame.mixer.music.play()
        pygame.time.wait(1000)
        self.start()

    def generateLevel(self):
        
        for square in self.squares:
            square.draw(self.screen)
        #pygame.display.flip()

    def creatLevel(self):
        carwat_1 = [Square(60,20,30,30),Square(60,20,100,30),Square(60,20,170,30),Square(60,20,240,30),Square(60,20,310,30),Square(60,20,380,30),Square(60,20,450,30),Square(60,20,520,30),Square(60,20,590,30),Square(60,20,660,30)]
        carwat_2 = [Square(60,20,10,10),Square(60,20,80,10),Square(60,20,150,10),Square(60,20,220,10)]
        return carwat_1
    
    def start(self):
        self.__init__()
        self.p = player.player(self.screen,60,20)
        self.ball = Ball(self.screen, self.RED,random.randint(20, self.width-10), random.randint(20, self.height // 2), 15, (3, 3),self.check_score)
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # Check for key presses
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.p.update(0,"left")
            if keys[pygame.K_RIGHT]:
                self.p.update(0,"right")

            for square in self.squares[:]:  # Use a copy of the list for safe removal
                if square.check_collision(self.ball) & self.p.touched:
                    print("Collision detected!")
                    self.squares.remove(square)  # Remove the square
                    if (len(self.squares) <= 0):
                        print("You Win The Level !")
                        self.uWin()
                    break  # Break to avoid modifying the list during iteration
            self.screen.fill("grey")
            self.ball.move()
            self.ball.check_collision_with_edges(self.width, self.height,self.p,self.p.setTouched)
            # fill the screen with a color to wipe away anything from last frame
            
            self.p.draw(self.screen)
            self.ball.draw()
            self.generateLevel()
            #self.sq.check_collision(self.ball)
            self.screen.blit(self.bar.image, self.bar.rect)
            
            # flip() the display to put your work on screen
            pygame.display.flip()
            self.clock.tick(60)  # limits FPS to 60
        pygame.display.quit()
        pygame.quit()

    def uWin(self):
        # Load images
        Winingimage = pygame.image.load("assets/win.gif")
        pygame.mixer.music.load("assets/Win.wav")
        # Calculate positions to center images
        center_x = self.width // 2
        center_y = self.height // 2
        Winingimage_rect = Winingimage.get_rect(center=(center_x, center_y))
        self.screen.fill("grey")
        # Display images
        self.screen.blit(Winingimage, Winingimage_rect)
        pygame.display.flip()
        pygame.mixer.music.play()
        pygame.time.wait(4000)
        self.start()
    