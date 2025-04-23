
weapons = [{"Amber Duel": {'Info' : "Knight sword", 'atk' : 8, 'dmg' : 1, 'place' : "Spawn"}},
            {"Dark-Dweller": {'Info' : "Magic Sword", 'atk' : 18, 'dmg' : 3, 'place' : "The Lonely Forest"}},
            {"Felix 99":{'Info' : "Wand", 'atk' : 15, 'dmg' : 2, 'place' : "The Lonely Forest"}},
            {"Espee De Fue": {'Info' : "Magic Sword", 'atk' : 50, 'dmg' : 6, 'place' : "The Hardy Sea of Flying Fish"}},
            {"Exodus 1600": {'Info' : "Wand", 'atk' : 50, 'dmg' : 10, 'place' : "The Hardy Sea of Flying Fish"}},
            {"Pulsing Wave": {'Info' : "Wand", 'atk' : 60, 'dmg' : 1, 'place' : "The Hardy Sea of Flying Fish"}},
            {"Donta 2048": {'Info' : "Wand", 'atk' : 65, 'dmg' : 12, 'place' : "The Mountain Bearing Shiny Teeth"}},
            {"Great Warrior’s Valor": {'Info' : "Knight sword", 'atk' : 70, 'dmg' : 11, 'place' : "The Mountain Bearing Shiny Teeth"}}]


items = [{'name' : 'Bungle Berry', 'uses' : 1, 'hp' : 7, 'atk' : 0, 'place': 'The Lonely Forest'},
        {'name' : 'Tinkle Berry', 'uses' : 1, 'hp' : 5, 'atk' : 0, 'place': 'The Lonely Forest'},
        {'name' : "Nature’s Call", 'uses' : 1, 'hp' : 7, 'atk' : 15, 'def' : 10, 'place': 'The Lonely Forest'},
        {'name' : 'Panacea Potion', 'uses' : 1, 'hp' : 25, 'atk' : 10, 'place': 'The Lonely Forest'},
        {'name' : 'Whispering Leaf', 'uses' : 1, 'hp' : 30, 'atk' : 0, 'place': 'The Lonely Forest'},
        {'name' : 'Beetlelight Lantern', 'uses' : 2, 'hp' : 0, 'atk' : 0, 'place': 'The Lonely Forest'},
        {'name' : 'Skilled Crafter', 'uses' : True, 'hp' : 0, 'atk' : 0, 'place': 'The Lonely Forest'},
        {'name' : 'Nonalcoholic Mead', 'uses' : 1, 'hp' : 15, 'def' : 5, 'place': 'The Hardy Sea of Flying Fish'},
        {'name' : 'Katzenjammer', 'uses' : 1, 'hp' : 10, 'atk' : 0, 'place': 'The Hardy Sea of Flying Fish'},
        {'name' : 'Spiked Freshwater', 'uses' : 1, 'hp' : 7, 'def' : 5, 'place': 'The Hardy Sea of Flying Fish'},  
        {'name' : 'Soothing Aqua', 'uses' : 1, 'hp' : 25, 'atk' : 0, 'place': 'The Hardy Sea of Flying Fish'},
        {'name' : "Bartender’s Special", 'uses' : 1, 'hp' : 30, 'atk' : 8, 'place': 'The Hardy Sea of Flying Fish'},
        {'name' : 'Adrenaline Booster', 'uses' : 1, 'atk' : 10, 'place': 'The Hardy Sea of Flying Fish'},
        {'name' : 'Conch Horn', 'uses' : 2, 'place': 'The Hardy Sea of Flying Fish'},
        {'name' : 'Frozen Berry', 'uses' : 1, 'hp' : 8, 'atk' : 7, 'place': 'The Mountain Bearing Shiny Teeth'},
        {'name' : 'Fur Coat', 'uses' : 1, 'spd' : 5, 'atk' : 2, 'place': 'The Mountain Bearing Shiny Teeth'}, 
        {'name' : 'Unlit Torch', 'uses' : 1, 'spd' : 3, 'def' : 3, 'place': 'The Mountain Bearing Shiny Teeth'},
        {'name' : 'Normal Serum', 'uses' : 1, 'hp' : 50, 'atk' : 25, 'place': 'The Mountain Bearing Shiny Teeth'},
        {'name' :"Doctor Good’s Refined Serum", 'uses' : 1, 'hp' : 60, 'atk' : 30, 'place': 'The Mountain Bearing Shiny Teeth'},
        {'name' : 'Chrono Vial', 'uses' : 1, 'def' : 30, 'place': 'The Hideout'},
        {'name' : 'Chrono Core', 'uses' : 1, 'atk' : 25, 'place': 'The Hideout'},
        {'name' : 'Refined Serum', 'uses' : 1, 'hp' : 10, 'def' : 15, 'place': 'The Hideout'},
        {'name' : "Beast’s Final Hour", 'uses' : 1, 'hp' : 70, 'atk' : 90, 'def':50, 'place': 'The Hideout'}]


class Monster: # fix later
    ''' Should be used in fighting.py. '''
    def __init__(self):
        ''' Define the health, material drop, lower and upper threshold of encountering, and basic and special attacks. '''
        self.health = 1
        self.material = ""
        self.smallest_amt = 0 # Lower threshold of 
        self.biggest_amt = 1
        self.basic_atk = ""
        self.basic_dmg = 0
        self.special_atk = ""
        self.special_dmg = 0

