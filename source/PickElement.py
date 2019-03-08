# This file stores the functions needed to read the .txt files, save the contents as a list varible
# and then pick a random index in the list, returning the value of that index

import random

def UpdateSelectionInProgram():
    CurrentSelecion = []
    with open("list.txt", "r") as read_file:
        CurrentSelecion = read_file.readlines()
    return CurrentSelecion

def SelectRandomElementFromList():
    CurrentSelecion = UpdateSelectionInProgram()    # Run function then save the list that the the function makes
    ChosenChoice = random.choice(CurrentSelecion)
    return ChosenChoice
