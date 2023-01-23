import pyautogui
import time
import keyboard

while True:
    pyautogui.moveRel(10, 0, duration=0.25)
    pyautogui.moveRel(0, 10, duration=0.25)
    pyautogui.moveRel(-10, 0, duration=0.25)
    pyautogui.moveRel(0, -10, duration=0.25)
    time.sleep(180) # 3 Minuten
    if keyboard.is_pressed('esc'): # Abbruchtaste
        break 