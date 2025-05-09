import time

def runPrologue():
    time.sleep(1)
    print("SOMEWHERE HIGH UP...\n")
    time.sleep(2)

    print("*poof*")
    time.sleep(1)

    print("\t???: Finally... after so long, it is FINALLY done... my masterpiece!")
    time.sleep(0.5)
    print("*Something rumbles.*")
    time.sleep(0.5)
    print("\t???: Oh, be quiet, Torricend. You can’t even begin to fathom how important this serum is! With it, the wizarding world will HAVE to acknowledge me!")
    time.sleep(0.8)
    print("*Torricend rumbles again.*")
    time.sleep(0.5)
    print("\t???: It’s so exciting, I know. And I think I have a test subject in mind...")

    time.sleep(1)
    print("\nIN THE ROYAL PALACE...\n")
    time.sleep(2)

    print("\tKing Vaughan: Maribelle, you know it’s not safe to go out right now-")
    time.sleep(0.8)
    print("\tPrincess Maribelle: Nonsense, father! There hasn’t been an attack in months! Plus, you know how much I despise being locked away in the castle all day! Now, imagine that for an entire week! I have begun to lose memory of what the birds and trees look like...")
    time.sleep(0.8)
    print("\tKing Vaughan: Princess, you must understand that this is all in your good interest. If you are attacked, I do not know how well I can handle that news again!")
    time.sleep(0.8)
    print("\tPrincess Maribelle: Father, are you not concerned about the townsfolk? The recent earthquakes that ravage our city have taken a toll on them! It is absolutely imperative that we at the least send word their way that we have not forgotten them-")
    time.sleep(0.8)
    print("\tKing Vaughan: In this madness?! Princess, there are mutants lurking our very courtyards. In what world will we be able to make it outside the castle grounds alive, lest we be gravely injured by their unhinged maws and elongated claws?!")
    time.sleep(0.8)
    print("*Before Princess Maribelle can respond, a violent earthquake rocks the castle. The vibrations get stronger and stronger before, suddenly, the floor beneath them crumbles as a giant dog-like monster with green vessels wrapped around its body digs its way out with claws as long as the Queen Mary.*")
    time.sleep(2)
    print("\tPrincess Maribelle: WHAT IN THE WORLD IS GOING ON?!")
    time.sleep(0.8)
    print("*Her screams are abruptly silenced by the being, its serrated claws delicately closing around her and sequestering her from the rest of the world. Almost as quickly as it comes, the being disappears, bringing Princess Maribelle with it.*")
    time.sleep(2)

    time.sleep(1)
    print("\nDEEP IN THE FOREST...\n")
    time.sleep(2)

    print("*You receive a scroll while out gathering Tinkle Berries.*")
    time.sleep(0.8)
    print("\t???: Another quest… from the King?! What a surprise. I thought he’d want nothing to do with me after attempting to court the Lady.")
    time.sleep(0.8)
    print("*You skim the letter. Somewhere in the beginning, the King makes it clear that you’re only being hired because of your skill and that he is overlooking your sour relationship with him.*")
    time.sleep(2)

    player_name = input("Sign your name on the scroll to accept the quest:\t").strip()

    time.sleep(1)
    print("*You begrudgingly accept the quest.*")
    time.sleep(1)
    print(f"\t{player_name}: Very well... the Berries will have to wait.")
    time.sleep(0.8)
    
    return player_name