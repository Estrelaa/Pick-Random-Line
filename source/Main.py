# This is the main file that runs the whole program. 

import PickElement

def menu():
    print('Welcome to PRL! Please select a option below: ')
    print (' ') # Blank line to make menu look nicer
    print('1. Run program')
    print('2. Select file')
    print('3. Help')
    print('4. Quit')
    print('Your Selection: ')
    UserSelection = int(input())
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
        return 0


def main():
    while(True):
        UserOption = menu()
        ReturnedValue = RunSelectedOption(UserOption)
        if ReturnedValue != 0:
            break
    return print(ReturnedValue)

main()
