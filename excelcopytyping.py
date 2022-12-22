'''
    calculate and type in weighted ratings for design project in excel
    very dusty but imports are valid
'''
from getnumbers import returnums
import pyautogui
import time

weights=[0.117,0.154,0.175,0.134,0.130,0.15,0.14]#list containing weighted percentages

def mainFn():
    argument = input('enter string')
    values=returnums(argument)    # get numbers from string into list
    output = []
    for number in range(len(values)):
        #output.append(weights[number] * values[number])    # create list with corresponding weighted values
        output.append(values[number])
    time.sleep(7)    # stalls application for me to navigate to word file
    for element in output:
        pyautogui.typewrite(f'{element}')    # types string formatted number(to 4sf) in table
        pyautogui.typewrite(['down']) # presses tab key and moves cursor to next cell
    #pyautogui.typewrite(f'{sum(output):.2f}')    # types sum in the last cell for total

mainFn()#run the main function once
while True: #(input('finished continue y/n?')) in ('y','Y'):#with typing values
    mainFn()
    continue
else:
    quit()



