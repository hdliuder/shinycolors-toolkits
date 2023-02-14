# -*- coding: utf-8 -*-
"""
Created on Sun May  8 23:35:59 2022

@author: hf
"""
import cv2
import pyautogui as pag
import PIL,os
import numpy as np
from time import sleep

def fanwei(pt,anle):
    for i in anle:
        if abs(i[0] - pt[0]) < 10 and abs(i[1] - pt[1]) < 10:
            return False
    return True

def find_ex_up():
    img = cv2.imread('a.png', 0)
    img2 = cv2.imread('aa.png', 0)
    
    bg = PIL.ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    bg = bg.crop((0,0,1300,1080))
    bg.save('b.png')
    bg = cv2.imread('b.png', 0)
    # h, w = img.shape[:2]  # rows->h, cols->w
    
    method = cv2.TM_CCOEFF_NORMED
    res = cv2.matchTemplate(img, bg, method)
    res2= cv2.matchTemplate(img2, bg, method)
    threshold = 0.9
    loc = np.where(res >= threshold)
    loc2 = np.where(res2 >= threshold)

    locs = (np.concatenate((loc,loc2),axis=1))

    
    anle = []
    for pt in zip(*locs[::-1]):  # *号表示可选参数
        if fanwei(pt,anle) == True:
            pag.click(pt[0],pt[1])
            anle.append((pt[0],pt[1]))
        # print(anle)
        pag.click(1425,969)
        sleep(0.1)
    os.remove('b.png')
        
def scroll():
    pag.moveTo(400,700)
    pag.click(400,700)
    pag.dragRel(0,-475,0.15)
    pag.click(400,700)

def run(n=100):
    for i in range(n):
        find_ex_up()
        scroll()

if __name__ == '__main__':
    find_ex_up()