import pyautogui
import time

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

pyautogui.click(x=768, y=358)
pyautogui.write("teste2393@gmail.com")

pyautogui.click(x=817, y=456)
pyautogui.write("senhaço123")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)