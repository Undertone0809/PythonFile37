# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 13:31
# @Author  : Zeeland
# @File    : 播放音乐.py
# @Software: PyCharm
import time
import pygame

pygame.init()
print("播放音乐1")
track = pygame.mixer.music.load(r"D:\CloudMusic\A-Lin - 输了你赢了世界又如何 (Live).mp3")

pygame.mixer.music.play()
time.sleep(30)
pygame.mixer.music.stop()