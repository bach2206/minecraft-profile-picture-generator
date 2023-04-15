
# import generate() from render.py
from render import generate
from io import BytesIO 
# Import requests
import requests
from PIL import Image
import os
from termcolor import colored

os.system('color')

# Print a cool welcome screen
print(colored("""
Welcome to the Minecraft profile picture generator!
""", 'red'))
# Ask for the username with a cool UI
username = input(colored("Enter the username: ", 'white'))
background_color = input(colored("Enter the background color (RGBA: Eg. 255,255,255): ", 'white'))
top_layer = input(colored("Enter if you want it to have a top layer (Y or N): ", 'white'))


def generatePage(username, background_color, top_layer):
    # Fetch https://api.mojang.com/users/profiles/minecraft/<username>
    # and get the UUID
    response = requests.get("https://api.mojang.com/users/profiles/minecraft/" + username)
    uuid = response.json()['id']

    # Fetch https://crafatar.com/skins/<uuid>
    # and get the skin data
    response = requests.get("https://crafatar.com/skins/" + uuid)
    # to image
    skin = Image.open(BytesIO(response.content))

    generate(
        skin,
        background_color,
        top_layer,
    ).save("result.png")

# If top is Yes, YES or yEs, generate the top layer
if top_layer.lower() == "no" or top_layer.lower() == "n":
    generatePage(username, background_color, False)
else:
    generatePage(username, background_color, True)
