
# Emo Girl 


Remember Pocket Emo? The Flash Game where you create your own emo boy, dress him up, and take care of him? Well! Now it's back, and better than ever. This time though, now you can make your own emo girl. You can dress her up in all your favorite emo clothes, give her your favorite emo hairstyles, and interact with her!

## Test method description

TO PLAY THE GAME:

Download all folders, including main_emo_girl.py. Load up the main_emo_girl.py file and run it in the terminal, making sure the assets folder is in the same main root folder as main_emo_girl.py. A window should pop up, allowing you to see the game. To see and interact with the buttons, you have to full screen the canvas. To save your avatar, press the save button. 

For this project, you'll need to use three Python libraries: Pillow, Pygame, and Tkinter. Here is how to install them and their 
roles in the project.

Pillow(PIL)-

Pillow is a Python Imaging Library used to handle image processing tasks like opening, resizing, and converting image formats.
In this project, it's used to load and resize clothing and character assets before displaying them in the interface.

To install Pillow, run this in your terminal:
pip install Pillow

Pygame-

Pygame is a Python library used for game development. In this project, it's used to load and play background music.

To install Pygame, run this in your terminal:
pip install Pygame

Tkinter-

Tkinter is Python’s standard GUI library, used to build graphical user interfaces. It’s used in this project to create buttons, 
a canvas for character images, and manage layout.

Tkinter usually comes pre-installed with Python, so you typically don't need to install it manually.

import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pygame
from tkinter import filedialog
from PIL import ImageGrab
### Button Interactions
 -We tested all four buttons (Change Hair, Change Top, Change Bottom, Change Accessory) to make sure they cycle through the correct options and update the canvas.<br>
 -Verified that the old item disappears when a new one is added (e.g., old hair is removed before the new one is placed).<br>

### Image Placement
 -We tested different outfits to confirm that each clothing item aligns correctly over the base image.<br>
 -Made sure images load at the right coordinates and the layering order looks visually correct.<br>

### Music Playback
 -Verified that background music begins when the program launches and loops continuously using Pygame.

### Screenshot Saving
 -We tested the screenshot functionality by entering a filename in the prompt and confirming the saved image matches the girl’s appearance.<br>
 -Checked that only the portion of the canvas with the girl is captured and the image is stored properly.

### Basic Functions: 
a. Load in the avatar 
b. Customize the avatar 
c. Save the avatar  

## Group Members
If you are doing a group project, the list of group members with both their real names and Github usernames. <br>
Isabella Machaj. Github-imachaj <br>
Tara Mirkov. Github- tmirkov


How work will be divided (assigned and tracked) among group members, and; How (and how often!) team members will communicate with each other about the project (such as weekly meetings, ongoing group chat, etc.) 

We live in the same dorm hall so we can meet with eachother whenever. We will help eachother write the code, but we will split the work to make it even. Any work done in the code can be labeled by the person with a note.

## Classes, Functions, Methods

### Classes

**Item**-
What it does: Loads a picture of clothing or hair and remembers what type it is (like top, hair, accessory) <br>
Used for: Adding things like tops or hairstyles to the girl <br>

**Girl**-
What it does: Holds the base girl and shows items on her <br>
Used for: Changing how the girl looks by putting images on her <br>

**EmoGame**-
What it does: Runs the whole game: screen, buttons, and how they work <br>

### Methods

**set_item(self, item)**-
Puts a new item on the girl <br>

**button methods**-
Switch to the next hairstyle, top, bottom, or accessory <br>

## Functions

**play_music()**-
Starts background music <br>

**save_screenshot()**-
Lets player type a name and saves a picture of the girl
