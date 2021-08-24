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
poin = []
keys = ['d', 'f', 'j', 'k']
f_setup = False
#pyautogui.position()
try:
    while True:
        print('Select 4 measure pixels and 1 to choose activation color')
        #set measurepoints
        while not f_setup:
            if keyboard.is_pressed('s'):
                a=a+1
                print('Set '+ str(a) + ' pixels')
                x, y = pag.position()
                pos_x.append(x)
                pos_y.append(y)
                col.append(psc.screenshot().getpixel((x, y)))
                if not keyboard.is_pressed('s'):
                    None
                else:
                    sleep(0.5)
            if keyboard.is_pressed('h'):
                f_setup = True
        dark = col[a-1]
        #game
        while True:
            for i in range(0, 3):
                poin = psc.screenshot().getpixel((pos_x[i], pos_y[i]))
                if poin==dark:
                    keyboard.press(keys[i])
                    print(keys[i] + 'down')
                else:
                    keyboard.release(keys[i])
                    print(keys[i] + 'up')
            sleep(0.3)

except KeyboardInterrupt:
    print(a)
    print(pos_x)
    print(col)
finally:
    None
