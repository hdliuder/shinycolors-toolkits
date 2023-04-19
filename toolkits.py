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
    keyboard.add_hotkey('n', s1)
    keyboard.add_hotkey('g', skip)
    
    keyboard.add_hotkey('q',full)
    keyboard.add_hotkey('w',half2)
    keyboard.add_hotkey('e',dead)

    # keyboard.add_hotkey('m',ml)
    # keyboard.add_hotkey('alt+m',ml_auto)

    keyboard.add_hotkey('a',pingwei1)
    keyboard.add_hotkey('s',pingwei2)
    keyboard.add_hotkey('d',pingwei3)

    keyboard.add_hotkey('b',dao1)
    keyboard.add_hotkey('m',dao3)
    keyboard.add_hotkey(',',autoon)

    keyboard.add_hotkey('r',shijing)
    keyboard.add_hotkey(2,lambda: shijingN(1))
    keyboard.add_hotkey(3,lambda: shijingN(2))
    keyboard.add_hotkey(4,lambda: shijingN(3))
    keyboard.add_hotkey(5,lambda: shijingN(4))
    keyboard.add_hotkey(6,lambda: shijingN(5))
    keyboard.add_hotkey(7,lambda: shijingN(6))
    keyboard.add_hotkey(8,lambda: shijingN(7))
    keyboard.add_hotkey(9,lambda: shijingN(8))
    keyboard.add_hotkey(11,lambda: shijingM(10))

    keyboard.add_hotkey('h',kc1)
    keyboard.add_hotkey('j',kc2)
    keyboard.add_hotkey('k',kc3)
    keyboard.add_hotkey('l',kc4)
    keyboard.add_hotkey(';',kc5)
    keyboard.add_hotkey('\'',kc6)

    keyboard.add_hotkey(75,cc1)
    keyboard.add_hotkey(72,cc2)
    keyboard.add_hotkey(77,cc3)

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

def pingwei1():
    pag.moveTo(200,291)
def pingwei2():
    pag.moveTo(200,529)
def pingwei3():
    pag.moveTo(200,760)

def dao1():
    pag.moveTo(747,960)
    pag.click()
def dao2():
    pag.moveTo(1056,960)
    pag.click()
def dao3():
    pag.moveTo(1366,960)
    pag.click()
def autoon():
    pag.moveTo(1501,126)
    pag.click()

def shijing():
    pag.moveTo(252,699)
    pag.click()

def shijingN(n):
    x,y = pag.position()
    pag.moveTo(1656,512)
    pag.click(clicks=n)
    pag.moveTo(x,y)

def shijingM(n):
    x,y = pag.position()
    pag.moveTo(590,512)
    pag.click(clicks=n)
    pag.moveTo(x,y)

def kc1():
    pag.moveTo(586,726)
    pag.click()
def kc2():
    pag.moveTo(825,726)
    pag.click()
def kc3():
    pag.moveTo(1057,726)
    pag.click()
def kc4():
    pag.moveTo(1226,726)
    pag.click()
def kc5():
    pag.moveTo(1435,726)
    pag.click()
def kc6():
    pag.moveTo(1674,726)
    pag.click()

def cc1():
    pag.moveTo(412,398)
    pag.click()
def cc2():
    pag.moveTo(959,254)
    pag.click()
def cc3():
    pag.moveTo(1492,391)
    pag.click()
print('initing')
signup()
keyboard.add_hotkey('alt+x',unsign)
print('inited')
keyboard.wait('esc')