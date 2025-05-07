import os, time
from game_things1 import *

def battle(player, monster):
    player.enter_battle()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\nYou encountered a {monster.name}!\n")
    time.sleep(0.8)
    print(f"\t\tEnemy: {monster.health}/{monster.max_health} HP")

    while monster.health > 0 and player.health > 0:
        choice = input("\n[F] FIGHT, [I] OPEN INVENTORY, [R] RETREAT: ").strip().lower()

        if choice == "f": # player attacks
            damage = player.use_weapon(player.equipped_weapon)
            print(f"You attack and deal {damage} damage!")
            monster.take_dmg(damage)
        elif choice == "i":
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

        if monster.is_defeated():
            print(f"\nYou defeated {monster.name}!")
            if monster.name in boss_monsters:
                return
            print(f"It dropped: {monster.material}")
            return
        
        # Monster attacks
        damage = monster.attack(3)
        player.health = max(0, player.health - damage)
        print(f"You are at {player.health}/{player.max_health} HP.")

        if player.is_defeated():
            print("\nYou were defeated...")
            print("Game over.")
            exit()



