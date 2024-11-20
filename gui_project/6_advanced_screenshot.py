import os
import time
from PIL import ImageGrab
from pynput import keyboard

#! 윈도우 확인 > Screenshot saved as ~ Desktop/image_20241120_162237.png
def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    save_path = os.path.expanduser(f"~/Desktop/image{curr_time}.png")  # 바탕화면에 저장
    img = ImageGrab.grab()
    img.save(save_path)
    print(f"Screenshot saved as {save_path}")

def on_press(key):
    try:
        if key.char == 'f':  # 'f' 키를 눌렀을 때
            screenshot()
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
