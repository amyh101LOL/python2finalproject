import random

class Player:
    ''' Simulate the Player and their stats. '''
    
    def __init__(self, name, health, max_health, inventory):
        self.name = name
        self.health = health # Changing HP
        self.max_health = health # Max HP
        self.attack = 0
        self.defense = 0
        self.inventory = inventory
    
    def use_weapon(self):
        return self.weapon.atk
    
    def open_inventory(self):
        print('\n-'.join([thing for thing in self.inventory]))
        action = input("[U] Use Item, [C] Craft Item").strip().lower()
        if action == 'u':
            item_name = input("Enter the name of the item you would like to use:\t").strip().title()
            if item_name in items_movement.keys():
                print(f"You used {item_name}.")
                
                if "hp" in items_movement[item_name].keys():
                    if self.health + item_name['hp'] <= self.max_health:
                        self.health += item_name['hp']
                    elif self.health + item_name['hp'] > self.max_health:
                        self.health = self.max_health
                    print("HP increased to", self.health)
                if "atk" in items_movement[item_name].keys():
                    self.attack += item_name['atk']
                    print("ATK increased to", self.attack)
                if "def" in items_movement[item_name].keys():
                    self.defense += item_name['def']
                    print("DEF increased to", self.defense)
                elif item_name == "Beetlelight Lantern":
                    print(items_movement['Beetlelight Lantern'])

class Monster:
    ''' Simulate a monster that can fight the Player. '''

    def __init__(self, name, health, material, basic_atk, basic_dmg, special_atk, special_dmg):
        self.name = name # Monster name
        self.health = health # Changing HP
        self.max_health = health # Max HP
        self.material = material # What's dropped when killed
        self.basic_atk = basic_atk # Name of basic attack
        self.basic_dmg = basic_dmg # Amt of dmg dealt by basic
        self.special_atk = special_atk # Name of special attack
        self.special_dmg = special_dmg # Amt of dmg dealt by special
        self.extra_dmg = 3

    def attack(self, special_chance):
        if random.randint(1, 10) <= special_chance:
            print(f"{self.name} uses {self.basic_atk} and deals {self.basic_dmg} damage!")
            return self.basic_dmg
        else:
            print(f"{self.name} uses {self.special_atk} and deals {self.special_dmg} damage!")
            return self.special_dmg

    def take_dmg(self, dmg):
        self.health = max(0, self.health - dmg)
        print(f"{self.name} takes {dmg} damage! Remaining HP: {self.health}/{self.max_health}")

    def is_defeated(self):
        return self.health <= 0

    def display(self):
        return f"{self.name} | HP: {self.health}/{self.max_health}"

class Boss(Monster):
    def __init__(self):
        self.health = 3 # placeholder cuz errors

weapons = {"Amber Duel": {'weapon_type' : "Knight Sword", 'atk' : 8}, # 'location' : "Spawn"
            "Dark-Dweller": {'weapon_type' : "Magic Sword", 'atk' : 18}, # 'location' : "The Lonely Forest"
            "Felix 99":{'weapon_type' : "Wand", 'atk' : 15}, # 'location' : "The Lonely Forest"
            "Espee De Fue": {'weapon_type' : "Magic Sword", 'atk' : 50}, # 'location' : "The Hardy Sea of Flying Fish"
            "Exodus 1600": {'weapon_type' : "Wand", 'atk' : 50}, # 'location' : "The Hardy Sea of Flying Fish"
            "Pulsing Wave": {'weapon_type' : "Wand", 'atk' : 60}, # 'location' : "The Hardy Sea of Flying Fish"
            "Donta 2048": {'weapon_type' : "Wand", 'atk' : 65}, # 'location' : "The Mountain Bearing Shiny Teeth"
            "Great Warrior's Valor": {'weapon_type' : "Knight Sword", 'atk' : 70}} # 'location' : "The Mountain Bearing Shiny Teeth"

items_fighting = {'Bungle Berry': {'hp' : 7}, #  'location': 'The Lonely Forest'
        'Tinkle Berry' : {'hp' : 5}, # 'location': 'The Lonely Forest'
        "Nature’s Call" : {'hp' : 7, 'atk' : 15, 'def' : 10}, # 'location': 'The Lonely Forest'
        'Panacea Potion' : {'hp' : 25, 'atk' : 10}, # 'location': 'The Lonely Forest'
        'Whispering Leaf' : {'hp' : 30}, #  'location': 'The Lonely Forest'
        'Conch Horn' : "Daze enemy. They cannot attack for 1 turn.", # 'location': 'The Hardy Sea of Flying Fish'
        'Nonalcoholic Mead' : {'hp' : 15, 'def' : 5}, # 'location': 'The Hardy Sea of Flying Fish'
        'Katzenjammer' : {'hp' : 10}, # 'location': 'The Hardy Sea of Flying Fish'
        'Spiked Freshwater' : {'hp' : 7, 'def' : 5}, # 'location': 'The Hardy Sea of Flying Fish'
        'Soothing Aqua' : {'hp' : 25}, # 'location': 'The Hardy Sea of Flying Fish'
        "Bartender’s Special" : {'hp' : 30, 'atk' : 8}, # 'location': 'The Hardy Sea of Flying Fish'
        'Adrenaline Booster' : {'atk' : 10}, # 'location': 'The Hardy Sea of Flying Fish'
        'Frozen Berry' : {'hp' : 8, 'atk' : 7}, # 'location': 'The Mountain Bearing Shiny Teeth'
        'Normal Serum' : {'hp' : 50, 'atk' : 25}, # 'location': 'The Mountain Bearing Shiny Teeth'
        'Refined Serum' : {'hp' : 10, 'def' : 15}, # 'location': 'The Hideout'
        "Doctor Good’s Refined Serum" : {'hp' : 60, 'atk' : 30}, # 'location': 'The Mountain Bearing Shiny Teeth'
        'Chrono Vial' : {'def' : 30}, # 'location': 'The Hideout'
        'Chrono Core' : {'atk' : 25}, # 'location': 'The Hideout'
        "Beast’s Final Hour" : {'hp' : 70, 'atk' : 90, 'def':50}} # 'location': 'The Hideout'

items_movement = {'Beetlelight Lantern' : "0% monster encounter chance for 8 moves.",
        'Unlit Torch' : {'spd' : 3, 'def' : 3, 'location': 'The Mountain Bearing Shiny Teeth'},
        'Fur Coat' : {'spd' : 5, 'atk' : 2, 'location': 'The Mountain Bearing Shiny Teeth'},
        }


# name, health, material, basic_atk, basic_dmg, special_atk, special_dmg, extra_dmg
ch1_monsters = {'Goblin' : Monster('Goblin', 25, 'Scrap Cloth', 'Bonk', 5, 'Bash', 15),
                'Drudead' : Monster('Drudead', 35, ['Dehydrated Shoots'], 'Tackle', 10, 'Body Slam', 25)}
ch2_monsters = {'Fishky' : Monster('Fishky', 40, ['Glazed Scales', 'Translucent Drops'], 'Tail Whip', 15, 'Sky Plunge', 30),
                'Zombat' : Monster('Zombat', 60, ['Echoing Shards'], 'Gust', 20, 'Sonic Boom', 45),
                'Poisonorous' : Monster('Poisonorous', 70, ['Spine Fragments', 'Translucent Droplets'], 'Spikeball', 13, 'Drill Sting', 15)}
ch3_monsters = {'Toskic' : Monster('Toskic', 100, ['Tufts of Snow'], 'Hornsweep', 18, 'Avalanche', 30),
                'Mammauth' : Monster('Mammauth', 120, ['Tufts of Snow', 'Broken Icicles'], 'Burrow', 20, 'Tectonic Rage', 42),
                'Frostfault' : Monster('Frostfault', 280, ['None'], 'Frostbite', 35, "Winter's Fury", 70)}
ch4_monsters = {'Skelerat' : Monster('Skelerat', 95, ['Spine Fragments'], 'Screech', 10, 'Ankle Bite', 20),
                'Enhanced Drudead' : Monster('Enhanced Drudead', 200, ['Dehydrated Shoots'], 'Tackle', 30, 'Body Slam', 75)}
boss_monsters = {'Stage 1 Torricend' : Boss('Stage 1 Torricend')}