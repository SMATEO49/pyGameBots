from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def hold(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)


def dehold(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def clickB(button):
    keyboard.press(button)
    sleep(0.05)
    keyboard.release(button)

#pyautogui.displayMousePosition()


