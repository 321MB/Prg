import time  # includes a library named time
import random  # includes a library named random


# def rps():
#    """This plays a game of rock-paper-scissors
#
#        Dutch version (or a variant of that game ...)
#
#        inputs: no inputs    (prompted text doesn't count as input)
#        outputs: no outputs  (printing doesn't count as output)
#    """
#    name = input("Hoi...wat is jouw naam? ")
#    print()
#    print("Hmmm...")
#    print()
#
#    if name == "Johan" or name == "Marjan":
#        print('Ik ben "offline". Probeer het later.')
#
#    elif name == "Piet":
#        print("Bedoel je Riet?")
#        time.sleep(1)
#        print("Nee?")
#        time.sleep(1)
#        print("Oh.")
#
#    else:
#        print("Welkom, ", name)
#       my_choice = random.choice(["steen", "papier", "schaar"])
#        print("Trouwens, ik koos ", my_choice)


def rps():
    print("    ")
    print("steen papier schaar")
    pc_choice = input("kies je hand [steen, papier, schaar]:")
    npc_choice = random.choice(["steen", "papier", "schaar"])
    print("ik heb", npc_choice)
    time.sleep(1)
    if pc_choice == "steen":  # user kiest steen
        if npc_choice == "papier":
            print("Yes!! ik win")
        elif npc_choice == "steen":
            print("Gelijkspel")
        else:
            print("Jij wint..")

    if pc_choice == "papier":  # user kiest papier
        if npc_choice == "schaar":
            print("Yes!! ik win")
        elif npc_choice == "papier":
            print("Gelijkspel")
        else:
            print("Jij wint..")

    if pc_choice == "schaar":  # user kiest schaar
        if npc_choice == "steen":
            print("Yes!! ik win")
        elif npc_choice == "schaar":
            print("Gelijkspel")
        else:
            print("Jij wint..")
