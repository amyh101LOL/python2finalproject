# main.py (rewritten)
import time
import random
import os
from turtle import position
from ch2 import helpedGale, ignoredGale, runCh2Intro
from game_things1 import Player, Location, Weapon, Monster, Boss,  items_movement, items_fighting, ch1_monsters, ch2_monsters, ch3_monsters, ch4_monsters
from fighting1 import battle
from prologue_ch1 import runPrologue

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
                    1: (0, 18),
                    2: (19, 36)
                },
                'building_pos': {
                    1: 10,
                    2: 23
                },
                'monsters': ch1_monsters,
                'locations': {
                    'Cottage in the Woods': Location(['Tinkle Berry', 'Bungle Berry', 'Beetlelight Lantern'], [7, 8, 1], 'Suspicious Mage'),
                    'Abandoned Campsite': Location(['Tinkle Berry', 'Bungle Berry', 'Whispering Leaf', 'Felix 99'], [12, 14, 2, 1], None)
                },
                'characters' : {
                    'Movable' : '웃',
                    'Interactable' : "⾕",
                    'Ground' : '_'
                }
            },
            20: {
                'title': "2: The Hardy Sea of Flying Fish",
                'sections': {
                    1: "The Pond in the Sky",
                    2: "Cloud Nine"
                },
                'boundaries': {
                    1: (0, 18),
                    2: (19, 36)
                },
                'building_pos': {
                    1: 7,
                    2: 32
                },
                'monsters': ch2_monsters,
                'locations': {
                    'The Pond in the Sky' : Location(['Conch Horn', 'Chrono Vial'], [1, 1], 'Bubba Boo'),
                    'Cloud Nine' : Location(['Nonalcoholic Mead', 'Katzenjammer', 'Spiked Freshwater', 'Espee de Fue'], [1, 2, 1, 1], 'Forrest Sump')
                },
                'characters' : {
                    'Movable' : '𓆟',
                    'Interactable' : "☁︎",
                    'Ground' : ' '
                }
            },
            21: {
                'title': "2: The Hardy Sea of Flying Fish",
                'sections': {
                    1: "The Hardy Sea",
                    2: "The Swirling Pool of Whirl"
                },
                'boundaries': {
                    1: (0, 18),
                    2: (19, 36)
                },
                'building_pos': {
                    1: None,
                    2: 27
                },
                'monsters': ch2_monsters,
                'locations': {
                    None : None,
                    'Swirling Pool of Whirl' : Location(['Frozen Berry', 'Conch Horn'], [16, 1], 'Queen Mariana'),
                },
                'characters' : {
                    'Movable' : '⏅',
                    'Interactable' : "｡○",
                    'Ground' : 'ꕀ'
                }
            },
            3: {
                'title': "3: The Mountain Bearing Shiny Teeth",
                'sections': {
                    1: "Cold Cavern",
                    2: "Mysterious Door"
                },
                'boundaries': {
                    1: (0, 18),
                    2: (19, 36),
                },
                'building_pos': {
                    1: 14,
                    2: 36
                },
                'monsters': ch3_monsters,
                'locations': {
                    'Cold Cavern' : Location(['Fur Coat', 'Frozen Berry', 'Unlit Torch', 'Tufts of Snow'], [1, 7, 1, 4], 'Doctor Good'),
                    'Mysterious Door' : Location(None, None, 'Frostfault'),
                },
                'characters' : {
                    'Movable' : '웃',
                    'Interactable' : "⛩",
                    'Ground' : '⋆❅₊'
                }
            },
            4: {
                'title': "4: The Hideout",
                'sections': {
                    1: "Dusty Lab Cell",
                    2: "Industrial Lair"
                },
                'boundaries': {
                    1: (0, 18),
                    2: (19, 36),
                },
                'building_pos': {
                    1: 8,
                    2: 27
                },
                'monsters': ch4_monsters,
                'locations': {
                    'Dusty Lab Cell' : Location(['Chrono Vial', 'Chrono Core', 'Adrenaline-Booster'], [1, 1, 1], None)
                },
                'characters' : {
                    'Movable' : '웃',
                    'Interactable' : "⛓",
                    'Ground' : '_'
                }
            }
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
            time.sleep(1.5)
            self.player.add_to_inventory(location.items, location.items_amt)
            time.sleep(1.5)
            self.leave_location()
        elif location_name == 'Abandoned Campsite':
            print('You come across an abandoned campsite...')
            time.sleep(2)
            print("There are some useful items left behind.")
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
        choose_move_on = False
        self.player.moves = 0
        
        while True:
            # Check for section change
            for section, (start, end) in chapter['boundaries'].items():
                if start <= player_pos <= end and section != current_section:
                    current_section = section
                    print(f"\nEntered {chapter['sections'][section]}!\n")
                    time.sleep(0.5)
            
            # Display current section info
            print(chapter['sections'][current_section])
            
            # Get current section boundaries
            section_start, section_end = chapter['boundaries'][current_section]
            section_len = section_end - section_start + 1

            # Display range is always 20 chars
            position_display = [chapter['characters']['Ground']] * section_len

            # Building and tp indexes
            building_pos = chapter['building_pos'][current_section]
            
            # Build the location
            if section_start <= building_pos <= section_end:
                position_display[building_pos - section_start] = chapter['characters']['Interactable']
            
            # Build the TP to next location
            if current_section == 2:
                position_display[section_len - 1] = "◈"
            
            # Build the player
            player_index = player_pos - section_start
            if 0 <= player_index < section_len:
                position_display[player_index] = chapter['characters']['Movable']
            else:
                print(f"out of bounds: index {player_pos}")

            print(''.join(position_display))

            # Interaction prompts
            if player_pos == building_pos or player_pos == section_end and current_section == 2: # fix player-tp overlap interaction
                print('[E] to interact')
            
            # Movement input
            try:
                move = input("Move ([A] left, [D] right), [I] inventory, [Q] quit game: ").strip().lower()
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
                exit()
            elif move == 'a':
                if player_pos > 0:
                    player_pos -= 1
                else:
                    print("Can't go further left!")
                    time.sleep(0.5)
            elif move == 'd':
                if player_pos < self.chapters[chapter_num]['boundaries'][2][1]:
                    player_pos += 1
                else:
                    print("Can't go further right!")
                    time.sleep(0.5)
            elif move == 'i':
                print()
                self.player.open_inventory(items_movement, items_fighting)
            elif move == 'e' and player_pos == building_pos:
                self.enter_location(chapter['sections'][current_section])
            elif move == 'e' and player_pos == section_end and current_section == 2:
                while True:
                    move_on = input("Are you sure you want to move on? ([Y] Yes, [N] No):\t").strip().lower()
                    if move_on == 'y':
                        choose_move_on = True
                        break
                    elif move_on == 'n':
                        self.clear_screen()
                        break
                    else:
                        print("Please enter Y or N.")
                        time.sleep(1)
                        continue
            else:
                print("\nInvalid input. Use A/D to move, I for inventory, E to interact.\n")
                time.sleep(0.8)
                self.clear_screen
                continue
            
            if choose_move_on: # go to next chapter
                break
            
            self.player.moves += 1
            self.clear_screen()
            
            # Random monster encounters (when not at building)  v FIX THIS
            if player_pos != building_pos and (player_pos != section_end and current_section != 2) and random.randint(1, 25) >= 23 and self.player.moves > 10:
                monster = random.choice(list(chapter['monsters'].values()))
                battle(self.player, monster)
                if self.player.health <= 0:
                    return

    def ch1(self):
        time.sleep(1)
        print('\nFROM DEVS: Use a VSCode terminal for a better experience.')
        time.sleep(1.5)
        self.display_chapter("1: The Lonely Forest")
        time.sleep(1)
        self.movement_loop(1)
    
    def ch20(self):
        time.sleep(1)
        self.display_chapter("2: The Hardy Sea of Flying Fish")
        time.sleep(1)
        self.movement_loop(20)
    
    def ch21(self):
        time.sleep(1)
        self.display_chapter("2: The Hardy Sea of Flying Fish")
        time.sleep(1)
        self.movement_loop(21)

if __name__ == "__main__":
    game = Game()
    game.player.setName(runPrologue()) # prologue
    player_name = game.player.name
    game.ch1() # run ch 1
    help_gale = runCh2Intro(player_name) # run ch 2
    if help_gale:
        helpedGale(player_name)
        game.ch20()
    else:
        ignoredGale(player_name)
        game.ch21()