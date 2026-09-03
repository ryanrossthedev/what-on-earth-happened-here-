import os
import time
import random
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
npcs = {}
def npc_service(load_npcs=False, plr_role=False):
    if load_npcs and plr_role == "Murderer":
            npcs = {
                "NPC01": {"name": "Abbey", "role": "Innocent"},
                "NPC02": {"name": "Garry", "role": "Innocent"},
                "NPC03": {"name": "Ryan", "role": "Innocent"},
                "NPC04": {"name": "Max", "role": "Innocent"},
                "NPC05": {"name": "Eagle", "role": "Constable"},
                "NPC06": {"name": "Leo", "role": "Innocent"},
                "NPC07": {"name": "Bryan", "role": "Innocent"},
                "NPC08": {"name": "Derrick", "role": "Innocent"},
                "NPC09": {"name": "Jackson", "role": "Innocent"},
                "NPC10": {"name": "Sophie", "role": "Innocent"}
            }
            return npcs
    elif load_npcs and plr_role == "Constable":
            npcs = {
                "NPC01": {"name": "Abbey", "role": "Innocent"},
                "NPC02": {"name": "Garry", "role": "Murderer"},
                "NPC03": {"name": "Ryan", "role": "Innocent"},
                "NPC04": {"name": "Max", "role": "Innocent"},
                "NPC05": {"name": "Eagle", "role": "Innocent"},
                "NPC06": {"name": "Leo", "role": "Innocent"},
                "NPC07": {"name": "Bryan", "role": "Innocent"},
                "NPC08": {"name": "Derrick", "role": "Innocent"},
                "NPC09": {"name": "Jackson", "role": "Innocent"},
                "NPC10": {"name": "Sophie", "role": "Innocent"}
            }
            return npcs
    elif load_npcs and plr_role == "Innocent":
            npcs = {
                "NPC01": {"name": "Abbey", "role": "Innocent"},
                "NPC02": {"name": "Garry", "role": "Innocent"},
                "NPC03": {"name": "Ryan", "role": "Innocent"},
                "NPC04": {"name": "Max", "role": "Innocent"},
                "NPC05": {"name": "Eagle", "role": "Constable"},
                "NPC06": {"name": "Leo", "role": "Innocent"},
                "NPC07": {"name": "Bryan", "role": "Innocent"},
                "NPC08": {"name": "Derrick", "role": "Innocent"},
                "NPC09": {"name": "Jackson", "role": "Murderer"},
                "NPC10": {"name": "Sophie", "role": "Innocent"}
            }
            return npcs
    return {}

def get_npcs(npcs_var):
    for npc in npcs_var.values():
        print(npc["name"])

plr_chance = int(random.randint(0, 10))
if plr_chance == 1:
    plr_role = "Murderer"
elif plr_chance == 2:
    plr_role = "Constable"
else:
    plr_role = "Innocent"
print(f"You are {plr_role}")

npcs_var = npc_service(load_npcs=True, plr_role=plr_role)
get_npcs(npcs_var)

print(logo)
time.sleep(5)
print(f"Welcome {plr_name}.")
print(f"The objective of this game is quite simple. As you could probably tell, this game is a Murder Mystery game. If you are Innocent, try your very best not to get murdered. If you are the Constable, you need to arrest the Murderer without messing up. And finally, if you are the Murderer... you need to get rid of every player until you are the last standing.")
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
