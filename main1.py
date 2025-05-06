# main.py (rewritten)
import time
import random
import os
from turtle import position
from game_things1 import Player, Location, Weapon, Monster, Boss,  items_movement, items_fighting
from fighting1 import battle

class Game:
    def __init__(self):
        self.player = Player("", 80, 80)
        self.setup_chapters()
        
    def setup_chapters(self):
        self.chapters = {
            1: {
                'title': "1: The Lonely Forest",
                'sections': {
                    1: "Cottage in the Woods",
                    2: "Abandoned Campsite"
                },
                'boundaries': {
                    1: (0, 9),
                    2: (10, 19)
                },
                'building_pos': {
                    1: 4,
                    2: 8
                },
                'monsters': {
                    'Goblin': Monster('Goblin', 25, 'Scrap Cloth', 'Bonk', 5, 'Bash', 15),
                    'Drudead': Monster('Drudead', 35, ['Dehydrated Shoots'], 'Tackle', 10, 'Body Slam', 25)
                },
                'locations': {
                    'Cottage in the Woods': Location(['Tinkle Berry', 'Bungle Berry', 'Beetlelight Lantern'], [7, 8, 1], 'Suspicious Mage'),
                    'Abandoned Campsite': Location(['Tinkle Berry', 'Bungle Berry', 'Whispering Leaf', 'Felix 99'], [12, 14, 2, 1], None)
                }
            }
            # Add other chapters here
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_chapter(self, title):
        width = 50
        center_align = "{:^{}}".format(title.upper(), width)
        print("\n", f"|{center_align}|", "\n")
        time.sleep(1)

    def enter_location(self, location_name):
        location = self.chapters[1]['locations'].get(location_name)
        if not location:
            return

        self.clear_screen()
        
        if location_name == 'Cottage in the Woods':
            print('You enter the homely cottage...')
            time.sleep(2)
            print('Nobody is home. You take some items from the table.')
            time.sleep(2)
            self.player.add_to_inventory(location.items, location.items_amt)
            time.sleep(1.5)
            self.leave_location()
        elif location_name == 'Abandoned Campsite':
            print('You come across an abandoned campsite...')
            time.sleep(2)
            print("There are some usable items left behind.")
            time.sleep(1.5)
            self.player.add_to_inventory(location.items, location.items_amt)
            time.sleep(1.5)
            self.leave_location()

    def leave_location(self):
        print('\nReturning to the road...')
        time.sleep(2)
        self.clear_screen()
        time.sleep(0.5)

    def movement_loop(self, chapter_num):
        chapter = self.chapters[chapter_num]
        player_pos = 0
        current_section = 1
        
        while True:
            
            # Display current section info
            print(chapter['sections'][current_section])
            
            # Simple position display
            position_display = [' '] * 20
            building_pos = chapter['building_pos'][current_section]
            position_display[building_pos] = "⾕"
            position_display[player_pos] = '웃'
            print(''.join(position_display))
            
            # Interaction prompts
            if player_pos == building_pos:
                print('[E] to interact')
            
            # Movement input
            try:
                move = input("Move ([A] left, [D] right, [I] inventory), [Q] quit game: ").strip().lower()
            except TypeError:
                print("\nPlease enter a valid letter.\n")
                time.sleep(0.8)
                continue
            except:
                print("\nPlease enter a valid input.\n")
                time.sleep(0.8)
                continue

            # Handle movement
            if move == 'q':
                print('Thank you for playing!')
                time.sleep(1)
                break
            elif move == 'a':
                if player_pos > 0: #chapter['boundaries'][current_section][0] or player_pos != 0:
                    player_pos -= 1
                '''else:
                    print("Can't go further left!")
                    time.sleep(0.5)'''
            elif move == 'd': # fix entering new section (wont send player back to index 0)
                if player_pos < chapter['boundaries'][current_section][1] or player_pos != 19:
                    player_pos += 1
                '''else:
                    print("Can't go further right!")
                    time.sleep(0.5)'''
            elif move == 'i':
                print()
                self.player.open_inventory(items_movement, items_fighting)
            elif move == 'e' and player_pos == building_pos:
                self.enter_location(chapter['sections'][current_section])
            else:
                print("\nInvalid input. Use A/D to move, I for inventory, E to interact.\n")
                time.sleep(0.8)
                continue
            
            self.clear_screen()
            
            # Random encounters (when not at building)
            '''if player_pos != building_pos and random.randint(1, 50) >= 42:
                monster = random.choice(list(chapter['monsters'].values()))
                battle(self.player, monster)
                if self.player.health <= 0:
                    return'''

            # Check for section change
            for section, (start, end) in chapter['boundaries'].items():
                if start <= player_pos <= end and section != current_section:
                    current_section = section
                    print(f"\nEntered {chapter['sections'][section]}!\n")
                    time.sleep(0.5)

    def start(self):
        print('\nFROM DEVS: Use a VSCode terminal for a better experience.')
        time.sleep(2)
        self.display_chapter("1: The Lonely Forest")
        time.sleep(2)
        self.movement_loop(1)

if __name__ == "__main__":
    game = Game()
    game.start()
    
''' put this in a txt file

chapter("PROLOGUE")

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