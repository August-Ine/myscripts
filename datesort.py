'''
    -this script is targetted at the directory with screenshots,
    it copies screenshots to a directory labelled with the date
    they were created hopefully sorting them according to context
'''
import os
import shutil
from datetime import datetime

def convert_date(timestamp):
    '''convert time since epoch to date string'''
    d=datetime.utcfromtimestamp(timestamp)
    formated_date=d.strftime('%d %b %Y')
    return formated_date

parentPath='C:/Users/augustine/Pictures/Screenshots'
os.chdir(parentPath)
imageDict={}
dateSet=set()#set for date elements to eliminate duplicates
screenshots=os.scandir()
for entry in screenshots:
    if entry.is_file():#to only evaluate png files and not directories
        info = entry.stat()  # create stat object
        moDate = convert_date(info.st_mtime)  # store string date in moDate variable
        imageDict[entry.name] = moDate  # assign dates to entry in dictionary
        dateSet.add(moDate)  # add date to dateSet
        for date in dateSet:
            try:
                os.mkdir(date)#create date directories in current directory
                if imageDict[entry.name] == date:#check if the current entry modification date is same as current date
                    shutil.move(entry.name, date)  # move to path denoted by the string representation of directory
                    print(f'moved file file {entry.name} to {date}')
                else:
                    continue
            except FileExistsError:
                print('won\'t create directory, file directory already exists ')#warn that the directory already exists
                if imageDict[entry.name] == date:#check if the current entry modification date is same as current date
                    shutil.move(entry.name, date)  # move to path denoted by the string representation of directory
                    print(f'moved file file {entry.name} to {date}')
                else:
                    continue


