#pip install pyautogui
import pyautogui as pag
import random
import time

while True:
    x = random.randint(0,1280);
    y = random.randint(0,1024);
    pag.moveTo(x,y,0.9)
    time.sleep(0.1)
