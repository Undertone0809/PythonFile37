from pymouse import *
from pykeyboard import *
import time
import pyperclip


def send_message1(context, count):
    mouse = PyMouse()
    k = PyKeyboard()
    time.sleep(2)  # 给你两秒时间让你把光标停留在消息界面
    for i in range(count):
        mylocalx, mylocaly = mouse.position()
        temp = context + str(count - i + 1)
        k.type_string(temp)
        k.tap_key(k.enter_key, 1)
        time.sleep(0.1)
        print(mylocalx, mylocaly)

#使用ctrl+v
def send_message2(context, count):
    mouse = PyMouse()
    k = PyKeyboard()
    time.sleep(2)  # 给你两秒时间让你把光标停留在消息界面
    for i in range(count):
        mylocalx, mylocaly = mouse.position()
        temp = context + str(count - i) + '秒'
        pyperclip.copy(temp)
        k.press_key(k.control_key)
        k.tap_key('v')
        k.release_key(k.control_key)
        k.tap_key(k.enter_key, 1)
        time.sleep(1)
        print(mylocalx, mylocaly)


if __name__ == '__main__':
    send_message2("睡觉倒计时:", 10)
