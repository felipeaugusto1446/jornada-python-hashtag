import pyautogui
import time

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)