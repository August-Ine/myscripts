'''
SCRIPT TO GUESS RANDOM NUMBERS FOR RATING
'''

import pyautogui, random, time
time.sleep(3)#wait 3 seconds to navigate to cell
for i in range (9):
    pyautogui.typewrite(f'{random.randint(4,9)}')#type a random integer between 3 and 8
    pyautogui.typewrite(['enter'])#tab to move to the next cell


