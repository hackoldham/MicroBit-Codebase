# Add your Python code here. E.g.
from microbit import *
import random
iState = 1
iTopSpeed = 150
iLoopDelay = 100
iDecrement = 10
iSpeed = 0
iCurrentLoop = 15
iPlayerPos = 0
iLinePos = 0
iLineGapPos = 0

while True:
    if iState == 0:
        iSpeed = iTopSpeed
        iCurrentLoop = iSpeed
        display.show(Image.ARROW_W)
        if button_a.is_pressed():
            iState = 1
    if iState == 1:
        display.scroll("Get ready!", 100)
        display.scroll("3")
        display.scroll("2")
        display.scroll("1")
        iPlayerPos = 0
        iLinePos = 0
        iState = 2
        iLineGapPos = random.randint(0, 4)
    if iState == 2:
        for iter in range(0, 5):
            if iter == iLineGapPos:
                display.set_pixel(iter, iLinePos, 0)
            else:
                display.set_pixel(iter, iLinePos, 7)
        display.set_pixel(iPlayerPos, 4, 9)
        
        if button_a.is_pressed() and iPlayerPos > 0:
            display.set_pixel(iPlayerPos, 4, 0)
            iPlayerPos = iPlayerPos - 1
        if button_b.is_pressed() and iPlayerPos < 4:
            display.set_pixel(iPlayerPos, 4, 0)
            iPlayerPos = iPlayerPos + 1
            
        iCurrentLoop = iCurrentLoop  - 1
        
        if iCurrentLoop < 0:
            iLinePos = iLinePos + 1
            display.scroll(str(iLinePos))
            if iLinePos == 5:
                iState = 3
            iCurrentLoop = iSpeed
            display.clear()
        else:
            sleep(iLoopDelay)
            
    if iState == 3:
        if iPlayerPos == iLineGapPos:
            iLinePos = 0
            iSpeed = iSpeed - iDecrement
            iCurrentLoop = iSpeed
            iState = 2
            iLineGapPos = random.randint(0,4)
        else:
            iState = 4
    if iState == 4:
        display.scroll ("Game over")
        display.scroll ("Final Score")
        display.scroll (str(10 - iSpeed))
        iState = 0
