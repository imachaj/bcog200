Remember Pocket Emo? The Flash Game where you create your own emo boy, dress him up, and take care of him? Well! Now it's back, and better than ever. This time though, now you can make your own emo girl. You can dress her up in all your favorite emo clothes, give her your favorite emo hairstyles, and interact with her! 

Test method description: Running the file should show the title screen, the the main screen. Click the buttons on the GUI to test button functionality. Test the save feature when done. No user input is required.

Classes, Functions, Methods

Hair class #tmirkov

   change_hair_color(color: str)
	Description: allows the player to change the hair color of the avatar

	Parameters: the color of the hair is stored as a string
		-different colors have different effects on the avatar 

   change_hair_style(style: str)
	Description: allows the player to change the hair color of the avatar

	Parameters: the style is stored as a string
		-different styles have different effects on the avatar

   change_hair_accessory(accessory: str)
	Description: allows the player to change the hair color of the avatar

	Parameters: the accessory option is stored as a string
		-different accessories have different effects on the avatar

Example Use: change_hair_color("yellow")  #She sighs and says "Ugh, no. Black is better."

Outfit class #imachaj

  change_top(top: str)
	Description: allows the player to change the top


  change_bottom(bottom: str)
	Description: allows the player to change the bottom


  change_accessory(accessory: str)
	Description: allows the player to change the accessory


Misc class #tmirkov and imachaj collab

 play_music(track: str)
	Description: plays a song and affects the characters mood

	Parameters: track (string): name of song (e.g. Pierce the Veil: Caraphernelia) 

Example use: If the song is good, her happiness increases. If not, she gets extra moody.

give_energy_drink(brand: str) 
Description: Gives the character an energy drink, boosting excitement.

Parameters:
-brand(string): Name of the drink (e.g. “Monster”, “Red Bull”)


Example use:  If “Monster” is chosen, she says "yayy :D". If “Red Bull” she side eyes you

