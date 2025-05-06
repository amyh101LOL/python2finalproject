import time, math, os
from game_things import *
import fighting

player = Player("", 80, 80)

def chapter(ch):
    width = 50
    center_align = "{:^{}}".format(ch.upper(), width)
    print("\n", f"|{center_align}|", "\n")

def encounter_monster(ch, monster_list, monster_boss): # create lists of monsters for each section/chapter
    choose_monster = random.randint(1, 10)
    
    if monster_boss == None:
        return list(monster_list.keys())[0] if 1 <= choose_monster <= 6 else list(monster_list.keys())[1]
    else:
        if 1 <= choose_monster <= 5:
            return monster_list[ch].keys()[0]
        elif 6 <= choose_monster <= 8:
            return monster_list[ch].keys()[1]
        else:
            return monster_boss[ch]

def leave_location():
    print('\nReturning to the road...')
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.5)

def enter_location(ch):
    firstTime = locations[ch].firstTimeEntering
    os.system('cls' if os.name == 'nt' else 'clear')
    
    match ch.lower():
        case 'cottage in the woods': # ch 1
            firstTime == False
            print('You enter the homely cottage, disregarding the fact that you might be considered a home invader. Oh, well. It\'s not like they can do anything.')
            # call sus mage function. print below is placeholder for now
            time.sleep(2)
            print('Nobody is home, anyway. You decide to take a couple things from the breakfast table under the window. The owner probably won\'t mind.')
            time.sleep(2)
            player.add_to_inventory(locations[ch].items, locations[ch].items_amt)
            time.sleep(1.5)
            leave_location()
            return
        case 'abandoned campsite': # ch 1
            print('You come across a campsite. Since the outbreak, it\'s stayed unused. There are still some items from its last group of campers.')
            time.sleep(2)
            print("There's a big chance they won't care if you take a few things for the road.")
            time.sleep(1.5)
            return
        case 'the pond in the sky': # ch 2
            pass

def moving_in_game(ch, sections, section_boundaries, building_positions, screen_width):
    player_pos = 0  # value changes to simulate player movement
    scroll_offset = 0  # initial scroll offset (simulates movement)

    # track current section
    current_section = 1

    # while-loop to continuously move
    while True:

        # Calculate the actual position of the player relative to the scroll
        player_actual_pos = (player_pos - scroll_offset) % screen_width

        # Draw the "screen" with the player (@)
        screen = [' '] * screen_width  # Create an empty screen
        
        # Display building behind player if overlapped
        building_pos = building_positions[current_section]
        screen[building_pos] = "⾕"
        
        # Always place the player at the center of the screen
        screen[player_actual_pos] = '웃'

        # Display the current section description
        print(sections[current_section])

        # Print the screen
        print(''.join(screen))
        
        if player_actual_pos == building_pos:
            print('[E] to interact')
        else:
            encounter_chance = random.randint(1, 10)
            if encounter_chance >= 7:
                enemy = encounter_monster(ch, all_monsters[ch], boss_monsters[list(boss_monsters.keys())[ch]])
                battle(enemy)

        # Get user input to move
        try:
            move = input("Move ([A] left, [D] right), [I] inventory: ").strip().lower()
        except TypeError: # User entered a number
            print("\nPlease enter a valid letter.\n")
            time.sleep(0.8)
        except Exception:
            print("\nPlease enter a valid input.\n")
            time.sleep(0.8)

        # FIX THIS LATER FOR SECTION BARRIERS
        if move == 'a':
            if player_pos > 0:
                scroll_offset = (scroll_offset + 1) % screen_width
                player_pos -= 1 # Move player left
            os.system('cls' if os.name == 'nt' else 'clear')
        elif move == 'd':
            if player_pos < screen_width - 1:
                scroll_offset = (scroll_offset - 1) % screen_width
                player_pos += 1 # Move player right
            os.system('cls' if os.name == 'nt' else 'clear')
        elif move == 'i': # Opem inventory
            print()
            player.open_inventory(items_movement, items_fighting)
        elif move == 'e' and player_actual_pos == building_pos:
            print('player enters location (not implemented yet)')
            enter_location(sections[current_section]) # make classes for the locations
        else: # User didn't enter a valid choice
            print("\nPlease enter either a valid letter.\n")
            continue # Exit the game

        # Check if the player has moved off-screen and should enter a new section
        for section, (start, end) in section_boundaries.items():
            # Check if player position is within the section boundaries
            if start <= player_pos and player_pos <= end:
                if section != current_section:
                    current_section = section  # Update the current section
                    print(f"\nYou have entered {sections[section]}!\n")






''' chapter("PROLOGUE")

time.sleep(1)
print("SOMEWHERE HIGH UP...\n")
time.sleep(2)

print("*poof*")
time.sleep(1)

print("\t???: Finally... after so long, it is FINALLY done... my masterpiece!")
time.sleep(0.5)
print("*Something rumbles.*")
time.sleep(0.5)
print("\t???: Oh, be quiet, Torricend. You can’t even begin to fathom how important this serum is! With it, the wizarding world will HAVE to acknowledge me!")
time.sleep(0.8)
print("*Torricend rumbles again.*")
time.sleep(0.5)
print("\t???: It’s so exciting, I know. And I think I have a test subject in mind...")

time.sleep(1)
print("\nIN THE ROYAL PALACE...\n")
time.sleep(2)

print("\tKing Vaughan: Maribelle, you know it’s not safe to go out right now-")
time.sleep(0.8)
print("\tPrincess Maribelle: Nonsense, father! There hasn’t been an attack in months! Plus, you know how much I despise being locked away in the castle all day! Now, imagine that for an entire week! I have begun to lose memory of what the birds and trees look like...")
time.sleep(0.8)
print("\tKing Vaughan: Princess, you must understand that this is all in your good interest. If you are attacked, I do not know how well I can handle that news again!")
time.sleep(0.8)
print("\tPrincess Maribelle: Father, are you not concerned about the townsfolk? The recent earthquakes that ravage our city have taken a toll on them! It is absolutely imperative that we at the least send word their way that we have not forgotten them-")
time.sleep(0.8)
print("\tKing Vaughan: In this madness?! Princess, there are mutants lurking our very courtyards. In what world will we be able to make it outside the castle grounds alive, lest we be gravely injured by their unhinged maws and elongated claws?!")
time.sleep(0.8)
print("*Before Princess Maribelle can respond, a violent earthquake rocks the castle. The vibrations get stronger and stronger before, suddenly, the floor beneath them crumbles as a giant dog-like monster with green vessels wrapped around its body digs its way out with claws as long as the Queen Mary.*")
time.sleep(2)
print("\tPrincess Maribelle: WHAT IN THE WORLD IS GOING ON?!")
time.sleep(0.8)
print("*Her screams are abruptly silenced by the being, its serrated claws delicately closing around her and sequestering her from the rest of the world. Almost as quickly as it comes, the being disappears, bringing Princess Maribelle with it.*")
time.sleep(2)

time.sleep(1)
print("DEEP IN THE FOREST...\n")
time.sleep(2)

print("*You receive a scroll while out gathering Tinkle Berries.*")
time.sleep(0.8)
print("\t???: Another quest… from the King?! What a surprise. I thought he’d want nothing to do with me after attempting to court the Lady.")
time.sleep(0.8)
print("*You skim the letter. Somewhere in the beginning, the King makes it clear that you’re only being hired because of your skill and that he is overlooking your sour relationship with him.*")
time.sleep(2)

player_name = input("Sign your name on the scroll to accept the quest:\t").strip()

time.sleep(1)
print("*You begrudgingly accept the quest.*")
time.sleep(1)
print(f"\t{player_name}: Very well... the Berries will have to wait.")
time.sleep(0.8)
'''


print('\nFROM DEVS: Use VSCode\'s terminal for a better experience.')
chapter("1: The Lonely Forest")
time.sleep(2)

# sections for the screen and buildings, just for devs ease of locating places
sections1 = {1: "Cottage in the Woods",
            2: "Abandoned Campsite"}
sections1_boundaries = {1: (0,9),
                        2: (10, 19)}
building_pos1 = {1: 4, 2: 8}
chapter_index = 0
moving_in_game(chapter_index, sections1, sections1_boundaries, building_pos1, 20)

'''chapter("2: The Hardy Sea of Flying Fish")

chapter("3: The Mountain Bearing Shiny Teeth")

chapter("4: The Hideout")'''



