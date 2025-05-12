import time

def runCh2Intro(player_name):
    time.sleep(1)
    print("*You step out from the wide shadows of the Forest, your feet digging into the seaside sediment. Apprehension crawls up your spine at the sight of Zombats, turned from the Evil Scientist's manmade pandemic, in the far sky. You swear you'll get revenge on him...*")
    time.sleep(2)
    
    print("\t???: Help! Help!")
    time.sleep(0.8)
    print(f"\t{player_name}: W-What the- is that a...")
    time.sleep(0.8)
    print("\t???: Hey! You there! Help a fish out, would ya?")
    time.sleep(1)
    
    while True:
        help = input("\nWill you help? ([Y] Yes, [N] No):\t").strip().lower()
        
        if help == 'y':
            return True
        elif help == 'n':
            return False
        else:
            time.sleep(0.5)
            print("Please enter Y or N.")
            time.sleep(1)
            continue

def helpedGale(player_name):
    time.sleep(1)
    print(f"\t{player_name}: S-Sure.")
    time.sleep(1)
    
    print("*You spend a moment freeing the fish with wings from the net it's trapped in. The moment you do so, more fish of the same kind burst from the water. You shout in surprise as they flap wildly around you and the now-freed fish.*")
    time.sleep(2)
    
    print("\t???: Thank you! Thank you so much, uh...")
    time.sleep(0.8)
    print(f"\t{player_name}: Call me {player_name}.")
    time.sleep(0.8)
    print("\tGale: I’m Gale! Look alive, human; your valiant efforts have been acknowledged by the Flying Fish of the Hardy Sea!")
    print(f"\t{player_name}: I am honored.")
    time.sleep(0.8)
    print("\tGale: Say, is there anything I can do for you in return?")
    time.sleep(1)
    
    print("*You explain your predicament and how you need to cross the Hardy Sea.*")
    time.sleep(2)
    
    print(f"\tGale: You’ve asked the right fish to do the job! Hop on, {player_name}. I’ll give you a ride across! Although, I’ve got to warn ya, the area's been infested with Zombats for some time now. Could I trouble you with handling them so our ride is as smooth as possible?")
    time.sleep(0.8)
    print(f"\t{player_name}: No problemo.")
    time.sleep(1)

def ignoredGale(player_name):
    time.sleep(1)
    print(f"\t{player_name}: Sorry, I'm a little busy right now.")
    time.sleep(0.8)
    print("\tGale: W-Wait a second! Please! I can’t get out of this mess myself!")
    time.sleep(1)
    print("*You hustle away from the protesting fish, its voice disappearing behind you. Your mind stirs at the thought of losing precious time on your quest to save Princess Maribelle.*")

