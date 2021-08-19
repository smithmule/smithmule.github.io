import pygame
from pygame.locals import *
from time import sleep
from random import randrange

pygame.init()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
screen = pygame.display.set_mode((width,height))

difference = pygame.image.load('spot_the_diff.png')
difference = pygame.transform.scale(difference,(width,height))
screen.blit(difference,(0,0))
pygame.display.update()
sleep(randrange(3,15))

scream = pygame.mixer.Sound('scream.wav')
zombie = pygame.image.load('scary_pic')
zombie = pygame.transform.scale(zombie,(width,height))
screen.blit(zombie,(0,0))
pygame.display.update()
scream.play()
sleep(3)

scream.stop()
pygame.quit()