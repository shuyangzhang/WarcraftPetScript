import keyboard
import subprocess
import time
import threading

is_muted = False

def unmute():
	global is_muted
	if not is_muted: # if mic is already enabled
		print("111")
	else:
		print("222")
	is_muted = not is_muted

def loop():
    iter = 0
    global is_muted
    while True:
        if not is_muted:
            print(iter)
            iter += 1
            time.sleep(0.5)
    
def listener():
    keyboard.add_hotkey("F7", unmute)
    keyboard.wait()

if __name__ == "__main__":
    is_muted = True
    thread1 = threading.Thread(target=listener)
    thread2 = threading.Thread(target=loop)

    thread1.start()
    thread2.start()
    print("all setting has been initialized")