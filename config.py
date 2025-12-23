# Constants and configuration
import pygame
import os

# Screen dimensions
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
OCEAN_BLUE = (20, 50, 100)
DEEP_BLUE = (10, 30, 70)
WAVE_BLUE = (40, 80, 140)
BUTTON_COLOR = (180, 50, 50)
BUTTON_HOVER = (220, 80, 80)
BUTTON_SHADOW = (100, 30, 30)
SETTINGS_BTN = (70, 130, 180)
SETTINGS_HOVER = (100, 160, 210)
SETTINGS_SHADOW = (40, 80, 120)
GREEN = (50, 200, 50)
RED = (200, 50, 50)
GRID_LINE = (100, 150, 200)
CELL_EMPTY = (40, 80, 140)
CELL_HOVER = (80, 120, 180)
SHIP_COLOR = (100, 100, 100)
SHIP_HOVER = (150, 150, 150)
SHIP_PLACED = (80, 80, 80)
SHIP_INVALID = (200, 100, 100)
GRAY = (128, 128, 128)
HIT_RED = (255, 50, 50)
MISS_GRAY = (150, 150, 150)
YELLOW = (255, 255, 0)
DARK_RED = (150, 0, 0)
PIXEL_GREEN = (0, 255, 0)

# Game settings
DEFAULT_SFX_VOLUME = 0.5
DEFAULT_MUSIC_VOLUME = 0.5
DEFAULT_DIFFICULTY = "Easy"
DEFAULT_GAME_RULE = "Streak"
DEFAULT_SHIPS_NO_TOUCH = False

# Ship definitions
SHIPS = [
    ("Carrier", 5),
    ("Battleship", 4),
    ("Cruiser", 3),
    ("Submarine", 3),
    ("Destroyer", 2)
]

# Font sizes
TITLE_FONT_SIZE = 90
BUTTON_FONT_SIZE = 45
SMALL_FONT_SIZE = 30
TINY_FONT_SIZE = 24
MINI_FONT_SIZE = 18

# Paths (update these to match your actual paths)
ASSETS_DIR = r"D:\Battleship Assets"
AUDIO_DIR = r"D:\Battleship Assets\Audio"
SHIPS_DIR = r"D:\Battleship Assets\Ships"
VIDEO_DIR = r"D:\Battleship Assets\Videos"

# Button sound path
BUTTON_SOUND_PATH = r"C:\Users\world\AAST Workspace\Battleship\Assets\Audio\ButtonPress.mp3"

# Audio paths
HIT_SOUND_PATH = r"C:\Users\world\AAST Workspace\Battleship\Assets\Audio\HitSound.mp3"
MISS_SOUND_PATH = r"C:\Users\world\AAST Workspace\Battleship\Assets\Audio\MissSound.mp3"
BATTLE_MUSIC_PATH = r"C:\Users\world\AAST Workspace\Battleship\Assets\Audio\BattleMusic.mp3"
MAIN_MENU_MUSIC_PATH = r"D:\Battleship Assets\Audio\ArtOfWar.mp3"

# Explosion sprite paths
EXPLOSION_SPRITES = [
    r"C:\Users\world\AAST Workspace\Battleship\Assets\Sprite\Explosion_1.png",
    r"C:\Users\world\AAST Workspace\Battleship\Assets\Sprite\Explosion_2.png",
    r"C:\Users\world\AAST Workspace\Battleship\Assets\Sprite\Explosion_3.png",
    r"C:\Users\world\AAST Workspace\Battleship\Assets\Sprite\Explosion_4.png",
    r"C:\Users\world\AAST Workspace\Battleship\Assets\Sprite\Explosion_5.png",
    r"C:\Users\world\AAST Workspace\Battleship\Assets\Sprite\Explosion_6.png",
    r"C:\Users\world\AAST Workspace\Battleship\Assets\Sprite\Explosion_7.png",
    r"C:\Users\world\AAST Workspace\Battleship\Assets\Sprite\Explosion_8.png",
    r"C:\Users\world\AAST Workspace\Battleship\Assets\Sprite\Explosion_9.png",
    r"C:\Users\world\AAST Workspace\Battleship\Assets\Sprite\Explosion_10.png"
]

# Grid settings
GRID_ROWS = 10
GRID_COLS = 10
CELL_SIZE = 35
BATTLE_CELL_SIZE = 28

# Title screen settings
TITLE_FADE_IN_DURATION = 2.0
TITLE_DISPLAY_DURATION = 3.0
TITLE_FADE_OUT_DURATION = 1.5

# Explosion animation settings
EXPLOSION_FRAME_DURATION = 0.1  # seconds per frame

# AI delay settings
AI_MIN_DELAY = 0.5  # seconds
AI_MAX_DELAY = 1.5  # seconds

# Loading screen countdown
COUNTDOWN_DURATION = 10  # seconds

# Font paths (add pixel font)
try:
    # Try to load pixel font
    PIXEL_FONT = "C:\\Windows\\Fonts\\PressStart2P-Regular.ttf"
    if not os.path.exists(PIXEL_FONT):
        # Fallback to any pixel font
        PIXEL_FONT = None
except:
    PIXEL_FONT = None