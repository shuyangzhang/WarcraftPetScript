# coding = utf-8

import win32api
import win32gui
import win32con
import random
import time

str = input(u"请输入你要重复的按键对应的keycode:")
keycode = int(str)

hwnd = win32gui.FindWindow(0,u"魔兽世界")

if hwnd <= 0:
	print(u"魔兽世界未启动，脚本关闭中...")
	time.sleep(5)
	exit(0)
else:
	print(u"已检测到魔兽世界，正在运行脚本，请勿关闭窗口")

	while True:
		win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, keycode, 0)
		time.sleep(float(random.randint(1,200)/100))
		win32api.PostMessage(hwnd, win32con.WM_KEYUP, keycode, 0)

#for i in range(100000000000000):
#	win32api.keybd_event(keycode,0,0,0)
#	time.sleep(float(random.randint(1,200)/100))
#	win32api.keybd_event(keycode,0,win32con.KEYEVENTF_KEYUP,0)


