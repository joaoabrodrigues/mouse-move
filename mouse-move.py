import pyautogui
import time
from random import randint

pyautogui.FAILSAFE = False

count = 1

while(True) :
    x, y = pyautogui.position()

    x += randint(-3, 3)
    y += randint(-3, 3)

    pyautogui.moveTo(x, y)

    print(f"Mouse moved! {count} times - Current datetime: {time.strftime('%x - %X')}")

    count += 1

    time.sleep(60)
  
