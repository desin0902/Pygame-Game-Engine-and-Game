# Pygame-Project
A game engine and game built in pygame, aimed at practicing classes, objects, and splitting a project across multiple files for added modularity and simplified expansion. Drafted end-to-end and making the best possible use of superclasses and subclasses, global variables and modification through settings sliders, frontend UI elements. Forgive the art, I cobbled something workable together as a proof of concept.

Contents:

assets: A folder containing all non-code assets the game uses.
  img: An images folder containing all the sprites in the game, as well as backgrounds and transition screens.

  levels: The folder containing all of the tilemaps of the game, stored as .txt files. Easy to edit if you wish. B is for "block", G is for "gold block" (same function), P is       "player", E is "enemy", and F is "flag".

  sounds: A folder containing all of the sound effects and music for the game. All if it creative commons from freesound.org.

  Cantarell.ttf: The font used for the games restart button.

config.py: Contains values used repeatedly throughout the game to simplify variables, as well as a tilemap unpacker for simplified expansion of the game's maps.

icoimage.ico: The image file used for the icon for the game in windows explorer.

main.py: The main game file, containing the game's main loop and its different screens.

main.spec: The pyinstaller specification file for the game.

parents.py: Contains all of the superclasses for the most generic practical versions of all of the types in the game.

soundmanager.py: A sound manager to handle all of the sounds in the game. Fascilitates easy muting and unmuting.

sprites.py: Contains the different sprite classes in the game, the camera, collision detection, the button function, sound effects, and sprite animation management.

utils.py: Contains all of the classes and functions necessary for utilities, like UI elements and the camera.
