import keyboard
import win32api
import pyautogui as pag
import pyscreeze as psc
from time import sleep

from win32con import TRUE
from bot import clickB, click, hold, dehold


a = 0
i = 0
x, y = [0, 0]
pos_x = []
pos_y = []
col = []
keys = ['d', 'f', 'j', 'k']
f_setup = False
#pyautogui.position()
try:
    while True:
        #set measurepoints
        while not f_setup:
            if keyboard.is_pressed('s'):
                a=a+1
                x, y = pag.position()
                pos_x.append(x)
                pos_y.append(y)
                col.append(psc.screenshot().getpixel((x, y)))
                if not keyboard.is_pressed('s'):
                    None
                else:
                    sleep(0.5)
            if keyboard.is_pressed('k'):
                f_setup = True
        dark = col[a-1]
        #game
        while True:
            for i in range(0, 3):
                if pag.pixel(pos_x[i], pos_y[i])==dark:
                    keyboard.press(keys[i])
                    print('pressed')
                else:
                    keyboard.release(keys[i])
                    print('released')

except KeyboardInterrupt:
    print(a)
    print(pos_x)
    print(col)
finally:
    None
