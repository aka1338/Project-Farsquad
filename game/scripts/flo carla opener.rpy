define c = Character("Carla")
define f = Character ("Flo")
define u = Character("???")

#TODO When art is recieved, make sure to add appropriate sprites. 

label flo_carla_opener:

pov "Hello?"

show flo phone at phonepos
with easeinbottom

f "Hey dude! Where were you?"

f "Are you okay?"

f "Do I need to be worried?"

f "Oh, man god I'm sorry."

f "I'm kind of high right now..."

"You can hear the sound of rustling in the background through the phone."

u "Dude, you're always high."

"It's the sound of a voice that's familiar, but you can't exactly make out who it is."

f "Shut up, you're high too!"

"You feel as if you could almost catch the high through the phone itself."

"More rustling noises makes its way through the phone. It sounds as if the phone is being passed to someone else."

u "Hey, you should come through!"

u "I didn't see you today, but me and Flo are hanging out at my house."

"You think for a second. The voice sounds familiar." 

pov "Carla? Is Flo over at your place?"

c "Oh, Flo didn't tell you? Yeah, we're at my place right now."

c "Nobody saw you today when we went out earlier. Did you oversleep or something?"

"You laughed nervously." 

"Feeling kind of guilty, you decided to see if you could use this chance to hang out."

pov "Yep. Completely slept through everything."

pov "But, I can come over. You don't mind if I come through?"

c "Do it!"

f "Yeah, do it!"

"Flo's voice seemed as if it were far off somewhere, and muffled."

c "Oh my god, he's coming over. Should I drive?"

pov "?"

"It sounded as if Carla turned her head away from the phone." 

"If she was attempting to make it so you couldn't hear her, it wasn't working."

f "I can drive."

c "Okay, no. You're not going to drive."

f "What do you mean I can't drive?"

"You could hear the two arguing over the phone."

"As Carla seemed to get more upset, Flo's laughter only seemed to grow."

"Just as things seemed as if they were going to reach a boiling point, you decided to interject."

pov "It's okay, I can drive."

c "..."

f "..."

c "Oh shit, is the phone still on?"

f "Yeah it is!"

"You could hear Flo laughing powerfully in the background."

c "Hey. [pov], I can drive you. It's okay."

c "Just wait right there!"

pov "Alright, alright. I'll stay here."

hide flo phone
with easeoutbottom

"Something about the entire ordeal makes you laugh."

"As the laughter subsides, you're overcome with something... overwhelming."

"You have a very bad feeling about this."

"But, the prospect of hanging with your friends excite you."

pov "Well, I guess I should go get ready."

scene black
with dissolve

scene bg kitchen
with dissolve

"You arrive at your kitchen after dressing up to grab something to drink before Flo and Carla get to your house."

"You take a look inside your fridge to find it filled with random food items and assorted drinks."

"There's at least a dozen raw vegetables covered in seran wrap, water in a mason jar for whatever reason, and what looks like to be a bottle of soda at the back of the fridge."

#phone rings
#pause 

show flo phone at phonepos
with easeinbottom

"That's probably Flo calling you."

hide flo phone
with easeinbottom

"Before answering, you decide to take a look out the window to see if they've arrived."

scene black
with dissolve

scene bg carla car outside
with dissolve

"On the way to the window, you realize that you didn't pick up the phone."

"But looking outside, you can clearly see a familiar car puttering on idle."

"All of a sudden, you're caught off guard by the smell of weed wafting over from the car."

"You try your best to pay it no mind."

"On closer inspection, you can see Flo, who is clearly high."

"Carla looks the same, as usual."

"You decide to head downstairs to greet them."

scene bg carla car closeup
with dissolve

"Before they can see you approach the car, you can overhear a conversation between the two."

"Which for some reason, is extremely loud."


c "Okay, don't fuck this up."


f "And don't mention the flowers in the back?"

f "{i}Who does that?{/i}"

"You can hear Flo fly into a fit of laughter."

c "I swear to god, Flo."

f "What?! He's kinda sexy though."

c "..."

f "..."

f "{i}I get it.{/i}"

c "Flo, you're being so fucking loud right now, I swear."

f "OKAYYYYYYYYYY!"

c "... Oh my god."

"You can still hear Flo laughing maniacally, as you begin to approach the car at what seems like a good time."

"When you get up to the car, you decide to block out the entire interaction you just heard, and wave at Flo, sitting in the passenger's seat."

pov "Hey, guys."

show carla happy at cpos1
with easeinleft

show flo happy at cpos2
with easeinleft

"Flo and Carla let an awkward silence pass by."

"Flo's eyes looked a bit glazed over."

f "I am."

f "So."

f "High."

f "Right now!"

c "That's what I said!"

"The both of them look at each other and laugh."

"By the looks of it, things seemed to have calmed down, at least."

pov "So, your place?"

c "My place. You ready?"

pov "That's fine with me."

"Before you have a chance to enter the car, Flo shoots you a smug look, as if ready to tell a joke."


menu: 
     f "Hey, [pov], are you {i}hot{/i} right now?"

     "Yeah, I don't know why I wore a hoodie today.": 
          f "Yeah, I don't know why you wore a hoodie either."
          f "Like, it's hot."
          f "You're hot."
          f "Haha..."
          pov "..."
          f "..."
          c "..."
          f "Kind of like how Selina talks about your hot dad!"
          f "Right? {i}Right?{/i}"
          "Another painful silence fills the air."
          c "God."
          c "You're a fucking moron."
          "Something about this entire interaction makes you feel slightly offended, but overwhelmed by laughter."

     "No, but you look pretty hot yourself.": 
          f "Oh."
          f "{i}Oh, shit.{/i}"
          f "..."
          c "..."
          f "You're beautiful."
          "Flo's eyes gaze awkwardly into yours, as if she were stuck in a trance."
          f "..."
          f "We have flowers in the back for you."
          c "FLO!!!"
          scene bg carla car closeup
          with vpunch
          "Carla's voice echoed down the street, startling both Flo and you."
          show carla happy at cpos1
          with dissolve
          show flo happy at cpos2
          with dissolve
          f "Yeah?"
          c "Why would you..."
          f "{i}OH YEAH, THAT'S A SECRET!{/i}"
          "Something about this entire interaction makes you feel slightly offended, but overwhelmed by laughter."
          $flag1 = True

"You motion to Flo to let you get into the car, who stumbles out of the front seat to let you into the back."

"You realize that your head practically hits the roof of the car when you sit upright."

"Flo and Carla are caught up in another conversation, as you lay back into your seat."

"You know that the ride to Carla's place is realtively short. But, you feel as if it will take a long, long time."

hide carla 
with easeoutleft

hide flo
with easeoutright

#scene bg outside carlas house
#with dissolve 

show carla happy at cpos1
with easeinleft

c "...And welcome to my place!"

"Cozy. Haven't been here for a while."

c "I know, right?"

show carla happy 
with easeoutleft


return