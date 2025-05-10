import os, time
from game_things1 import *

def battle(player, monster):
    player.battle()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\nYou encountered a {monster.name}!\n")
    time.sleep(0.6)
    print(f"\t\tEnemy: {monster.health}/{monster.max_health} HP")
    print(f"{player.name}: {player.health}/{player.max_health} HP")

    while monster.health > 0 and player.health > 0:
        choice = input("\n[F] FIGHT, [I] OPEN INVENTORY, [R] RETREAT: ").strip().lower()

        if choice == "f": # Player attacks
            damage = player.use_weapon(player.equipped_weapon)
            print(f"\nYou attack and deal {damage} damage!\n")
            monster.take_dmg(damage)
            time.sleep(0.8)
            print(f"\t\tEnemy: {monster.health}/{monster.max_health} HP")
        elif choice == "i":
            print()
            player.open_inventory(items_movement, items_fighting)
            continue
        elif choice == "r":
            if monster.name in boss_monsters or monster.prevent_retreat():
                print(f"{monster.name} gives off a warning sound. You don't need to guess what it means; running away only means death.")
            else:
                print("You fled the battle.")
                return
            continue
        else:
            print("Please enter either F, I, or R.")
            continue
        
        time.sleep(1)
        print()
        
        # Did player kill monster?
        if monster.is_defeated():
            print(f"You defeated {monster.name}!")
            if monster.name in boss_monsters:
                return
            time.sleep(0.8)
            print(f"It dropped: {monster.material}")
            player.battle()
            return
        
        # Monster attacks
        damage = monster.attack(3)
        player.health = max(0, player.health - damage)
        time.sleep(0.8)
        print(f"\n{player.name}: {player.health}/{player.max_health} HP")
        print()
        time.sleep(0.8)

        if player.is_defeated():
            print("\nYou were defeated...")
            time.sleep(1)
            print("Game over.")
            time.sleep(0.8)
            exit()
