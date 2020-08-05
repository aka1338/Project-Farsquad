# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

# Note that Ren'py does not take in to account order of files and treats the script as one large collection of scripts. 
# Labels are therefore global, so keep that in mind. 



label start:

# Letting the player decide their name. 
define pov = Character("[povname]")

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

"Even if you just threw on pants and a shirt, you knew that nobody was going to be at the meeting place."

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


"You feel bad enough that you didn't go to the get together, so pretending like you ended up sleeping the entire day makes you feel a little better."

#another discord notification rings out.

pov "Huh?"

#show a picture of discord here

"It's from Michelle."

"She's asking if you want to play that new shooting game that everyone's been playing."

"You try to remember the title."

"You think it was called Valiance."

menu: 
     "Respond?"

     "Yes.": 
          "You decided to respond back."
          # Please note that jumps don't alter the scene.
          # jump Michelle_Noella_opener

     "No.": 
          "You're pretty bad at shooting games, and the early morning grogginess give you yet another excuse to not have to suffer through an embarrassing 0-13 game."

pov "I guess everyone's already back home..."

"Considering that Michelle is already playing games at home, it makes sense everyone else would be, too."

"The thought of missing out makes you a little depressed."

# phone notification plays.

"You get a text on your phone. It's from Jo' Pauline. You know her as 'JP' for short."

"Height included."

"You take a look at the message through the app, but don't open it as to not accidentally send a read receipt."

"Hey! You okay? Everyone's been trying to reach you since you weren't the-"

"That's all you can manage to make out from the message unless you decide to open it up and read it."

menu: 
     "Open the rest of the message?"

     "Open it.": 
          "You decided check out the rest of the message."
          # Please note that jumps don't alter the scene.
          # jump JoPauline_Hira_opener

     "Don't open it.": 
          "Just like earlier, you decide inaction is the best action for now."

"It's starting to feel kind of funny that you have the power to deny all social interaction for today."

"You make your way downstairs to grab a drink, feeling awfully thirsty."

#change bg here to int kitchen 

"You make your way to the fridge and open it up, to find a whole box of Truthfully alcoholic seltzers stocked in the fridge. You wonder how that got there."

"There's a calender next to the fridge that you always update to stay on top of things for the week. Scheduled for tonight is 'Clubbing with the Girls.'"

"You realize what the drinks in the fridge were for- they were pregame drinks for clubbing tonight with your friends Jemina and Callie."

menu: 
     "Go clubbing tonight?"

     "Let's go!": 
          "You decide to try to go clubbing tonight."
          # Please note that jumps don't alter the scene.
          # jump Michelle_Noella_opener

     "Let's not go.":
           "You don't feel like getting sloshed tonight."

pov "just how many things am I going to miss today..."

"You take a look at the calenday onbe more time, and also realize that tonight is the release of that game everyone has been talking about."

"You don't have a preorder to grab the game at tonight's midnight release, but you do know of two other people that will be going for use."

"Your friends Selina and Jhin have been waiting for a whole year for it to come out, and your only chance of nabbing a copy tonight may lie with them."

"The night is free for you, for sure."

menu: 
     "Call up Selina and Jhin?"

     "Call them.": 
          "You decide to hit them up."
          # Please note that jumps don't alter the scene.
          # jump Michelle_Noella_opener

     "Don't call them.":
          "You're tired of looking at the calenday and decide that today is just one of those days."

"You feel bad for leaving your friends alone, but you have an excuse to do so today, anyways."

"You decide to head to the livingroom to snooze the rest of the day away with the TV on."

# change bg here to int livingroom. 

"You head for the couch and turn on the TV, open up your phone and decide to check ByteChat."

"There's a function to see where your friends are, and you notice that Eden is close."

"Like, really close. Outside of your window, apparently."

#play shuffling noise here, show window picture in time

"She's walking right by your house!"

"This is your last chance to be social for today."



menu: 
     "Call out her name?"

     "Call her out!": 
          pov "Eden!"
          # Please note that jumps don't alter the scene.
          # jump Michelle_Noella_opener

     "Say nothing.":
          "..."

"..."

"The opportunity slips by you. You're too tired, too lazy, and way too lethargic to commit to being social today."

"And well, that's alright."

"You turn back to the TV and see what's on."

pov "There's always tomorrow."

"As long as the world isn't ravaged by some rogue pandemic tomorrow, you'll always have the chance to see your friends again."

return
