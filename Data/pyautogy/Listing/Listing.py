import pyautogui
import time


def checkPostion():
    time.sleep(1)
    file = open("listing.txt")
    print(pyautogui.position())
    print(file)


def createNew():
    print("Running .....")
    pyautogui.press("capslock")

    # Open File
    file = open("listing.txt")
    pyautogui.click(197, 19, button="left")
    pyautogui.press("f9")
    pyautogui.click(242, 102, button="left")


def createLine():
    time.sleep(1)
    file = open("listing.txt")
    steps = 0

    for item in file:
        if steps == 0:  # Barcode
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 1:  # Group
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 2:  # SS Group
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 3:  # SSS Group
            pyautogui.click(300, 178, button="left")
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 4:  # Brand
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 5:  # Category
            pyautogui.press("delete", presses=4)
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 6:  # Description
            pyautogui.write(item)
            pyautogui.press("enter")
            steps = steps + 1

        elif steps == 7:  # Small Description
            pyautogui.write(item)
            pyautogui.press("enter")
            steps = steps + 1

        elif steps == 8:  # Item Code
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 9:  # UOM
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 10:  # Base Packing
            pyautogui.press("delete", presses=4)
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 11:  # Major Packing
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 12:  # Major Packing Qty
            pyautogui.write(".")
            pyautogui.press("left", 2)
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 13:  # Major Packing Name
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 14:  # Supplier
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 15:  # Pack ID
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 16:  # Cost
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 17:  # Landing Cost
            pyautogui.write(item)
            steps = steps + 1

        elif steps == 18:  # Retail
            pyautogui.write(item)
            steps = steps -18

        elif steps == 19:  # Retail
            steps = steps - 18
            steps = 0
            

def addLocation():
    time.sleep(1)
    pyautogui.press("f8")
    pyautogui.click(521, 323, button="left")
    pyautogui.click(528, 354, button="left")
    pyautogui.press("f10")


# checkPostion()
def runApp():
    createNew()
    createLine()


runApp()
