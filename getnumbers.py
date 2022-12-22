'''
python script to return a list of numbers from a STRING pasted into the console
separated by whitespace, commas, fullstops. em dash'-',underscore'_',newline\n

import returnums(arg) function that takes the string as argument and returns a list of numbers

pending: modify to accept floats !
'''


class stringNums:
    def __init__(self, stringnums):
        self.value = stringnums
        self.separatedlist = []

    def separatenums(self):
        templist = []
        for i in self.value:
            if i not in (' ', '-', ',', '.', '_', '//n') and i.isdigit(): #check for separating characters
                templist.append(i)
                continue
            else:
                if templist:
                    self.separatedlist.append(int(''.join(templist)))#append the integer form of the string formed by joining the elements of templist
                    templist.clear()  # remove all elements from the string list for next iteration(s)
                    continue
                else:
                    continue
        else: #to run after exhaustion of for loop
            self.separatedlist.append(int(''.join(templist)))#append resultant integer in templist after iterations
        return self.separatedlist

def returnums(arg):
    '''
    work the script here, call to paste manually
    :return:list containing separated numbers
    '''
    # thenumstring = input('paste the whitespace, commas, fullstops. em dash'-',underscore\'_\',newline\\n ')
    return stringNums(arg).separatenums()
# print(returnums('12 34,56,75 43.22 _ 34'))