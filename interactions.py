def mage_riddle():
    """"""
    print("Mage: What has hands but can't clap?")

    while True:
        selection = input("You can choose to:\n[A] Answer\n[W] Walk away\n")

        if selection.lower() == "a":
            ans = input("\nAnswer: ")
            if ans.lower() == "clock" or "a clock":
                print("Congratulations! You recieved the Dark-Dweller Sword!")
                break
            else:
                print("Incorrect.")
                break
        elif selection.lower() == 'w':
            print("\nYou walked away from the Mage.")
            break
        else:
            print("\nInvalid Response. Try again.")


def thimblerig():
    """"""
    cups = ['Nonalcoholic Mead', "Bartender's Special", 'Poisonous Drink']
    selection = int(input("Select a cup:\n[1]\n[2]\n[3]\n"))
    if selection == 1:
        print("The Bartender is expressionless.")
    elif selection == 2:
        print("The Bartender is disappointed.")
    
