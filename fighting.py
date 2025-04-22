from re import A


monster_name = ""
monster_health = 40
XP = 30
player_health = 50
print(f"You encountered a {monster_name}!")
print(f"Health: {monster_health}")

choice = input("\nWhat will you do?\nAttack [A]\nUse an Item [I]\nRetreat [R]\nEnter: ")

initial_health = player_health
if monster_health <= 0:
    print("You win!")
    XP += monster_health*(1/5)
    print(XP)
elif player_health <= 0:
    print("You lose.")
    player_health = initial_health


