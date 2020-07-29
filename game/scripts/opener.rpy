# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

# Note that Ren'py does not take in to account order of files and treats the script as one large collection of scripts. 
# Labels are therefore global, so keep that in mind. 



label start:

# Letting the player decide their name. 
define pov = Character("[povname]")

""

python:
    povname = renpy.input("What is your name?")
    povname = povname.strip()

    if not povname:
         povname = "Default Guy"

"You feel the heavy weight of sleepiness weighing you down..."

# an alarm goes off in the background

# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.
show bg messy room
with dissolve

"You grabbed your phone laying face down on the bed."

"You knew where to press the stop alarm button by muscle memory alone."

pov "Finally, some silence..."

pov "..."

#play discord notif sound here

pov "......"

#play discord notif sound here 

pov "Huh?"

pov "What time is it...?"

"Flipping your phone over, you checked the time."

pov "..."

pov "3:15PM?!?"

pov "Shit!"

pov "I was supposed to hang out with the girls today... "

pov "I really shouldn't have stayed up so late..."

"You remember that all your friends were all doing something today."

"You were scheduled to meet them up by 12 o’clock..."

pov "...but now it's almost four."

"You let out a heavy sigh."

pov "Well, at least I know nobody's gonna be at the meeting place..."

"Unlocking your phone, you see that you have over 30 text messages and calls from many people."

"It pains you to think about how long they spent trying to reach you."

#phone rings 

pov "?"

"It's Flo. One of the girls you were supposed to hang out with today."

menu: 
     "Answer the phone?"

     "Answer.": 
          "You decided to answer the phone."
          # Please note that jumps don't alter the scene.
          jump flo_carla_opener

     "Don't answer.": 
          "You decided against answering the phone."

# This ends the game.

"You feel bad enough that you didn't go to the get together, so pretending like you ended up sleeping the entire day makes you feel a little better."

#another discord notification rings out.

pov "Huh?"

pov "I swear to god you're gonna make me act up"

return
