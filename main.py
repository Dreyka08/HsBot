import pyautogui
import time
from ctypes import *
import datetime
import os


X_SIZE = 1052
Y_SIZE = 712


def mach(_c):
    d = _c
    for x in pyautogui.getAllWindows():
        if x.title == "Hearthstone":
            x.restore()
            pyautogui.press('f4')
            windll.user32.BlockInput(True)
            x.moveTo(150, 100)

            x.resizeTo(X_SIZE, Y_SIZE)
            _x, _y = x.topleft

            # fight3(_x, _y, x.width, x.height, 2)
            pyautogui.click(_x + (80 / 752) * x.width, _y + (254 / 508) * x.height)
            time.sleep(0.5)
            pyautogui.click(_x + (200 / 752) * x.width, _y + (200 / 508) * x.height)
            time.sleep(0.5)
            pyautogui.click(_x + (600 / 752) * x.width, _y + (400 / 508) * x.height)
            time.sleep(3)
            pyautogui.click(_x + (575 / 752) * x.width, _y + (430 / 508) * x.height)
            time.sleep(0.5)
            pyautogui.click(_x + (300 / 752) * x.width, _y + (300 / 508) * x.height)
            time.sleep(5)

            for k in range(4):
                doi = 0
                print(d, " ", d * 168)
                d = d + 1
                for j in range(3):
                    if k == 3:
                        pyautogui.click(_x + (600 / 752) * x.width, _y + (400 / 508) * x.height)
                        time.sleep(1)
                    else:
                        pyautogui.click(_x + j * 90 + (150 / 752) * x.width, _y + (250 / 508) * x.height)
                        time.sleep(1)
                        pyautogui.click(_x + (600 / 752) * x.width, _y + (400 / 508) * x.height)
                        time.sleep(1)
                windll.user32.BlockInput(False)
                # x.minimize()
                tic = time.perf_counter()
                f_last = 0
                while 1:
                    tok = time.perf_counter()
                    d = (tok - tic) / 60
                    f = round((d % 1) * 60 - ((d % 1) * 60 % 0.1))
                    u = 60
                    if f != f_last:
                        print(round(d - (d % 1)), ":", f)
                        f_last = f
                    if (tok - tic > 15 * u) & (doi == 0):
                        x.restore()
                        pyautogui.press('f4')
                        windll.user32.BlockInput(True)
                        x.moveTo(150, 100)
                        x.resizeTo(X_SIZE, Y_SIZE)
                        doi = 1
                        time.sleep(0.5)
                        pyautogui.click(_x + (650 / 752) * x.width, _y + (240 / 508) * x.height)
                        # x.minimize()
                        windll.user32.BlockInput(False)
                    if tok - tic > 30 * u:
                        x.restore()
                        pyautogui.press('f4')
                        windll.user32.BlockInput(True)
                        x.moveTo(150, 100)
                        x.resizeTo(X_SIZE, Y_SIZE)
                        fight3(_x, _y, x.width, x.height, k)
                        time.sleep(12)
                        if k == 3:
                            now = datetime.datetime.now()
                            try:
                                os.mkdir("D:\\SC\\" + str(now.day) + "." + str(now.month))
                            except:
                                pass
                            im = pyautogui.screenshot(region=(_x, _y, x.width, x.height))
                            path = "D:\\SC\\" + str(now.day) + "." + str(now.month) + "\\" + str(now.day) + "." + str(
                                now.hour) + "." + str(now.minute) + "." + str(now.second) + ".png"
                            im.save(path)
                            time.sleep(5)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(1)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(1)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(12)
                            pyautogui.click(_x + (375 / 752) * x.width, _y + (175 / 508) * x.height)
                            time.sleep(1)
                            pyautogui.click(_x + (275 / 752) * x.width, _y + (385 / 508) * x.height)
                            time.sleep(1)
                            pyautogui.click(_x + (510 / 752) * x.width, _y + (385 / 508) * x.height)
                            time.sleep(1)
                            pyautogui.click(_x + (392 / 752) * x.width, _y + (307 / 508) * x.height)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(6)
                            pyautogui.click(_x + (392 / 752) * x.width, _y + (420 / 508) * x.height)
                            time.sleep(3)
                            break
                        else:
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(1)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(1)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(8)
                            pyautogui.click(_x + (285 / 752) * x.width, _y + (254 / 508) * x.height)
                            time.sleep(1)
                            pyautogui.click(_x + (410 / 752) * x.width, _y + (437 / 508) * x.height)
                            time.sleep(5)
                            break
    return d


def fight3(x, y, x_size, y_size, k):
    for i in range(3):
        pyautogui.moveTo(x + 410, y + 325)
        if k == 3:
            pyautogui.dragTo(x + 500, y + 200, 0.2, button='left')
        else:
            pyautogui.dragTo(x + 430, y + 200, 0.2, button='left')
        time.sleep(1)
    pyautogui.click(x + (650 / 752) * x_size, y + (240 / 508) * y_size)
    time.sleep(16)
    if k != 3:
        now = datetime.datetime.now()
        try:
            os.mkdir("D:\\SC\\" + str(now.day) + "." + str(now.month))
        except:
            pass
        im = pyautogui.screenshot(region=(x, y, x_size, y_size))

        path = "D:\\SC\\" + str(now.day) + "." + str(now.month) + "\\" + str(now.day) + "." + str(now.hour) + "." +\
               str(now.minute) + "." + str(now.second) + ".png"
        im.save(path)
    fight1(x, y, x_size, y_size)
    time.sleep(5)
    return 0


def fight1(x, y, x_size, y_size):
    for i in range(3):
        pyautogui.moveTo(x + 410, y + 325)
        pyautogui.dragTo(x + 520, y + 200, 0.2, button='left')
        time.sleep(1)
    pyautogui.click(x + (650 / 752) * x_size, y + (240 / 508) * y_size)
    return 0


if __name__ == "__main__":
    Count = 0
    Pts = 0
    while 1:
        Count = mach(Count)
        Pts = Pts + Count * 168
        print(Count, " ", Pts)
        time.sleep(2)
