import mp3play, pygame
pygame.init()

filename = r'D:\Music\AUD-20170321-WA0000.mp3'
clip = mp3play.load(filename)
clip.play()

import time
time.sleep(min(30, clip.seconds()))
clip.stop()

'''import mp3play

filename = r'C:\Documents and Settings\Michael\Desktop\music.mp3'
clip = mp3play.load(filename)

clip.play()

import time
time.sleep(min(30, clip.seconds()))
clip.stop()'''