import random, time
from game_things1 import special_boss_monsters
from fighting1 import battle

def queen_mariana(poisonorous_defeated):
    """"""
    if poisonorous_defeated < 5:
        print('unfinished')
        #add Queen Mariana's and the player's conversation where she laments over it
    else:
        print('unfinished')
        #add the conversation where she rewards the player with the Exodus 1600 and the Conch Horn

def pulsing_wave(echoing_shards):
    """ Interaction between the Player and Bubba Boo, the pond fisherman.
        Player has the opportunity to get a new weapon by meeting a requirement. """
    if echoing_shards >= 40:
        print('unfinished')
        #add the conversation where Bubba Boo rewards the player with the Pulsing Wave
    else:
        print('unfinished')
        #add the conversation where Bubba Boo tells the player about the Pulsing Wave
    return True

def thimblerig():
    """Game of thimblerig. You get 2 tries. You can inspect a cup and lift it 
    based on the bartender's facial expressions. Only one cup has the Bartender's 
    Special under it!"""
    cups = ['Nonalcoholic Mead', "Bartender's Special", 'Katzenjammer']
    random.shuffle(cups)
    for x in range(2):
        print(f"Selection #{x+1} ")
        selection = int(input("Inspect a cup ([1], [2], [3]): "))   
        cup = cups[selection-1]
        
        print()
        
        if cup != 'Bartender\'s Special': print("Bartender Sump blinks blankly.")
        else: print("Bartender Sump holds his breath nervously.")
        
        time.sleep(1)
        
        while True:
            if x == 0:
                choice = input("Do you want to lift this cup? ([Y] Yes / [N] No): ").strip().lower()
            if choice == 'y': break
            elif choice == 'n':
                if x == 0:
                    print("Choose your cup.\n")
                break
            else:
                print("Please enter Y or N.")
                continue
        time.sleep(1)
    
    print(f"The item underneath is the {cup}.\n")
    time.sleep(1)
    return cup

def tablet_puzzle(helped_gale, battles_fought):
    """a tablet asks the player riddles. When answered correctly, if the player has helped gale and fought more than a 100 battles, the player is rewarded
    with the great warrior's valor. If the player didn't, recives Donta 2048."""
    riddles = [
        ("I speak without a mouth and hear without ears. I come alive with wind. What am I?", "echo"),
        ("What has keys but can’t open locks?", "piano"),
        ("The more of me you take, the more you leave behind. What am I?", "footsteps")]

    print("The tablet shimmers and ancient runes appear:")

    for question, answer in riddles:
        print(f'Riddle: "{question}"')
        player_answer = input("Your answer: ").strip().lower()

        if player_answer == answer:
            if helped_gale and battles_fought >= 100:
                print("The tablet glows brightly. You receive Great Warrior’s Valor!")
            else:
                print("A faint hum echoes from the tablet. You receive Donta 2048.")
            break
        else:
            print("Incorrect. Another ancient rune appears!")
    print("\"Human there are more obstacles yet to come\"\nThe ancient runes disappear")


def mage_riddle():
    """Answer the Mage's riddle to recieve the Dark-Dweller Sword"""
    print("Mage: What has hands but can't clap?")

    while True:
        selection = input("You can choose to:\n[A] Answer\n[W] Walk away\nChoice: ")

        if selection.lower() == "a":
            ans = input("\nAnswer: ")
            if ans.lower() == "clock" or "a clock":
                print("Congratulations! You recieved the Dark-Dweller Sword!")
                break
            else:
                print("Incorrect. The Mage nods his head and walks away...")
                break
        elif selection.lower() == 'w':
            print("\nYou walked away from the Mage.")
            break
        else:
            print("\nInvalid Response. Try again.")

def frostfault_puzzle(player):
    """Puzzle to arrange Greek letters in ascending order to awaken Frostfault."""
    greek_letters = {chr(num) for num in range(945, 950)}
    shuffled = list(greek_letters)
    random.shuffle(shuffled)

    print("Ancient Greek letters glow within the summoning circle:")
    print("Arrange them in ascending order.")
    print("Current order:", ' '.join(shuffled))

    moves = 0
    sorted_letters = sorted(greek_letters)

    while shuffled != sorted_letters:
        try:
            player_order = input("Enter positions for full new order (5 numbers, space-separated): ").split()
            if len(player_order) != 5:
                print("Enter exactly 5 positions.")
                continue

            positions = [int(x)-1 for x in player_order]
            if set(positions) != set(range(5)):
                print("Invalid positions. Use each number 1 to 5 exactly once.")
                continue

            shuffled = [shuffled[pos] for pos in positions]
            moves += 1
            print("Current order:", ' '.join(shuffled))

        except (ValueError, IndexError):
            print("Please enter five valid numbers (1-5).")

    print(f"*The circle ignites after {moves} moves — Frostfault awakens!*")
    battle(special_boss_monsters['Frostfault'])
    frostfault_battle()

def frostfault_battle():
    """ Karma choice for Player. """
    choice = input("Do you spare Frostfault after battle: ").strip().lower()
    if choice == "yes":
        print("*Frostfault bows with acceptance and grants you the key.*")
        time.sleep(1)
        print("*His gratitude overflows, taking the form of the Beast’s Final Hour!*")
    else:
        print("You deal the final blow to Frostfault and rip the chilly key, dangling from the string around his stiff neck, off his body.")
