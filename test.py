import pytest
from io import StringIO
import sys
from PocketEmoGame import Hair, Outfit, Misc
import pygame


def capture_output(func, *args):
    captured = StringIO()
    sys.stdout = captured
    func(*args)
    sys.stdout = sys.__stdout__
    return captured.getvalue().strip()

def test_outfit_change_top():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    outfit = Outfit(screen)
    outfit.change_top("band tee")
    assert outfit.current_top == "band tee"

def test_outfit_change_bottom():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    outfit = Outfit(screen)
    outfit.change_bottom("ripped jeans")
    assert outfit.current_bottom == "ripped jeans"

def test_outfit_change_accessory():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    outfit = Outfit(screen)
    outfit.change_accessory("choker")
    assert outfit.current_accessory == "choker"