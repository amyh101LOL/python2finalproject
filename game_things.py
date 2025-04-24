from email.base64mime import header_length
import random

weapons = {"Amber Duel": {'weapon_type' : "Knight Sword", 'atk' : 8, 'location' : "Spawn"},
            "Dark-Dweller": {'weapon_type' : "Magic Sword", 'atk' : 18, 'location' : "The Lonely Forest"},
            "Felix 99":{'weapon_type' : "Wand", 'atk' : 15, 'location' : "The Lonely Forest"},
            "Espee De Fue": {'weapon_type' : "Magic Sword", 'atk' : 50, 'location' : "The Hardy Sea of Flying Fish"},
            "Exodus 1600": {'weapon_type' : "Wand", 'atk' : 50, 'location' : "The Hardy Sea of Flying Fish"},
            "Pulsing Wave": {'weapon_type' : "Wand", 'atk' : 60, 'location' : "The Hardy Sea of Flying Fish"},
            "Donta 2048": {'weapon_type' : "Wand", 'atk' : 65, 'location' : "The Mountain Bearing Shiny Teeth"},
            "Great Warrior's Valor": {'weapon_type' : "Knight Sword", 'atk' : 70, 'location' : "The Mountain Bearing Shiny Teeth"}}


items = {'Bungle Berry': {'hp' : 7, 'location': 'The Lonely Forest'},
        'Tinkle Berry' : {'hp' : 5, 'location': 'The Lonely Forest'},
        "Nature’s Call" : {'hp' : 7, 'atk' : 15, 'def' : 10, 'location': 'The Lonely Forest'},
        'Panacea Potion' : {'hp' : 25, 'atk' : 10, 'location': 'The Lonely Forest'},
        'Whispering Leaf' : {'hp' : 30, 'location': 'The Lonely Forest'},
        'Beetlelight Lantern' : {'location': 'The Lonely Forest'},
        'Skilled Crafter' : {'location': 'The Lonely Forest'},
        'Nonalcoholic Mead' : {'hp' : 15, 'def' : 5, 'location': 'The Hardy Sea of Flying Fish'},
        'Katzenjammer' : {'hp' : 10, 'location': 'The Hardy Sea of Flying Fish'},
        'Spiked Freshwater' : {'hp' : 7, 'def' : 5, 'location': 'The Hardy Sea of Flying Fish'},  
        'Soothing Aqua' : {'hp' : 25, 'location': 'The Hardy Sea of Flying Fish'},
        "Bartender’s Special" : {'hp' : 30, 'atk' : 8, 'location': 'The Hardy Sea of Flying Fish'},
        'Adrenaline Booster' : {'atk' : 10, 'location': 'The Hardy Sea of Flying Fish'},
        'Conch Horn' : {'location': 'The Hardy Sea of Flying Fish'},
        'Frozen Berry' : {'hp' : 8, 'atk' : 7, 'location': 'The Mountain Bearing Shiny Teeth'},
        'Fur Coat' : {'spd' : 5, 'atk' : 2, 'location': 'The Mountain Bearing Shiny Teeth'}, 
        'Unlit Torch' : {'spd' : 3, 'def' : 3, 'location': 'The Mountain Bearing Shiny Teeth'},
        'Normal Serum' : {'hp' : 50, 'atk' : 25, 'location': 'The Mountain Bearing Shiny Teeth'},
        "Doctor Good’s Refined Serum" : {'hp' : 60, 'atk' : 30, 'location': 'The Mountain Bearing Shiny Teeth'},
        'Chrono Vial' : {'def' : 30, 'location': 'The Hideout'},
        'Chrono Core' : {'atk' : 25, 'location': 'The Hideout'},
        'Refined Serum' : {'hp' : 10, 'def' : 15, 'location': 'The Hideout'},
        "Beast’s Final Hour" : {'hp' : 70, 'atk' : 90, 'def':50, 'location': 'The Hideout'}}

class Player:
    ''' Simulate the Player and their stats. '''
    
    def __init__(self, name, health, max_health, weapon, inventory):
        self.name = name
        self.health = health # Changing HP
        self.max_health = health # Max HP
        self.weapon = weapon
        self.inventory = inventory
    
    def use_weapon(self):
        return self.weapon.atk
    
    def use_item(self, item): # fix this later
        try:
            self.health += item['hp']
        except:
            pass
        try:
            self.weapon += item['atk']
        except:
            pass

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
