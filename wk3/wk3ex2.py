# Programmeren I, week 3 opgave 2
# Bestandsnaam: wk3ex2.py
# Naam: MICK
# Probleemomschrijving: Slaapwandelende student

import random
import time


def rs():
    """rs chooses a random step and returns it.
    note that a call to rs() requires parentheses
    arguments: none at all!
    """
    return random.choice([-1, 1])


def rwpos(start, nstep):
    """rwpos
    random 
    """
    
    if nstep <= 0:
        return start
    else:
        nStart = start + rs()  # nStart is start + random -1 or 1
        print("start is", nStart)    #debug to see if correctly constant random between runs (add # infront to deactivate)
        return rwpos(nStart, nstep - 1)


def rwsteps(start, low, hi):
    print("|", (start - low) * "_", "😴", (hi - start) * "_", "|")
    steps = 0
    if hi <= low:  # check if hi is larger then low
        return "low needs to be smaller then hi"
    elif low < 0 or hi < 0:  # check for no negative low
        return "no negatieve inputs!!!!"
    elif start == hi or start == low:
        return 0
    else:
        time.sleep(0.1)
        return (
            rwsteps(start + rs(), low, hi) + 1
        )  # +1 counts times it is run and when return 0 from elif above is run it does all +1 from the counts for amount of steps

def ave_signed_displacement(numtrials):
    lc = [rwpos_plain(0, 100) for x in range(numtrials)]
    average = sum(lc) / len(lc)
    return average

def ave_squared_displacement(numtrials):
    lc = [rwpos_plain(0, 100)**2 for x in range(numtrials)]
    average = sum(lc) / len(lc)
    return average

def rwpos_plain(start, nstep,):
    if nstep <= 0:
        return start
    else:
        nStart = start + rs() 
        return rwpos_plain(nStart, nstep - 1)
"""
    Om de gemiddelde totale afwijking voor een
    toevalsbeweging met 100 willekeurige stappen
    te berekenen, heb ik rwpos_plain
       

    Zorg dat je ave_signed_displacement en
    ave_squared_displacement beide ten minste één
    keer uitvoert en de gegevens en het gemiddelde
    hierin kopieert.
"""