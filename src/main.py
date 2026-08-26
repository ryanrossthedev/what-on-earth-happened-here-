import os
import time
import random

global plr_name
onboarding_choice = input("Do you want to use your operating system's username as your player name? [Y/n] ")
if onboarding_choice == "Y":
    plr_name = os.getlogin()
else:
    plr_name = input("What should I call you? ")

print(f"Welcome {plr_name}! Please wait while the game loads...")
time.sleep(5)
