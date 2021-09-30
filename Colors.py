import random
num = random.randrange(3, 10)
print (num)
import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("random circles")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen

while True:#GAME LOOP
        for x in range(750):
            pygame.draw.ellipse(screen, (random.randrange(0,255),random.randrange(0, 255),random.randrange(0,255)), (x,400,50,50))

        pygame.display.flip()

pygame.quit()
