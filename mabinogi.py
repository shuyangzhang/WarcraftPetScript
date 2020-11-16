import win32api
import win32gui
import win32con
import random
import time

input_string = input("keycode to repeat:")
keycode = int(input_string) if input_string else 112

window_title = input("window title:")
title = window_title if window_title else "Mabinogi"
hwnd = win32gui.FindWindow(0, title)

interval_time = input("interval time(ms):")
interval_time = int(interval_time) if interval_time else 1000

lower_interval_time = interval_time - 1000 if interval_time > 1000 else 0
higher_interval_time = interval_time + 1000 if interval_time > (0-1000) else 0

if hwnd <= 0:
	print("Cannot detect the window, closing...")
	time.sleep(5)
	exit(0)
else:
	print("Window detected, starting...")

	while True:
		win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, keycode, 0)
		time.sleep(float(random.randint(100, 400) / 1000))
		win32api.PostMessage(hwnd, win32con.WM_KEYUP, keycode, 0)
                time.sleep(float(random.randint(lower_interval_time, higher_interval_time) / 1000))



