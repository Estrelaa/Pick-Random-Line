# This is the main file that runs the whole program. 

import os
import PickElement

# Clears the terminal screen for both windows and Unix based systems
# We save the command as a variable so that it does not display a return code to the user 
def CleanTerminal():
    UnusedVariable = os.system('cls')
    UnusedVariable = os.system('clear')


# This functions display a menu for the user to select different options within the program
def menu():
    UserSelection = 0
    while(True):
        CleanTerminal()
        print('Welcome to PRL! Please select a option below: ')
        print (' ') # Blank line to make menu look nicer
        print('1. Run program')
        print('2. Select file')
        print('3. Help')
        print('4. Quit')
        print('Your Selection: ')
        try:
            UserSelection = int(input())
        except ValueError:
            UnusedVariable = input('Please type a number to select one of the options')
        if UserSelection > 0 and UserSelection < 5:
            break
        else:
            UnusedVariable = input('Please type a number between the given range!')
    return UserSelection


def RunSelectedOption(UserOption):
    if UserOption == 1:
        Selecion = PickElement.SelectRandomElementFromList()
        return Selecion
    elif UserOption == 2:
        pass
    elif UserOption == 3:
        pass
    elif UserOption == 4:
        quit()
    else:
        print('Did not reconise input! Please make sure you type one number!')
        return 0    # Used in the main function to tell if user input is vaild or not.


# Main loop that runs the whole program
def main():
    while(True):
        UserOption = menu()
        ReturnedValue = RunSelectedOption(UserOption)
        if ReturnedValue != 0:  # if the returned value is 0 Keep asking for vaild user input.
            break
    return print(ReturnedValue)

main()
