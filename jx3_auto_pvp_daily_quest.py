import win32api
import win32con
import win32gui
from ctypes import *
import time
from pynput.keyboard import Key, Listener

SWITCH = True

class POINT(Structure):
    _fields_ = [("x", c_ulong),("y", c_ulong)]

def get_mouse_point():
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    return int(po.x), int(po.y)

def mouse_middle_click(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, x, y, 0, 0)

def loop_toggle(key):
    global SWITCH
    if key == Key.f8:
        SWITCH = not SWITCH

if __name__ == "__main__":
    print("++++++++++++++++++++++++++++++++++++")
    print("++++++ 剑网三全自动矿车任务脚本 ++++")
    print("++++++++ Author： Zhang SY +++++++++")
    print("++ Mail：zhangshuyang@outlook.com ++")
    print("++++++ Release version 1.0.1  ++++++")
    print("++++++++++++ Jan/2 2019 ++++++++++++")
    print("++++++++++++++++++++++++++++++++++++")
    print("")
    print("")
    print("")
    print("请将互动键设置为鼠标中键")
    input("确认请按回车")

    server_name = input("请输入你的服务器名称（默认：唯我独尊）：")
    server_name = server_name if server_name else "唯我独尊"

    server_zone = input("请输入该服务器所在大区（默认：电信五区）：")
    server_zone = server_zone if server_zone else "电信五区"

    game_window_name = "剑网3 - " + server_name + " @ " + server_zone

    hwnd = win32gui.FindWindow(0, game_window_name)

    if hwnd <= 0:
        print("剑网3未启动，脚本关闭中...")
        time.sleep(5)
        exit(0)
    else:
        print("已检测到剑网三，请将窗口切换至剑网三，将鼠标指针悬停在剑网三窗口内")
        print("脚本运行中，请勿关闭此窗口")
        print("按F8可以暂停/继续脚本")

        key_listener = Listener(on_release=loop_toggle)
        key_listener.start()

        while True:
            if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == game_window_name:
                if SWITCH:
                    x, y = get_mouse_point()
                    mouse_middle_click(x, y)
                    print("\r当前状态：执行中", end="")
                else:
                    print("\r当前状态：暂停中", end="")
                time.sleep(0.05)
                # print("已按！")
