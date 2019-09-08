from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *
from Format_GIFT import *
from random import randint

#
# Example 3 shows the use of a multi-select menu. A multi-select menu will execute all of the
# selected actions with a single user input prompt.
#


def SaisieManuelle():
    print("Saisie manuelle des questions")
    Screen().input('Press [Enter] to continue')


def GenerationAuto():
#    bases = {'décimale','hexadécimale','binaire'}
#
#    q = Question()
#    q.titre = "Question de conversion"
#    i1 = randint(0,2)
#    while True:
#        i2 = randint(0,2)
#        if (i1 != i2): break
#    q.enonce = "Convertir le nombre "+base[i1]+" suivant en "+bases[i2]
#    print(q.titre)
#    print(q.enonce)

    print("Génération automatique des questions de conversion")
    Screen().input('Press [Enter] to continue')
    

def main():

    # Create the root menu
    menu = MultiSelectMenu("Root Menu", "This is a Multi-Select Menu",
                           epilogue_text=("Please select one or more entries separated by commas, and/or a range "
                                          "of numbers. For example:  1,2,3   or   1-4   or   1,3-4"),
                           exit_option_text='Exit Application')  # Customize the exit text

    # Add all the items to the root menu
    menu.append_item(FunctionItem("Saisie manuelle des questions", SaisieManuelle, args=[]))
    menu.append_item(FunctionItem("Génération automatique des questions de conversion", GenerationAuto, args=[]))

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
