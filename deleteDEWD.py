'''
python script to delete encrypted DEWD and  ransomware _readme files from a directory and all subdirectories
counts number of instances of readme files removed
run ide as admin
'''

# import statements
from getextension import get_extension
import os


# function to delete all files in the path
def removedewd(mylist):
    print('working...')
    for i in mylist:
        filext = ''
        filext = get_extension(i)
        if filext[-1] == '.dewd':
            os.remove(i)  # deletes file with 'DEWD' extension


# main function
def main():
    thecount = 0
    path = 'D:/'
    print('operation in ' + path)
    os.chdir(path)  # switch to parent file path
    allfiles = []  # list to contain all file paths
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        for file in filenames:
            if file == '_readme.txt':
                os.remove(os.path.join(dirpath, '_readme.txt'))  # delete ransomware readme files
                thecount += 1
            else:
                allfiles.append(os.path.join(dirpath, file))
    removedewd(allfiles)  # call function removedewd
    print('done :) instances removed =', str(thecount))


main()
