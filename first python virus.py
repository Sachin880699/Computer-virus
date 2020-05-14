import pyautogui
import os
import webbrowser



for i in range(1,2):
      os.system("gnome-terminal -e 'bash -c \"hollywood; exec bash\"'")

for i in range(10):
      pyautogui.moveTo(100, 100, duration=0.25)
      pyautogui.moveTo(200, 100, duration=0.25)
      