#from storage import Monster

#monster_name = new Monster()
monster_health = 40
m_current_health = 40
player_health = 50
print(f"You encountered a {monster_name}!")
print(f"Enemy: {monster_health}/{monster_health} HP")

choice = input("\n[F] ATTACK, [I] USE ITEM, [R] RETREAT: ")

initial_health = player_health


if monster_health <= 0:
    print("You win!")
    print(f"{monster_name} dropped", )
elif player_health <= 0:
    print("You lose.")
    player_health = initial_health
