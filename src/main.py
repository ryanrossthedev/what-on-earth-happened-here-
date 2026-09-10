import os
import time
import random
from pathlib import Path
logo = r"""
__        ___   _    _  _____    ___  _   _   _____    _    ____ _____ _   _ 
\ \      / / | | |  / \|_   _|  / _ \| \ | | | ____|  / \  |  _ \_   _| | | |
 \ \ /\ / /| |_| | / _ \ | |   | | | |  \| | |  _|   / _ \ | |_) || | | |_| |
  \ V  V / |  _  |/ ___ \| |   | |_| | |\  | | |___ / ___ \|  _ < | | |  _  |
   \_/\_/  |_| |_/_/   \_\_|    \___/|_| \_| |_____/_/   \_\_| \_\|_| |_| |_|
 _   _    _    ____  ____  _____ _   _ _____ ____                            
| | | |  / \  |  _ \|  _ \| ____| \ | | ____|  _ \                           
| |_| | / _ \ | |_) | |_) |  _| |  \| |  _| | | | |                          
|  _  |/ ___ \|  __/|  __/| |___| |\  | |___| |_| |                          
|_| |_/_/   \_\_|   |_|   |_____|_| \_|_____|____/                           
 _   _ _____ ____  _____ ___                                                 
| | | | ____|  _ \| ____|__ \                                                
| |_| |  _| | |_) |  _|   / /                                                
|  _  | |___|  _ <| |___ |_|                                                 
|_| |_|_____|_| \_\_____|(_)                                                 
"""

global plr_name
onboarding_choice = input("Do you want to use your operating system's username as your player name? [Y/n] ")
if onboarding_choice == "Y":
    plr_name = os.getlogin()
else:
    plr_name = input("What should I call you? ")

print(f"Welcome {plr_name}! Please wait while the game loads...")
time.sleep(2)

def get_version():
    # Path() automatically fixes the dots and slashes for Windows
    path = Path("./info/CHANGELOG.md")
    
    # opens said file
    with open(path, "r", encoding="utf-8") as file:
        # reads the first line of CHANGELOG.md
        version = file.readline().strip()

    return version

# define variables
npcs = {}
global npcs_dead
npcs_dead = 0
global plr_alive
plr_alive = True
global plr_arrested
plr_arrested = False

# Loads NPC varients that the Murderer can encounter
def npc_service(load_npcs=False):
    npcs = {
        "NPC01": {"name": "Abbey", "role": "Innocent"},
        "NPC02": {"name": "Karen", "role": "Karen"},
        "NPC03": {"name": "Ryan", "role": "Innocent"},
        "NPC04": {"name": "Max", "role": "Innocent"},
        "NPC05": {"name": "Eagle", "role": "Constable"},
        "NPC06": {"name": "Leo", "role": "Innocent"},
        "NPC07": {"name": "Bryan", "role": "Innocent"},
        "NPC08": {"name": "Derrick", "role": "Innocent"},
        "NPC09": {"name": "Jackson", "role": "Innocent"},
        "NPC10": {"name": "Sophie", "role": "Artist"}
    }
    return npcs

# Fetches the names for each NPC in the NPC dictionary
def get_npcs(npcs_var):
    for npc in npcs_var.values():
        print(npc["name"])

def main(plr_alive, plr_arrested, npcs_dead, npcs_var):
        print(f"Initiating game round...")
        print(f"Welcome {plr_name}. Your objective is to murder as many people you can without getting caught. Some NPCs might be a tiny bit more vigilent than others, so be careful. Good luck.")
        while plr_alive == True:
            # Establishs an NPC that the player can either attempt to murder or abstain from murdering
            npc_target = random.choice(list(npcs_var.values()))
            # Checks to see iof the NPC is the Constable varient.
            if npc_target == "NPC05":
                choice = input("It is nighttime. You've spotted someone going for a late night walk. Are you going to try murder them? [Y/n] ")
                if choice == "Y":
                    if int(random.randint(1, 3)) == 1:
                        time.sleep(1)
                        plr_alive = False
                        plr_arrested = True
                        print(f"Oops. You tried to murder a Constable and you failed to silence them. You were arrested. You sucessfully murdered {npcs_dead} people!")
                        return plr_alive
                    else:
                        print("You successfully murdered a Constable without getting arrested.")
                        time.sleep(1)
                        npcs_dead = npcs_dead + 1
                        print(f"You've currently murdered {npcs_dead} people.")
                else:
                    print("You didn't murder anyone.")
            elif npc_target == "NPC02":
                            choice = input("It is nighttime. You've spotted someone going for a late night walk. Are you going to try murder them? [Y/n] ")
                            if choice == "Y":
                                if int(random.randint(1, 3)) == 1:
                                    time.sleep(1)
                                    plr_alive = False
                                    plr_arrested = True
                                    print(f"Oops. You tried to murder Karen. She asked to speak to your manager and you died of cringe. You sucessfully murdered {npcs_dead} people!")
                                    return plr_alive
                                else:
                                    print("You murdered Karen. She'll be asking to see heaven's manager now...")
                                    time.sleep(1)
                                    npcs_dead = npcs_dead + 1
                                    print(f"You've currently murdered {npcs_dead} people.")
                            else:
                                print("You didn't murder anyone.")
            elif npc_target == "NPC10":
                            choice = input("It is nighttime. You've spotted someone going for a late night walk. Are you going to try murder them? [Y/n] ")
                            if choice == "Y":
                                if int(random.randint(1, 3)) == 1:
                                    time.sleep(1)
                                    plr_alive = False
                                    plr_arrested = True
                                    print(f"Oops. You tired to murder Sophie the Artist.She sat you down and made you wait for a goofy ahh portrait of yourself for so long, you died of an uneventful heart attack. You sucessfully murdered {npcs_dead} people!")
                                    return plr_alive
                                else:
                                    print("You murdered Sophie the Artist. What a shame.")
                                    time.sleep(1)
                                    npcs_dead = npcs_dead + 1
                                    print(f"You've currently murdered {npcs_dead} people.")
                            else:
                                print("You didn't murder anyone.")
            else:
                choice = input("It is nighttime. You've spotted someone going for a late night walk. Are you going to try murder them? [Y/n] ")
                if choice == "Y":
                    if int(random.randint(1, 15)) == 1:
                        time.sleep(1)
                        plr_alive = False
                        print(f"You tried to murder an innocent and they got away. You were found out. You successfully murdered {npcs_dead} people!")
                        return plr_alive
                    else:
                        print("You successfully murdered an Innocent!")
                        time.sleep(1)
                        npcs_dead = npcs_dead + 1
                        print(f"You've currently murdered {npcs_dead} people.")
                else:
                    print("You didn't murder anyone.")

npcs_var = npc_service(load_npcs=True)
get_npcs(npcs_var)
print(logo)
version2 = get_version()
print(version2)
time.sleep(2)
print(f"Welcome {plr_name}.")
print(f"The objective of this game is to keep murdering people for as long as you can until you eventually get caught. Further insturctions will be provided.")
input("Press any key to continue.")
print("The game will start shortly. Please exit the script if you do not wish to continue... (5)")
time.sleep(1)
print("The game will start shortly. Please exit the script if you do not wish to continue... (4)")
time.sleep(1)
print("The game will start shortly. Please exit the script if you do not wish to continue... (3)")
time.sleep(1)
print("The game will start shortly. Please exit the script if you do not wish to continue... (2)")
time.sleep(1)
print("The game will start shortly. Please exit the script if you do not wish to continue... (1)")
time.sleep(1)
print("The game will start shortly. Please exit the script if you do not wish to continue... (0)")
time.sleep(1)
main(plr_alive, plr_arrested, npcs_dead, npcs_var)
