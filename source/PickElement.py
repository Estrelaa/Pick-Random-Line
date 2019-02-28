import json
import random

def UpdateSelectionInProgram():
    CurrentSelecion = []
    with open("list.txt", "r") as read_file:
        CurrentSelecion = read_file.readlines()
    return CurrentSelecion

def SelectRandomElementFromList():
    CurrentSelecion = UpdateSelectionInProgram()
    ChosenChoice = random.choice(CurrentSelecion)
    return ChosenChoice

UpdateSelectionInProgram()