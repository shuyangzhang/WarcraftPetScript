import autopy
from pynput.keyboard import Key, Listener
import winsound

SWITCH = False

def on_release(key):
    global SWITCH

    if key == Key.f8:
        if SWITCH:
            winsound.Beep(600, 300)
        else:
            winsound.Beep(2000, 300)
        SWITCH = not SWITCH

if __name__ == "__main__":
    print("diablo auto t16 entrance program is running")
    print("press F8 to toggle the switch")
    print("author: Zhang SY")
    print("mail: zhangshuyang@outlook.com")
    print("release version 1.0.0")
    print("May 26th, 2019")
    key_listener = Listener(on_release=on_release)
    key_listener.start()

    while True:
        if SWITCH:
            autopy.mouse.click()
        else:
            pass