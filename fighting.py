import main
from game_things import *

def battle(monster):
    main.player.enter_battle()
    print(f"\nYou encountered a {monster.name}!\n")
    print(f"\t\tEnemy: {monster.health}/{monster.max_health} HP")

    while monster.health > 0 and main.player['health'] > 0:
        choice = input("\n[F] FIGHT, [I] USE ITEM, [R] RETREAT: ").strip().lower()

        if choice == "f": # main.player attacks
            damage = main.player.use_weapon()
            print(f"You attack and deal {damage} damage!")
            monster.take_dmg(damage)
        elif choice == "i":
            main.player.open_inventory()
        elif choice == "r":
            if monster.name in boss_monsters:
                print(f"{monster.name}'s voice shakes the ground beneath your feet. You don't need to guess what it means; running away only means death.")
            else:
                if monster.prevent_retreat == True:
                    print(f"{monster.name} tenses. You probably shouldn't run away right now.")
                else:
                    print("You fled the battle.")
                    break
            return
        else:
            print("Invalid choice. Try again.")
            continue
        if monster.is_defeated():
            print(f"\nYou defeated the {monster.name}!")
            if monster.name in boss_monsters:
                return
            print(f"It dropped: {monster.material}")
            return
        
        # Monster attacks
        damage = monster.use_basic_attack()
        main.player['health'] = max(0, main.player['health'] - damage)
        print(f"You are at {main.player['health']}/{main.player['max_health']} HP.")

        if main.player.is_defeated():
            print("\nYou were defeated...")
