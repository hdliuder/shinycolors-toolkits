# -*- coding: utf-8 -*-
"""
Created on Sun May  8 23:35:59 2022

@author: hf
"""
import cv2
import pyautogui as pag
import PIL,os,keyboard
import numpy as np
from time import sleep

def check_health():
    bg = PIL.ImageGrab.grab(bbox=(960, 0, 1920, 1080))
    rgb = bg.getpixel((10,10))
    rgb2 = bg.getpixel((10,10))
    if rgb == (10,10,10):
        return 'pojia'
    elif rgb2 == (10,10,10):
        return 'dacan'
    else:
        return 'yidixie'

def check_tili():
    pag.moveTo(412,52)
    pag.click()
    # pag.typewrite('baidu.com')
    #pag模块受中文输入法影响,因此选择keyboard模块
    keyboard.write('baidu.com')
    pag.press('enter')
    pag.press('enter')
    sleep(4)
    bg = PIL.ImageGrab.grab(bbox=(960, 0, 1920, 1080))
    rgb = bg.getpixel((10,10))
    if rgb == (10,10,10):
        return 'full'
    else:
        return 'not full'

def check_yingye():
    pag.moveTo(412,52)
    pag.click()
    # pag.typewrite('baidu.com')
    #pag模块受中文输入法影响,因此选择keyboard模块
    keyboard.write('baidu.com')
    pag.press('enter')
    pag.press('enter')
    sleep(4)
    bg = PIL.ImageGrab.grab(bbox=(960, 540, 1920, 1080))
    rgb = bg.getpixel((10,10))
    if rgb == (10,10,10):
        return 'done'
    else:
        return 'not done'
    
if __name__ == '__main__':
    # print(check_health())
    sleep(3)
    check_tili()