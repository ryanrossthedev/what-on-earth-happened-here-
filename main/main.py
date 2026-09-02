import os
import time
import random
import json

global plr_name
onboarding_choice = input("Do you want to use your operating system's username as your player name? [Y/n] ")
if onboarding_choice == "Y":
    plr_name = os.getlogin()
else:
    plr_name = input("What should I call you? ")

print(f"Welcome {plr_name}! Please wait while the game loads...")
time.sleep(2)

global npcs
npcs = []

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


plr_chance = int(random.randint(0, 10))
if plr_chance == 1:
    plr_role = "Murderer"
elif plr_chance == 2:
    plr_role = "Constable"
else:
    plr_role = "Innocent"
print(f"You are {plr_role}")

npc_service(load_npcs=True, plr_role=plr_role)
# get_npcs(npcs)