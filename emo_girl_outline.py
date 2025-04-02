class Hair: #tmirkov
    """Handles avatar's hair customization."""
    def change_hair_color(self, color: str):
        """Allows the player to change the avatar’s hair color."""
        pass
    
    def change_hair_style(self, style: str):
        """Allows the player to change the avatar’s hairstyle."""
        pass
    
    def change_hair_accessory(self, accessory: str):
        """Allows the player to add a hair accessory."""
        pass


class Outfit: #imachaj
    """Handles avatar's outfit customization."""
    def change_top(self, top: str):
        """Allows the player to change the avatar’s top."""
        pass
    
    def change_bottom(self, bottom: str):
        """Allows the player to change the avatar’s bottom."""
        pass
    
    def change_accessory(self, accessory: str):
        """Allows the player to change the avatar’s accessory."""
        pass


class Misc: #tmirkov and imachaj
    """Handles additional interactive features of the game."""
    def play_music(self, track: str):
        """Plays a song and affects the character’s mood."""
        pass
    
    def give_energy_drink(self, brand: str):
        """Gives the character an energy drink, boosting excitement."""
        pass



if __name__ == "__main__":
    hair = Hair()
    outfit = Outfit()
    misc = Misc()
    
    hair.change_hair_color("yellow")  # Expected: She sighs and says "Ugh, no. Black is better."
    outfit.change_top("bright pink crop top")  # Expected: She refuses to wear it.
    misc.play_music("Pierce the Veil - King for a Day")  # Expected: "Yesss, this is my jam! :D"
