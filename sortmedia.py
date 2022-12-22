'''
this program sorts mp4 and mp3 files in a folder to respective audio and video
directories.
notes: i could not get the progress percent to show :(
'''
import os
import pprint
import shutil


def get_extension(filename):
    '''returns a string with the extension of a file'''
    splitItem = os.path.splitext(filename)  # get a tuple with separated file name and file extension
    return splitItem


def show_progress():
    '''generator function that print the percentage progress of moving operation'''
    global totalItems, counter
    counter + 1
    yield float((counter / totalItems) * 100)


def get_prettydict(listObj):
    '''function that pretty prints a dictionary with keys being extensions and values being number of files'''
    extensionSet = {x for x in listObj}  # remove duplicates by creating a set for the extensions
    fileCount = {x: exTension.count(x) for x in extensionSet}  # comprehension to map extension to number of files
    return fileCount  # return pretty printable dictionary


def main():
    # global variables
    parentPath = 'F:/phone VIdeos'
    os.chdir(parentPath)  # change directory to parent directory
    print(os.getcwd())  # print new working directory
    fileList = os.listdir()  # get list of all files in current directory
    exTension = [get_extension(element) for element in fileList]  # get all extensions to a list
    globalDict = get_prettydict(exTension)
    counter = 0
    totalItems = globalDict['.mp4'] + globalDict['.mp3'] + globalDict['.3gp'] + globalDict['.m4a']
    pprint.pprint(globalDict)  # prettty print dictionary
    input('press any button to move files to video and audio folders')  # prompt user
    os.mkdir('Video')
    os.mkdir('Audio')  # make directories for files
    for item in fileList[:]:  # iterate over sliced list
        if get_extension(item) in ('.mp3', '.3gp', '.m4a'):
            shutil.move(item, 'Audio')
            # print(f'{show_progress():}%',end='\r')
        elif get_extension(item) == '.mp4':
            shutil.move(item, 'Video')
            # print(f'{show_progress():}%', end='\r')
