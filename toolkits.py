import pyautogui as pag
import keyboard,os
import time
import ex
import timer
import get_info


jing = 1
pag.PAUSE = 0.01



def typein():
    pag.PAUSE = 0.1
    pag.moveTo(412,52)
    pag.click()
    pag.hotkey('ctrl','a')
    pag.typewrite(r'https://shinycolors.enza.fun/produce/?a=')
    pag.press('enter')
    pag.press('enter')
    pag.PAUSE = 0.01
    
def typein2():
    pag.PAUSE = 0.1
    pag.moveTo(412,52)
    pag.click()
    pag.hotkey('ctrl','a')
    pag.typewrite(r'https://shinycolors.enza.fun/produce/?a=#')
    pag.press('enter')
    pag.press('enter')
    pag.PAUSE = 0.01
    
def typein0():
    time.sleep(0.4)
    pag.moveTo(412,52)
    pag.click(clicks=3)
    
    pag.typewrite(r'https://shinycolors.enza.fun/produce/?a=')
    pag.press('enter')
    pag.press('enter')
    time.sleep(1)
    pag.click()
    pag.press('right')
    pag.typewrite(r'#')
    pag.press('enter')
    pag.press('enter')
    pag.PAUSE = 0.01
    
def print_position():
    print(pag.position())

def switch():
    global jing
    if jing ==1:
        pag.hotkey('alt','left')
        jing = 0
    else:
        pag.hotkey('alt','right')
        jing = 1
    pag.moveTo(318,845)
    time.sleep(0.1)
def clicking():
    while keyboard.is_pressed('z'):
        pag.click()
def go_da():
    pag.moveTo(448,698)
    pag.click()
    pag.moveTo(806,765)
def learn():
    x,y = pag.position()
    pag.moveTo(1670,963)
    pag.click()
    time.sleep(0.05)
    pag.moveTo(1095,785)
    pag.click()
    pag.moveTo(x,y)

def full():
    pag.click()
    timer.delay(1.250)
    pag.click()
def half2():
    pag.click()
    timer.delay(1.170)
    pag.click()
def dead():
    pag.click()
    print('a')
    timer.delay(1.050)
    pag.click()
    print('v')
def auto_chudao():
    health = get_info.check_health()
    if health == '':
        full()
    elif health == '':
        half2()
    elif health == '':
        dead()
    else:
        print('?')

def ml(copyed=False):
    if copyed == False:
        pag.moveTo(412,52)
        pag.click()
        pag.hotkey('ctrl','a')
        pag.hotkey('ctrl','c')

    pag.moveTo(1670,963)
    pag.click()

    time.sleep(4)
    pag.moveTo(412,52)
    pag.click()
    pag.hotkey('ctrl','a')
    pag.hotkey('ctrl','v')
    pag.hotkey('enter')
def ml_auto():
    timer.delay(1)
    pag.moveTo(412,52)
    pag.click()
    pag.hotkey('ctrl','a')
    pag.hotkey('ctrl','c')
    while(1):
        ml(True)
        time.sleep(60*30)

def signup():
    keyboard.add_hotkey('alt+x',unsign)
    
    keyboard.add_hotkey('alt+l',ex.run)
    keyboard.add_hotkey('alt+1', typein0)
    # keyboard.add_hotkey('alt+2', typein2)
    keyboard.add_hotkey('p', print_position)
    keyboard.add_hotkey('z', clicking)
    keyboard.add_hotkey('x', switch)
    keyboard.add_hotkey('c', go_da)
    keyboard.add_hotkey('v', learn)
    keyboard.add_hotkey('b', s1)
    keyboard.add_hotkey('g', skip)
    
    keyboard.add_hotkey('q',full)
    keyboard.add_hotkey('w',half2)
    keyboard.add_hotkey('e',dead)

    keyboard.add_hotkey('m',ml)
    keyboard.add_hotkey('alt+m',ml_auto)
def unsign():
    keyboard.unhook_all_hotkeys()
    keyboard.add_hotkey('alt+z',signup)
    print('unsigned')
    
def s1():
    pag.moveTo(990,926)
    pag.click()
def skip():
    pag.moveTo(1722,146)
    pag.click()

def make_cake():
    return

def check_yingye():
    return 

def re_yingye():
    return

print('initing')
signup()
keyboard.add_hotkey('alt+x',unsign)
print('inited')
keyboard.wait('esc')