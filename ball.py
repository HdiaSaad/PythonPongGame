import pygame


class Ball:
    def __init__(self, screen, color, x, y, radius, speed,check_score):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.check_score = check_score

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]

    def check_collision_with_edges(self, width, height,player):
        player_rect = pygame.Rect(player.x, player.y + (height - 40), player.width, player.height)
        ball_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
            #ball hit the player
        if player_rect.colliderect(ball_rect):
            self.speed = (self.speed[0], -self.speed[1])
            pygame.mixer.music.load("assets/touch.mp3")
            pygame.mixer.music.play()
            #print(player.y)
        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.speed = (-self.speed[0], self.speed[1])
            pygame.mixer.music.load("assets/touch.mp3")
            pygame.mixer.music.play()
        if self.y - self.radius < 0 :
            self.speed = (self.speed[0], -self.speed[1])
            pygame.mixer.music.play()
        if self.y + self.radius > height:
            #ball pass the playe
            pygame.mixer.music.unload()
            pygame.mixer.music.load("assets/lose_sound.mp3")
            pygame.mixer.music.play(1)
            self.check_score()