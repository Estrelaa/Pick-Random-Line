# This file stores the functions needed to read the .txt files, save the contents as a list varible
# and then pick a random index in the list, returning the value of that index

import random

FileName = 'list.txt' 
FileNameDefault = 'list.txt'

def UpdateSelectionInProgram():
    CurrentSelecion = []
    with open(FileName, "r") as read_file:
        CurrentSelecion = read_file.readlines()
    return CurrentSelecion


def SelectRandomElementFromList():
    CurrentSelecion = UpdateSelectionInProgram()    # Run function then save the list that the the function makes
    ChosenChoice = random.choice(CurrentSelecion)
    return ChosenChoice

# This functions connects to option 2 in the menu function. This does not work yet as Filename is not being updated.
# This is due to the file closing when reentering the the menu loop. 
def SelectFileInDict():
    print('''Type the name of the file you want to use
    NOTE: Its needs to be in the same loctaion as list.txt and include .txt at the end!
    If it is not or you have just loaded the program it will "list.txt"\n''')

    FileName = input('Name of file: ')
