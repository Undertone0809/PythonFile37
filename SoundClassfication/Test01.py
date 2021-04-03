import time
import pygame

pygame.init()
print("播放音乐1")
track = pygame.mixer.music.load(r"D:\CloudMusic\A-Lin - 输了你赢了世界又如何 (Live).mp3")

pygame.mixer.music.play()
time.sleep(200)
pygame.mixer.music.stop()