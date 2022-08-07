import pyautogui
import time


def mach():
    for x in pyautogui.getAllWindows():
        if x.title == "Hearthstone":
            x.restore()
            _x, _y = x.topleft

            time.sleep(2)
            pyautogui.click(_x + (200 / 752) * x.width, _y + (200 / 508) * x.height)
            time.sleep(2)
            pyautogui.click(_x + (600 / 752) * x.width, _y + (400 / 508) * x.height)
            time.sleep(3)
            pyautogui.click(_x + (575 / 752) * x.width, _y + (430 / 508) * x.height)
            time.sleep(2)
            pyautogui.click(_x + (300 / 752) * x.width, _y + (300 / 508) * x.height)
            pyautogui.click(_x + (300 / 752) * x.width, _y + (300 / 508) * x.height)
            time.sleep(5)
            for k in range(4):
                doi = 0
                print(k)
                for j in range(3):
                    if k == 3:
                        pyautogui.click(_x + (600 / 752) * x.width, _y + (400 / 508) * x.height)
                        time.sleep(2)
                    else:
                        pyautogui.click(_x + j * 90 + (150 / 752) * x.width, _y + (250 / 508) * x.height)
                        time.sleep(3)
                        pyautogui.click(_x + (600 / 752) * x.width, _y + (400 / 508) * x.height)
                        time.sleep(3)
                x.minimize()
                tic = time.perf_counter()
                while 1:
                    tok = time.perf_counter()
                    d = (tok - tic) / 60
                    print(round(d - (d % 1)), ":", round((d % 1) * 60 - ((d % 1) * 60 % 0.1)))
                    if (tok - tic > 20 + 60 * (6 * (k + 1))) & (doi == 0):
                        x.restore()
                        doi = 1
                        pyautogui.click(_x + (650 / 752) * x.width, _y + (240 / 508) * x.height)
                        x.minimize()
                    if tok - tic > 20 + 60 * (6 * (k + 2)):
                        x.restore()
                        fight3(_x, _y, x.width, x.height)
                        time.sleep(8)
                        if k == 3:
                            time.sleep(10)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(3)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(3)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(12)
                            pyautogui.click(_x + (375 / 752) * x.width, _y + (175 / 508) * x.height)
                            time.sleep(3)
                            pyautogui.click(_x + (275 / 752) * x.width, _y + (385 / 508) * x.height)
                            time.sleep(3)
                            pyautogui.click(_x + (510 / 752) * x.width, _y + (385 / 508) * x.height)
                            time.sleep(3)
                            pyautogui.click(_x + (392 / 752) * x.width, _y + (307 / 508) * x.height)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(8)
                            pyautogui.click(_x + (392 / 752) * x.width, _y + (420 / 508) * x.height)
                            time.sleep(3)
                            break
                        else:
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(2)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(2)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            pyautogui.click(_x + (400 / 752) * x.width, _y + (300 / 508) * x.height)
                            time.sleep(8)
                            pyautogui.click(_x + (275 / 752) * x.width, _y + (254 / 508) * x.height)
                            time.sleep(2)
                            pyautogui.click(_x + (410 / 752) * x.width, _y + (437 / 508) * x.height)
                            time.sleep(10)
                            break
    return 0


def fight3(x, y, xsize, ysize):
    for i in range(3):
        pyautogui.moveTo(x + 350, y + 290)
        pyautogui.dragTo(x + 400, y + 200, 0.2, button='left')
        time.sleep(1)
    pyautogui.click(x + (650 / 752) * xsize, y + (240 / 508) * ysize)
    time.sleep(16)
    fight1(x, y, xsize, ysize)
    return 0


def fight1(x, y, xsize, ysize):
    for i in range(3):
        pyautogui.moveTo(x + 350, y + 290)
        pyautogui.dragTo(x + 450, y + 200, 0.2, button='left')
        time.sleep(1)
    pyautogui.click(x + (650 / 752) * xsize, y + (240 / 508) * ysize)
    return 0


if __name__ == "__main__":
    while 1:
        mach()
        time.sleep(6)
