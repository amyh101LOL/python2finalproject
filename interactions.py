import random
import time

def mage_riddle():
    """Answer the Mage's riddle to recieve the Dark-Dweller Sword"""
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


def pulsing_wave(echoing_shards):
    """"""
    if echoing_shards >= 40:
        pass
        #add the conversation where Bubba Boo rewards the player with the Pulsing Wave
    else:
        pass
        #add the conversation where Bubba Boo tells the player about the Pulsing Wave


def thimblerig():
    """Game of thimblerig. You get 2 tries. You can inspect a cup and lift it 
    based on the bartender's facial expressions. Only one cup has the bartender's 
    special under it!"""
    cups = ['Nonalcoholic Mead', "Bartender's Special", 'Poisonous Drink']
    random.shuffle(cups)
    for x in range(2):
        print(f"Selection #{x+1} ")
        selection = int(input("Inspect a cup:\n[1]\n[2]\n[3]\nEnter: "))   
        cup = cups[selection-1]
        print()
        if cup == 'Nonalcoholic Mead':
            print("Bartender Sump has no expressions on his face.")
        elif cup == "Bartender's Special":
            print("Bartender Sump is disappointed.")
        elif cup == 'Poisonous Drink':
            print("Bartender Sump is smirking.")
        choice = input("Do you want to lift this cup?(y / n)\nEnter: ")
        if choice.lower() == 'y':
            break
        else:
            print("You can inspect another cup but, you must lift it.\n")
    print(f"The item underneath your cup is the {cup}.")


def queen_mariana():
    """"""
    if poisonorous == False:
        pass
        #add Queen Mariana's and the player's conversation where she laments over it
    else:
        pass
        #add the conversation where she rewards the player with the Exodus 1600 and the Conch Horn
    

def stone_tablet():
    """"""
    time.sleep(3)
    print("On the far wall of the cavern hangs a large stone tablet. It has numbers on them.")
    time.sleep(1)
    print("Its out-of-place position has you wondering if there’s something more to it than just paleolithic decoration")
    time.sleep(1)
    print("There are four other tablets laying around. Maybe if you sort them in the correct position...\n")

#didn't finish yet
for x in range(1, 11):
    tablets = {random.randint(0,10) for x in range(1, 6)}
    print(tablets)


def frostfault_circle():
    """ Player must put them in order to awaken Frostfault. Mini boss battle with Frostfault. 
    Kill Frostfault to forcefully take the key to the Mysterious Door, or spare him, 
    retrieve the key, and Player will receive Beast’s Final Hour."""
    pass