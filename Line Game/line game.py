# Add your Python code here. E.g.
from microbit import *
import random
import math
iState = 0
iTopSpeed = 100
iLoopDelay = 10
iDecrement = 5
iSpeed = 150
iCurrentLoop = 15
iPlayerPos = 0
iLinePos = 0
iLineGapPos = 0
iSetsCompleted = 0
iSinceMove = 0
iBetweenMoves = 10
while True:
    if iState == 0:
        display.show(Image.ARROW_W)
        if button_a.is_pressed():
            iState = 1
    if iState == 1:
        display.scroll("Get ready!", 100)
        display.scroll("3  2  1", 100)
        iPlayerPos = 0
        iLinePos = 0
        iSpeed = iTopSpeed
        iCurrentLoop = iSpeed
        iSetsCompleted = 0
        iDecrement = 5
        iState = 2
        iLineGapPos = random.randint(0, 4)
    if iState == 2:
        for iter in range(0, 5):
            if iter == iLineGapPos:
                display.set_pixel(iter, iLinePos, 0)
            else:
                display.set_pixel(iter, iLinePos, 7)
        display.set_pixel(iPlayerPos, 4, 9)
        
        if button_a.is_pressed() and iPlayerPos > 0 and iSinceMove == 0:
            display.set_pixel(iPlayerPos, 4, 0)
            iPlayerPos = iPlayerPos - 1
            iSinceMove = iBetweenMoves
        if button_b.is_pressed() and iPlayerPos < 4 and iSinceMove == 0:
            display.set_pixel(iPlayerPos, 4, 0)
            iPlayerPos = iPlayerPos + 1
            iSinceMove = iBetweenMoves
        if iSinceMove > 0:
            iSinceMove = iSinceMove - 1
        iCurrentLoop = iCurrentLoop  - 1
        
        if iCurrentLoop < 0:
            iLinePos = iLinePos + 1
            if iLinePos == 5:
                iState = 3
            iCurrentLoop = iSpeed
            display.clear()
        else:
            sleep(iLoopDelay)
            
    if iState == 3:
        if iPlayerPos == iLineGapPos:
            iLinePos = 0
            iDecrement = 5 - math.floor(iSetsCompleted / 5)
            if iDecrement < 1:
                iDecrement = 1
            iSpeed = iSpeed - iDecrement
            iCurrentLoop = iSpeed
            iState = 2
            iOldPos = iLineGapPos
            while iLineGapPos == iOldPos:
                iLineGapPos = random.randint(0,4)
            iSetsCompleted = iSetsCompleted + 1
        else:
            iState = 4
    if iState == 4:
        display.scroll ("Game over")
        display.scroll ("Final Score")
        display.scroll (str(iSetsCompleted))
        iState = 0
