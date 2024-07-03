import pygame
pygame.init()

pygame.mixer.music.load('exercicio21.mp3')

pygame.mixer.music.play()

input()

pygame.event.wait()