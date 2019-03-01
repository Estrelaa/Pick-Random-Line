# This is the main file that runs the whole program. 

import PickElement

def menu():
    print('Welcome to PRL! Please select a option below: ')
    print (' ') # Blank line to make menu look nicer
    print('1. Run program')
    print('2. Select file')
    print('3. Help')
    print('4. Quit')

def main():
    Selecion = PickElement.SelectRandomElementFromList()
    return Selecion

print(main())
