# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Flo")
define c = Character("Carla")

# The game starts here.

# Note that Ren'py does not take in to account order of files and treats the script as one large collection of scripts. 
# Labels are therefore global, so keep that in mind. 

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg test
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show flo happy at cpos1
    with dissolve

    show carla happy at cpos2
    with dissolve 
 
    f "This is kind of embarrassing..."

    # These display lines of dialogue.

    f "So, where we droppin' chief?"

    f "don't make me say it"


    # This ends the game.

    return
