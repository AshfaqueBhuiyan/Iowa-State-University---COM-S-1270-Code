# Ash Bhuiyan                                               07-28-2025
# Lab 10 - This is a refactored version of the original chimp.py game.
#          The goal here is to apply OOP principles, such as inheritance, cleaner organization, 
#          and better error handling for resources.

# CITATION - chimp.py
# CITATION - Author: COM S 1270
# CITATION - Date Accessed: 07-28-2025

import os
import pygame

class Entity(pygame.sprite.Sprite):
    """
    A base class for game entities that handles loading and displaying an image.
    It simplifies sprite setup by doing the image loading inside the constructor.
    """
    def __init__(self, image_name, data_dir, colorkey=None, scale=1):
        super().__init__()

        image_path = os.path.join(data_dir, image_name)
        image = pygame.image.load(image_path).convert()

        if scale != 1:
            image = pygame.transform.scale_by(image, scale)

        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)

        self.image = image
        self.rect = self.image.get_rect()

def load_sound(name, data_dir):
    """
    Loads a sound file safely.
    If the file can't be loaded, it returns a silent fallback object instead of crashing the game.
    """
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer.get_init():
        return NoneSound()

    try:
        full_path = os.path.join(data_dir, name)
        sound = pygame.mixer.Sound(full_path)
        return sound
    except Exception as e:
        print(f"[Warning] Could not load sound '{name}': {e}")
        return NoneSound()

class Fist(Entity):
    """
    The Fist class represents the player's fist which follows the mouse.
    It inherits from Entity and updates its position based on mouse movement.
    """
    def __init__(self, data_dir):
        super().__init__("fist.png", data_dir, colorkey=-1, scale=1)
        self.fist_offset = (-235, -80)
        self.punching = False

    def update(self):
        """Update the fist's position to follow the mouse."""
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.fist_offset)
        if self.punching:
            self.rect.move_ip(15, 25)

    def punch(self, target):
        """Return True if the fist hits the target."""
        if not self.punching:
            self.punching = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        """Called to reset the punch state."""
        self.punching = False

class Chimp(Entity):
    """
    The Chimp class represents the monkey that walks across the screen.
    When punched, it spins around.
    """
    def __init__(self, data_dir):
        super().__init__("chimp.png", data_dir, colorkey=-1, scale=4)
        self.area = pygame.display.get_surface().get_rect()
        self.rect.center = (960, 360)
        self.move = 17
        self.dizzy = False

    def update(self):
        """Move the chimp or spin it depending on its state."""
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        """Move the chimp back and forth across the screen."""
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pygame.transform.flip(self.image, True, False)
        self.rect = newpos

    def _spin(self):
        """Spin the image to show dizziness."""
        center = self.rect.center
        self.dizzy = self.dizzy + 12
        if self.dizzy >= 360:
            self.dizzy = False
            self.image = self.original
        else:
            self.image = pygame.transform.rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        """Start the chimp spinning when hit."""
        if not self.dizzy:
            self.dizzy = True
            self.original = self.image

def main():
    """
    Sets up the game and runs the main loop.
    This version keeps everything inside this function to avoid global variables.
    """
    # Initialize Everything
    pygame.init()

    # Check if fonts and sounds are available (simple debugging info)
    if not pygame.font:
        print("Warning: Fonts are not available.")
    if not pygame.mixer:
        print("Warning: Sound is not available.")

    # Set up the window
    screen = pygame.display.set_mode((1280, 720), pygame.SCALED)
    pygame.display.set_caption("CHIMP REFACTOR")
    pygame.mouse.set_visible(False)

    # Figure out where the asset folder is
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")

    # Create The Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    # Put Text On The Background, Centered
    font = pygame.font.Font(None, 64)
    title = font.render("Punch The Chimp, and Win Rewards", True, (10, 10, 10))
    title_rect = title.get_rect(centerx=background.get_width() / 2, y=10)
    background.blit(title, title_rect)

    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    whiff_sound = load_sound("whiff.wav", data_dir)
    punch_sound = load_sound("punch.wav", data_dir)
    chimp = Chimp(data_dir)
    fist = Fist(data_dir)
    all_sprites = pygame.sprite.Group(chimp, fist)
    clock = pygame.time.Clock()
    running = True
    hits = 0
    misses = 0

    # Main Loop
    while running:
        clock.tick(60)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play()  # punch
                    chimp.punched()
                    hits += 1           # each punch will increase the score
                else:
                    whiff_sound.play()  # miss
                    misses += 1         # missed punch increases the miss count
            elif event.type == pygame.MOUSEBUTTONUP:
                fist.unpunch()

        all_sprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        # Show the Hit Points
        score_text = font.render(f"Hits: {hits}", True, (0, 0, 0))
        score_rect = score_text.get_rect(topright=(screen.get_width() - 20, 20))
        screen.blit(score_text, score_rect)
        # Show the Missed Points
        miss_text = font.render(f"Misses: {misses}", True, (0, 0, 0))
        miss_rect = miss_text.get_rect(topright=(screen.get_width() - 20, 80))
        screen.blit(miss_text, miss_rect)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

# Game Over

# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
