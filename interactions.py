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

    #idek what to do with this tbh
    tablets = [] 
    for x in range(1, 6):
        tablet = {random.randrange(0,10) for x in range(1, 6)}
        tablets.append(tablet)
        print(sum(tablet))




def frostfault_circle():
    """ Player must put them in order to awaken Frostfault. Mini boss battle with Frostfault. 
    Kill Frostfault to forcefully take the key to the Mysterious Door, or spare him, 
    retrieve the key, and Player will receive Beast’s Final Hour."""

    while True:
        letter_code_points = {random.randrange(945, 970) for x in range(1, 6)}
        if len(letter_code_points) == 5:
            break

    letters = [chr(x) for x in letter_code_points]
    sorted_letters = sorted(letters)

    numbers = ('1', '2', '3', '4', '5')
    print(" ".join(numbers))
    print(" ".join(letters))
    print()
    print(" ".join(sorted_letters))

    while True:
        sequence = input("\nYou can change the sequence by typing the numbers in your desired order:")
        sequence_set = set()
        for x in sequence:
             if x.isdigit():
                 if int(x) in range(1, 6):
                     sequence_set.add(x)

        print(f"This is sequence_set {sequence_set}")
        if len(sequence_set) != len(letters):
            print("Enter all the numbers in the sequence(1-5)")
        else:
            break

    
    print()
    sequence_letters = [chr(ord(letters[int(x)-1])) for x in sequence_set]
    print(sequence_letters)
    if sequence_letters == sorted_letters:
        print("YOU WIN HOMIEEEEEEE")
    else:
        print("Not this time")
    print("="*50)

while True:
    frostfault_circle()

