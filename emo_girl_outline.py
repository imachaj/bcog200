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
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)
        self.current_top = ""
        self.current_bottom = ""
        self.current_accessory = ""
        self.buttons = {
            "Top: Band Tee": pygame.Rect(50, 50, 200, 40),
            "Top: Bright Pink": pygame.Rect(50, 100, 200, 40),
            "Bottom: Ripped Jeans": pygame.Rect(50, 150, 200, 40),
            "Bottom: Khakis": pygame.Rect(50, 200, 200, 40),
            "Accessory: Choker": pygame.Rect(50, 250, 200, 40),
            "Accessory: Pearls": pygame.Rect(50, 300, 200, 40),
        }

    def draw_buttons(self):
        self.screen.fill((0, 0, 0))
        for label, rect in self.buttons.items():
            pygame.draw.rect(self.screen, (80, 80, 80), rect)
            text = self.font.render(label, True, (255, 255, 255))
            self.screen.blit(text, (rect.x + 10, rect.y + 5))

    def display_message(self, message: str):
        self.draw_buttons()
        text = self.font.render(message, True, (255, 0, 255))
        self.screen.blit(text, (50, 400))

    def change_top(self, top: str):
        self.current_top = top
        if top.lower() == "bright pink crop top":
            self.display_message("She refuses to wear it.")
        elif top.lower() == "band tee":
            self.display_message("Nice, but only if it's MCR.")
        else:
            self.display_message(f"Changed top to {top}.")

    def change_bottom(self, bottom: str):
        self.current_bottom = bottom
        if bottom.lower() == "khaki shorts":
            self.display_message("Do I look like a prep?")
        else:
            self.display_message(f"Changed bottom to {bottom}.")

    def change_accessory(self, accessory: str):
        self.current_accessory = accessory
        if accessory.lower() == "choker":
            self.display_message("Edgy. I like it.")
        elif accessory.lower() == "pearl necklace":
            self.display_message("What am I, a grandma?")
        else:
            self.display_message(f"Added accessory: {accessory}.")



class Misc: #tmirkov and imachaj
    """Handles additional interactive features of the game."""
    def play_music(self, track: str):
        """Plays a song and affects the character’s mood."""
        pass
    
    def give_energy_drink(self, brand: str):
        """Gives the character an energy drink, boosting excitement."""
        pass



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pocket Emo")
    clock = pygame.time.Clock()

    background_image = pygame.image.load("bedroom_background.png")
    background_image = pygame.transform.scale(background_image, (640, 480))

    emo_girl_image = pygame.image.load("emo_girl_base.png")
    emo_girl_image = pygame.transform.scale(emo_girl_image, (150, 200))

    outfit = Outfit(screen)
    misc = Misc(screen)
    hair = Hair()
    running = True

    while running:
        screen.blit(background_image, (0, 0))
        screen.blit(emo_girl_image, (245, 150))
        outfit.draw_buttons()
        misc.draw_buttons()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for label, rect in outfit.buttons.items():
                    if rect.collidepoint(mouse_pos):
                        if "Band Tee" in label:
                            outfit.change_top("band tee")
                        elif "Bright Pink" in label:
                            outfit.change_top("bright pink crop top")
                        elif "Ripped Jeans" in label:
                            outfit.change_bottom("ripped jeans")
                    


        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
