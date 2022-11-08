#pip install pyautogui
import pyautogui as pag


#if u have error  use this '  pip install pyautogui   '


import random
import time

while True:
    x = random.randint(0,1280); #x cordinate
    y = random.randint(0,1024); #y cordinate
    pag.moveTo(x,y,0.9) # move 'X' and 'Y', 0.9 - this speed..
    time.sleep(0.1)
