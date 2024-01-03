import pyautogui as pg
import time


def promtion():
    def endPromotion():
        steps = 1
        pg.click(197, 19, button="left")
        for i in range(50):
            i = +1
            if steps == 1:
                yes = pg.locateCenterOnScreen(
                    "resources/promotion/yes.png", confidence=0.7
                )
                try:
                    if len(yes) > 1:
                        steps = steps + 1
                        print(steps)
                except:
                    pg.hotkey("ctrl", "b")
                    steps = 1

            elif steps == 2:
                unapprove = pg.locateCenterOnScreen(
                    "resources/promotion/unapprove.png", confidence=0.8
                )
                yes = pg.locateCenterOnScreen(
                    "resources/promotion/yes.png", confidence=0.8
                )
                time.sleep(0.5)
                pg.leftClick(unapprove)
                time.sleep(0.5)
                pg.press("f8")
                pg.leftClick(yes)
                pg.press("n")
                pg.press("enter")
                pg.press("f10")
                steps = steps + 1

            elif steps == 3:
                time.sleep(0.5)
                approve = pg.locateCenterOnScreen(
                    "resources/promotion/approve.png", confidence=0.8
                )
                pg.leftClick(approve)
                time.sleep(0.5)
                pg.hotkey("ctrl", "b")
                steps = 1

    endPromotion()


promtion()
