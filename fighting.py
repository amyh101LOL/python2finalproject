from game_things import Monster

def battle(player, monster):
    print(f"\nYou encountered a {monster.name}!\n")
    print(f"\t\tEnemy: {monster.health}/{monster.max_health} HP")

    while monster.health > 0 and player['health'] > 0:
        choice = input("\n[F] FIGHT, [I] USE ITEM, [R] RETREAT: ").lower()

        if choice == "f":
            damage = player.use_weapon
            print(f"You attack and deal {damage} damage!")
            monster.take_dmg(damage)

        elif choice == "i":
            player.display_inventory # add this method
            player.choose_item # add this method
            print(f"You rummage through your bag... and find your {display_inventory[chosen_item]}. You use it.")

        elif choice == "r":
            print("You fled the battle.")
            return

        else:
            print("Invalid choice. Try again.")
            continue

        if monster.is_defeated():
            print(f"\nYou defeated the {monster.name}!")
            print(f"It dropped: {monster.material}")
            return

        # Monster attacks
        damage = monster.use_basic_attack()
        player['health'] = max(0, player['health'] - damage)
        print(f"You have {player['health']} HP left.")

        if player['health'] <= 0:
            print("\nYou were defeated... Game Over!")
            return
