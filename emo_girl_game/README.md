
# Emo Girl 


Remember Pocket Emo? The Flash Game where you create your own emo boy, dress him up, and take care of him? Well! Now it's back, and better than ever. This time though, now you can make your own emo girl. You can dress her up in all your favorite emo clothes, give her your favorite emo hairstyles, and interact with her!

## Test method description

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
