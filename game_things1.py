import math, time, random

class Weapon:
    ''' Simulate a weapon the player can use. '''
    
    def __init__(self, name, atk, dmg, upgrade_count, effect, lvl_up_value, lvl_up_mat_amt, lvl_up_materials):
        self.name = name
        self.atk = atk # atk dealt to enemy
        self.dmg = dmg # atk dealt to player
        self.upgrade_count = upgrade_count # how many times it can lvl up (int)
        self.effect = effect # what stat lvling up affects (string)
        self.lvl_up_value = lvl_up_value # change effect by this value (int)
        self.lvl_up_mat_amt = lvl_up_mat_amt # mat amt needed to lvl up
        self.lvl_up_materials = lvl_up_materials # list of mats required to lvl up weapon (list)
    
    def lvl_up_weapon(self, player):
        if self.upgrade_count > 0 and self.lvl_up_materials in player.materials:
            self.upgrade_count -= 1
            if self.effect == 'atk':
                self.atk += self.lvl_up_value
            elif self.effect == 'def':
                player.defense += self.lvl_up_value
            elif self.effect == 'hp':
                player.health += self.lvl_up_value
        elif self.upgrade_count == 0:
            print("This weapon is already at max level.")
        elif self.lvl_up_materials not in player.materials or self.lvl_up_mat_amt not in player.materials[self.lvl_up_materials]['amt']: # check this
            print("You do not have enough materials to level up this weapon.\nRequired materials:", '-', '\n- '.join([mat for mat in self.lvl_up_materials]), "\n")

class Player:
    ''' Simulate the Player and their stats. '''
    
    def __init__(self, name, health, max_health):
        self.name = name
        self.health = health # Changing HP
        self.max_health = max_health # Max HP
        self.attack = 0
        self.defense = 0
        self.inventory = {'Skilled Crafter' : 1, 'Tinkle Berry' : 4}
        self.materials = {}
        self.weapons = {'Amber Duel' : Weapon('Amber Duel', 10, 0, 0, None, 0, [0], None)}
        self.equipped_weapon = 'Amber Duel'
        self.in_battle = False
        self.moves = 0
    
    def setName(self, name):
        self.name = name

    def battle(self):
        self.in_battle = True
    
    def exit_battle(self):
        self.in_battle = False
    
    def add_weapon_to_inv(self, weapons, new_weapon):
        self.weapons[new_weapon] = weapons[new_weapon]

    def use_weapon(self, weapon_name):
        return self.weapons[weapon_name].atk # return the atk value of the weapon the Player is using.
    
    def equip_weapon(self, weapon_name):
        self.equipped_weapon = weapon_name
        print(f'{weapon_name} equipped.')
        return weapon_name
    
    def is_defeated(self):
        return self.health <= 0
    
    def add_to_inventory(self, new_items, amounts):
        print()
        for item in new_items:
            if item not in self.inventory.keys():
                self.inventory[item] = amounts[new_items.index(item)]
            else:
                self.inventory[item] += amounts[new_items.index(item)]
        print('Inventory updated. Added items:\n', '-', '\n - '.join([f'{self.inventory[item]} {item}' for item in new_items]))
    
    def remove_from_inventory(self, item):
        if item not in self.inventory.keys():
            print("Item not found in inventory.")
            return
        self.inventory[item] -= 1
        if self.inventory[item] == 0:
            del self.inventory[item]

    def craft_inventory(self):
        if len(self.materials) != 0:
            print('Inventory (Materials)\n', '-', '\n- '.join([thing for thing in self.materials]), "\n")
            # mahee
            # ask what user wants to craft.
            # if user's materials >= materials needed to make item,
            # then add that item to user inventory and remove that amt of materials from user's materials
        else:
            print("You have no materials in your inventory.\n")
            time.sleep(1)
            return
    
    def weapon_inventory(self):
        # 'w' input in open_inventory
        print('\n - '.join([weapon for weapon in self.weapons.keys()]))
        # mahee
        # ask user if they want to equip or upgrade a weapon.
        # do the appropriate task.
        action = input("\n[1]Equip Weapon, [2] Upgrade Weapon, [3] Close Weapon Inventory: ").strip()
        if action != '3':
            weapon_name = input("Enter the weapon name: ").strip().title()
            if weapon_name not in self.weapons:
                print("Weapon not found")

            if action == '1':
                self.equip_weapon(weapon_name)
            elif action == '2':
                if self.weapons[weapon_name].upgrade_count <= 0:
                    print(f"{weapon_name} cannot be upgraded further.")
                    return
                
                # Check if the player has the necessary materials to upgrade
                if set(self.weapon.lvl_up_materials).issubset(set(self.materials.keys())):
                    total_materials = True
                    for material in self.weapon.lvl_up_materials:
                        if self.materials.get(material, 0) < self.weapon.lvl_up_mat_amt:
                            print(f"Not enough {material} to upgrade.")
                            total_materials = False
                            break
                    if total_materials:
                        print(f"{weapon_name} successfully upgraded!")
                        self.weapon.lvl_up_weapon(self)
                        self.remove_from_inventory(self.weapon.lvl_up_materials)
                    else:
                        print("You don't have enough materials to upgrade this weapon.")
                else:
                    print("Invalid action.")
                    return
                
                print(f"Upgrading {weapon_name}...\n")
    
    def recipe_inventory(self):
        # 'r' input in open_inventory
        # mahee
        # ask user what item they want to craft. if they had/have it in their inventory, they can craft it.
        # display the material and amount of material needed to craft the item
        pass # delete this line when done

    def open_inventory(self, items_movement, items_fighting):
        def use_item_effects(item_data):
            if "hp" in item_data:
                self.health = min(self.health + item_data['hp'], self.max_health)
                print(f"HP increased to {self.health}")
            if "atk" in item_data:
                self.attack += item_data['atk']
                print(f"ATK increased to {self.attack}")
            if "def" in item_data:
                self.defense += item_data['def']
            print(f"DEF increased to {self.defense}")

        while True:
            inv_display = '\n - '.join([f'{self.inventory[thing]} {thing}' for thing in self.inventory])
            print(f"Inventory (Items)\n - {inv_display}\n")

            try:
                action = input("[E] Use Item" + (", [Q] Close Inventory: " if self.in_battle else ", [R] Item Recipe, [W] Weapons, [Q] Quit: ")).strip().lower()
            except Exception:
                print("\nPlease enter a valid input.\n")
                time.sleep(0.8)
                continue

            if action == 'e':
                while True:
                    item_name = input("Enter item name ([Q] Close): ").strip().title()
                    if item_name == 'Q': break
                    
                    if item_name.lower() == "skilled crafter" and not self.in_battle: # handle crafting
                        self.craft_inventory()
                        break
                    elif item_name in items_movement and not self.in_battle: # handle movement items
                        if item_name.lower() == "beetlelight lantern" and not self.in_battle:
                            self.moves = 0
                        print(f"You used {item_name}.")
                        item_data = items_movement[item_name]
                        if isinstance(item_data, dict):
                            use_item_effects(item_data)
                        self.remove_from_inventory(item_name)
                        break
                    elif self.in_battle and item_name in items_fighting: # handle battle items
                        print(f"You used {item_name}.")
                        item_data = items_fighting[item_name]
                        if isinstance(item_data, dict):
                            use_item_effects(item_data)
                        self.remove_from_inventory(item_name)
                        break
                    else: # item was misspelled, not found, inappropriate in situation, etc.
                        print('\nItem cannot be used right now.\n')

            elif action == 'r':
                self.recipe_inventory()
                print('unfinished') # delete this line when recipe_inventory() is done
                pass
            elif action == 'w':
                self.weapon_inventory()
                print('unfinished') # delete this line when recipe_inventory() is done
                pass
            elif action == 'q':
                print("\nInventory closed.\n")
                time.sleep(0.8)
                return
            else:
                print("\nPlease enter either E, R, W, or Q.\n")
                time.sleep(0.8)

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
        self.extra_dmg = 2

    def prevent_retreat(self):
        threshold = random.randint(1, 10)
        if threshold <= 5:
            return True
        return False
    
    def attack(self, special_chance):
        if random.randint(1, 10) <= special_chance:
            print(f"{self.name} uses {self.basic_atk} and deals {self.basic_dmg} damage!")
            return self.basic_dmg
        else:
            print(f"{self.name} uses {self.special_atk} and deals {self.special_dmg} damage!")
            return self.special_dmg

    def take_dmg(self, dmg):
        self.health = max(0, self.health - dmg)

    def is_defeated(self):
        return self.health <= 0

    def display(self):
        return f"{self.name} | HP: {self.health}/{self.max_health}"

class Boss(Monster):
    ''' Simulate a monster boss that can fight the player. '''
    def __init__(self, name, health, material, basic_atk, basic_dmg, special_atk, special_dmg, ultimate_atk, ultimate_dmg):
        super().__init__(name, health, material, basic_atk, basic_dmg, special_atk, special_dmg)
        self.ultimate_atk = ultimate_atk
        self.ultimate_dmg = ultimate_dmg
        self.extra_dmg = 3

class Location:
    def __init__(self, items, items_amt, character):
        self.items = items
        self.items_amt = items_amt
        self.character = character
        self.firstTimeEntering = True

weapons = {'Amber Duel' : Weapon('Amber Duel', 10, 0, 0, None, 0, [0], None), # 'location' : "Spawn"
            "Dark-Dweller" : Weapon('Dark-Dweller', 18, 0.03, 6, 'atk', 2, [2], ['Dehydrated Shoots']), # 'location' : "The Lonely Forest"
            "Felix 99" : Weapon('Felix 99', 15, 0, 0, None, 0, [0], None), # 'location' : "The Lonely Forest"
            "Espee De Fue" : Weapon('Espee De Fue', 50, 6, 3, 'atk', 5, [1, 7], ['Dehydrated Shoots', 'Spine Fragments']), # 'location' : "The Hardy Sea of Flying Fish"
            "Exodus 1600" : Weapon('Exodus 1600', 50, 10, 0, None, 0, [0], None), # 'location' : "The Hardy Sea of Flying Fish"
            "Pulsing Wave" : Weapon('Pulsing Wave', 60, 0, 4, 'atk', 4, [10, 6], ['Glazed Scales', 'Echoing Shards']), # 'location' : "The Hardy Sea of Flying Fish"
            "Donta 2048" : Weapon('Donta 2048', 65, 12, 5, 'atk', 4, [2, 1], ['Broken Icicles', 'Tufts of Snow']), # 'location' : "The Mountain Bearing Shiny Teeth"
            "Great Warrior's Valor" : Weapon("Great Warrior's Valor", 70, 0, 2, 'atk', 10, [3, 5], ['Broken Icicles', 'Tufts of Snow'])} # 'location' : "The Mountain Bearing Shiny Teeth"

locations = {'Cottage in the Woods' : Location(['Tinkle Berry', 'Bungle Berry', 'Beetlelight Lantern'], [7, 8, 1], 'Suspicious Mage'),
            'Abandoned Campsite' : Location(['Tinkle Berry', 'Bungle Berry', 'Whispering Leaf', 'Felix 99'], [12, 14, 2, 1], None),
            'The Pond in the Sky' : Location(['Conch Horn', 'Chrono Vial'], [1, 1], 'Bubba Boo'),
            'Cloud Nine' : Location(['Nonalcoholic Mead', 'Katzenjammer', 'Spiked Freshwater', 'Espee de Fue'], [1, 2, 1, 1], 'Forrest Sump'),
            'Swirling Pool of Whirl' : Location(['Frozen Berry', 'Conch Horn'], [16, 1], 'Queen Mariana'),
            'Cold Cavern' : Location(['Fur Coat', 'Frozen Berry', 'Unlit Torch', 'Tufts of Snow'], [1, 7, 1, 4], 'Doctor Good'),
            'Mysterious Door' : Location(None, None, 'Frostfault'),
            'Dusty Lab Cell' : Location(['Chrono Vial', 'Chrono Core', 'Adrenaline-Booster'], [1, 1, 1], None)}

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
        "Beast’s Final Hour" : {'hp' : 70, 'atk' : 90, 'def': 50}} # 'location': 'The Hideout'

items_movement = {'Beetlelight Lantern' : "0% monster encounter chance for 10 moves.",
        'Unlit Torch' : {'spd' : 3, 'def' : 3, 'location': 'The Mountain Bearing Shiny Teeth'},
        'Fur Coat' : {'spd' : 5, 'atk' : 2, 'location': 'The Mountain Bearing Shiny Teeth'}}

ch1_monsters = {'Goblin' : Monster('Goblin', 25, 'Scrap Cloth', 'Bonk', 5, 'Bash', 15),
                'Drudead' : Monster('Drudead', 35, ['Dehydrated Shoots'], 'Tackle', 10, 'Body Slam', 25)}
ch2_monsters = {'Fishkys' : Monster('Fishkys', 40, ['Glazed Scales', 'Translucent Drops'], 'Tail Whip', 15, 'Sky Plunge', 30),
                'Zombat' : Monster('Zombat', 60, ['Echoing Shards'], 'Gust', 20, 'Sonic Boom', 45),}
ch3_monsters = {'Toskic' : Monster('Toskic', 100, ['Tufts of Snow'], 'Hornsweep', 18, 'Avalanche', 30),
                'Mammaulth' : Monster('Mammaulth', 120, ['Tufts of Snow', 'Broken Icicles'], 'Burrow', 20, 'Tectonic Rage', 42)}
ch4_monsters = {'Skelerat' : Monster('Skelerat', 95, ['Spine Fragments'], 'Screech', 10, 'Ankle Bite', 20),
                'Enhanced Drudead' : Monster('Enhanced Drudead', 200, ['Dehydrated Shoots'], 'Tackle', 30, 'Body Slam', 75)}
all_monsters = [ch1_monsters, ch2_monsters, ch3_monsters, ch4_monsters] # list of dictionaries
boss_monsters = {None : None,
                'Poisonorous' : Boss('Poisonorous', 65, ['Spine Fragments', 'Translucent Droplets'], 'Spikeball', 13, 'Drill Sting', 15, 'Noxious Infestation', 30),
                'Waile' : Boss('Waile', 70, ['Spine Fragments', 'Translucent Droplets'], 'Jet Click', 18, 'Fallen Soldier', 40, None, None),
                None : None} # ch 1 and 3 have no mini bosses
special_boss_monsters = {'Frostfault' : Boss('Frostfault', 280, None, 'Frostbite', 35, 'Shattering Verglas', 45, "Winter's Fury", 70),
                'Stage 1 Torricend' : Boss('Stage 1 Torricend', 700, None, 'Lunge', 40, 'Waste Pump', 80, 'Eroding Rumble', 110),
                'Stage 2 Torricend' : Boss('Stage 2 Torricend', 1800, None, 'Lockjaw', 70, 'Mortar Flush', 90, 'Ashes to Dust', 200)}
