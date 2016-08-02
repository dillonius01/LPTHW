from sys import exit 

items = [] 
feedback = "Eh? Try something else."
p = "> "

def sith():
	print "Here is the big boss, Mr. Shadow."
	print "He, or it, is a mix of Iago, Darth Vader, and Sauron."
	print "What do you do?"
	
	while True:
		choice = raw_input(p)
	
		if 'attack' in choice:
			dead('No weapon is a match for Mr. Shadow.')
		elif 'dust' in choice and 'dust' in items:
			dead('Mr. Shadow is angered by your use of dust and he rips you apart.')
		elif 'give up' in choice:
			dead('Never give up. Never surrender.')
		elif choice == 'say hello':
			print 'Mr. Shadow has a lot to share about his feelings.'
			print 'You know, he was not threatening you in any way.'
			print 'Great job, you win!'
			exit(0)
		else:
			print feedback
				

def sharks():
	print "The pirates seem to have left your ship."
	print "The hull is rammed from the outside."
	print "You know this means one thing: space sharks."
	print "What do you do?"
	
	while True:
		choice = raw_input(p)
		
		if 'abandon' in choice:
			print "You make for an escape pod."
			print "But you are eaten by a massive space shark."
			print "In its belly, you are not alone..."
			raw_input()
			sith()
		elif 'fight' in choice:
			dead('You are no match for the sharks, which tear you apart.')
		elif 'run away' in choice:
			dead('No one can escape the sharks. They attack your ship and you are sucked into outer space.')
		else:
			print feedback
			
		
def shelob():
	print "You awake to find yourself tightly wound in a sticky, elastic substance."
	print "There is a foul odor about this place."
	print "Out of the corner of your eye, you see a massive eight-legged creature."
	print "What do you do?"
	
	while True:
		choice = raw_input(p)
		
		if 'attack' in choice and 'bow' in items:
			print "You are somehow able to shoot an arrow off, which hits the spider in the brain."
			print "The web melts from your body, but the cave is disintegrating around you..."
			raw_input()
			sith()
		elif 'attack' in choice and 'sword' in items:
			print "You stab the Shelob and cut yourself free from the web."
			print "But now the cave disintegrates around you..."
			raw_input()
			sith()
		elif 'dust' in choice and 'dust' in items:
			print "Clever girl! You use the dust to put the spider to sleep."
			print "You are able to wiggle free from the web, but the cave begins to disintegrate aroudn you..."
			raw_input()
			sith()
		elif 'attack' in choice and 'bow' not in items and 'sword' not in items:
			dead('You have no weapons to attack with. The spider gnaws you alive.')
		else:
			dead('That does not work, and the spider eats you alive.')
			

def macbeth():
	print "Outside the castle, you are approached by three ugly witches."
	print "They are stirring some funky cauldron."
	print "They ask if you prefer toil, trouble, or rubble."
	print "What is your response?"
	
	while True:
		choice = raw_input(p)
		
		if 'toil' in choice:
			print "You are overcome by the funky smell..."
			raw_input()
			shelob()
		elif 'trouble' in choice:
			print "The witches cackle."
			print "From the castle, you hear a guttoral screech..."
			raw_input()
			sith()
		elif 'rubble' in choice:
			dead('The witches turn you to stone, then break you apart into a thousand bits.')
		else:
			print feedback
			

def pirates():
	print "You spot a ship dead ahead. It has a skull and crossbones painted on the hull."
	print "Your ship is immobile. The pirates dock and prepare to board your ship."
	print "What do you do?"
	
	choice = raw_input()
		
	if "hide" in choice:
		print "You find a compartment in which to hide yourself and Chewbacca."
		print "Outside, you hear the pirates walking around your ship."
		print "Then, there are screams. 'Look, they\'re coming right for us!' they say..."
		raw_input()
		sharks()
	else:
		dead("The pirates shoot you on sight.")


def henryiv():
	print "You are standing amongst many knights of the realm."
	print "They ask if you would like some mead."
	print "How do you answer?"
	
	while True:
		choice = raw_input(p)
		
		if choice == "Y":
			print "You get drunk with the knights. Nice!"
			print "One of them gives you his sword. Sweeeeet."
			items.append("sword")
			print "The army is moving out to seige a nearby castle."
			print "You're drunk so you cannot refuse."
			raw_input()
			macbeth()
		elif choice == "N":
			dead("They get mad at you and stab you in the gut.")
		else:
			print feedback


def gondor(i):
	if i == 0:
		print "You and the knights arrive outside the gates of Minas Tirith."
		print "The knights join the already massive army assembled outside the city."
	elif i == 1:
		print "The eagle lands outside the gates of Minas Tirith."
		print "She places you near a massive army assembled outside the city."
	elif i == 2:
		print "Mustardseed brings you to earth outside the gates of Minas Tirith."
		print "Here is a massive army assembled outside the city."
		print "Mustardseed sprinkles more fairy dust on you, and you can once again move."
		print "She also gives you a jar of the fairy dust. Nice!"
		items.append('dust')
	print "You hear a gruesome yell as a battalion of orcs emerges from across the plain."
	print "The battle is to begin. What do you do?"
	
	while True:
		choice = raw_input(p)
		
		if "attack" in choice and "bow" in items:
			print "You use your bow to kill many orcs."
			print "However, you are hit in the head during the melee."
			print "You fall to the ground unconscious..."
			raw_input()
			shelob()
		elif "fight" in choice and "bow" not in items:
			dead("You try to punch an orc but she eats your face off.")
		elif "flee" in choice or "run" in choice:
			print "You escape the battle but are hit in the head by a stray hammer."
			print "You fall to the ground unconscious..."
			raw_input()
			shelob()
		elif "dust" in choice:
			dead("As you bring the dust out of the jar, you are pushed into it and it paralyzes you. The orcs eat you alive.")
		else:
			print feedback
	

def black_hole():
	print "Your spaceship is being pulled into the gravitational pull of a massive collapsed star."
	print "The ship is known for making the Kessel Run in record time."
	print "However, it's unclear if you can escape the gravitational pull of the black hole."
	print "The numbers on your throttle go from 0 to 10. How much gas do you give it?"
	
	while True:
		choice = raw_input(p)
		
		try:
			throttle = int(choice)
		except:
			print "Man, learn to type a number!"
			black_hole()
		
		if throttle >=0 and throttle <=2:
			print "The gravitational pull of the black hole pulls your ship in."
			print "You are transported across dimensions..."
			raw_input()
			henryiv()
		elif throttle >2 and throttle <8:
			dead("The thrusters fire but your ship isn't going fast enough to escape the black hole. The added stress of engine burn causes the ship to explode.")
		elif throttle >=8 and throttle <=10:
			print "The ship rumbles near top speed, and you barely escape the gravitational pull."
			print "However, your thrusters are overheated, so you drift at constant velocity through space..."
			raw_input()
			pirates()
		else:
			print "Try that again, chief."
	

def amsnd():
	print "You are in a forest meadow surrounded by glowing fairies."
	print "One named Mustardseed approaches you and asks if you would like a drink of wine."
	print "What do you do?"
		
	consent = False
	while True:
		choice = raw_input(p)
		
		if "drink" in choice:
			print "You get drunk with the fairies. Nice!"
			print "The cherub convinces you to dance, so you do until your head spins."
			print "After some time, you lay down for a nap beside a tree..."
			raw_input()
			macbeth()
		elif "kiss fairy" in choice and consent == False:
			dead("What, you think you can kiss a fairy without asking? She blows your genitals off.")
		elif "say hello" in choice and consent == False:
			print "The fairy smiles and says you can kiss her if you like."
			consent = True
		elif "kiss fairy" in choice and consent == True:
			print "You kiss Mustardseed, and it's awesome. Nice!"
			print "She sprinkles fairy dust on you, making you immobile."
			print "'Come, we must make for the walled city', she says..."
			raw_input()
			gondor(2)
		elif "sex" in choice and consent == True:
			print "The fairy thinks you got too frisky. She knocks you over the head and you feel the world spin around you..."
			raw_input()
			tatooine()
		else:
			print feedback
	
def forest():
	print "Your party reaches a clearing in the forest."
	print "From behind the trees and above, a band of elves appears with arrows knocked."
	print "Their leader approaches the dwarves and demands they lay down their axes."
	print "What do you do?"
		
	while True:
		choice = raw_input(p)
		
		if "attack" in choice or "run away" in choice or "taunt" in choice:
			dead("You anger the elves, who shoot you in the face and crotch.")
		elif "hello" in choice and "bow" not in items:
			print "The elves are impressed with your kindness and give you a bow and arrows. Nice!"
			items.append("bow")
		elif "hello" in choice and "bow" in items:
			dead("As you say hello a second time, the dwarves attack the elves, and you are shot and hacked in the ensuing melee.")
		elif "climb" in choice:
			print "You duck behind a tree as the dwarves and elves continue their standoff."
			print "From above, an enormous eagle swoops down. Do you get on?"
				
			while True:
				choice2 = raw_input(p)
				
				if choice2 == "Y":
					print "The eagle takes you on her back and flies south."
					print "In the distance, you see a city surrounded by glistening white walls..."
					raw_input()
					gondor(1)
				elif choice2 == "N":
					print "The eagle flys off without you, and the power of her wings pushes you off the tree."
					print "You feel yourself falling, falling, further than where the ground once was..."
					raw_input()
					henryiv()
				else:
					print feedback
		else:
			print feedback
	
	
def moria():
	print "You have entered the mines of MORIA!"
	print "A cave troll is standing in front of the passageway forward. What do you do?"
	
	moved = False
	while True:
		choice = raw_input(p)
				
		if "attack" in choice:
			dead("You have no weapons. The troll smashes you under his foot.")
		elif "taunt troll" in choice and not moved:
			print "You get the troll to move away from the entrance."
			moved = True
		elif "taunt troll" in choice and moved:
			dead("You anger the troll, who picks you up and gnaws your face off.")
		elif "go" in choice and moved:
			print "The passageway free, you run ahead, emerging from the caves into a forest opening..."
			raw_input()
			forest()
		else:
			print feedback
	
	
def rohan():
	print "As the sun falls below the horizon, you and the riders enter a stretch of flatlands with a castle rising on a lone hill in the distance."
	print "There is a patch of shrubbery at the base of the hill..."
	raw_input()
	print "But no! That is not a shrubbery, but a group of wild Uruk-Hai."
	print "The riders scream and fling themselves bravely into the fight."
	print "What do you do?"
	
	while True:
		choice = raw_input(p)
		
		if "attack" in choice:
			dead("You have no weapons with which to attack. The Uruk-Hai tear you from limb to limb.")
		elif "castle" in choice:
			print "The castle doors fly open and your pony hurtles towards the keep." 
			print "Just as you make it inside, the doors slam shut."
			print "Greeting you is a lanky figure dressed in wizard's garb. He says:"
			print """
			'There is an evil possessing the king of these lands.'
			Come, I will show you.'"""
			print "The wizard takes you by the arm and brings you to the throne room."
			print "The king is slumped in his chair. Besides him is a dark-hooded figure, who strides towards you."
			raw_input()
			print """
			'My dear, there is no evil here but this wizard.
			If you wish, I would like to speak some things with you in private.
			Do you agree?'"""
							
			while True:
				choice2 = raw_input(p)
				
				if choice2 == "Y":
					dead("The soothsayer Wormtongue casts you under a spell and you stay in Rohan to rot for eternity.")
				elif choice2 == "N":
					print "As you shake your head, the wizard clutches his staff and shouts words in a language unknown to you."
					print "The dark-hooded figure is thrown back, and the king sits up in his chair."
					print "'BE GONE FROM HIM!' extolls the wizard."
					print "The king is revived."
					print "'Take my fastest horses and make for Gondor,' says the king. 'That is where the evil awaits.'"
					raw_input()
					gondor(0)					
				else:
					print feedback
						
		elif "run" in choice or "flee" in choice:
			dead("As you run away, stray Uruk-Hai overtake you and eat you alive.")
		else:
			print feedback

			
def tatooine():
	print "You are sitting in a canteen, surrounded by a menagerie of sordid alien creatures."
	print "Outside, the wind blows across a barren desert."
	print "Across the tavern is a clarinet band playing swing music."
	print "A bug-eyed alien sits down across from you, holding a pistol. What do you do?"
	
	while True:
		choice = raw_input(p)
						
		if "attack" in choice or "shoot" in choice and "blaster" not in items:
			dead("You try to attack but have no weapons. The alien shoots you in the face.")
		elif "look around" in choice and "blaster" not in items:
			print "As you look around, you realize you have a blaster holstered on your leg. Nice!"
			items.append("blaster")
		elif "shoot" in choice and "blaster" in items:
			print "You shot Gredo! Nice job."
			print "Outside, there is a spaceship preparing for takeoff. What do you do?"
			
			while True:
				choice2 = raw_input(p)
				
				if "get on" in choice2:
					print "You get on the ship, which is being piloted by a large woolly Chewbacca."
					print "The ship takes off and you leave the planet's orbit..."
					raw_input()
					black_hole()
				elif "shoot" in choice2:
					dead("The pilot inside blows you to smitherines.")
				else:
					print feedback
				
		elif "shoot" not in choice and "blaster" in items:
			dead("The alien across from you senses your hesitation. He shoots you in the face.")
		else:
			print(feedback)

	
def apothecary():
	print "You find yourself in a brightly-lit room, the shelves lined with bottles and jars of all sizes."
	print "In walks a squat old man and a young mistress looking doefully in your eyes."
	print "He takes three vials off the wall and says:"
	print """
	'The first vile will ease all your pains.
	The second will give you strength.
	The third will bring clarity, and not.'"""
	print "Which vile do you take?"
	
	while True:
		choice = raw_input(p)
		
		if "first" == choice:
			dead("The man starts to laugh. 'That is the path of the weak!' he screams.")
		elif "second" == choice:
			print "The man smiles and says, 'May you find strength when you arrive!'"
			print "The room around you vanishes, and you find yourself in a dark cave."
			print "At your side are three bearded dwarves carrying axes."
			raw_input()
			moria()
		elif "third" == choice:
			print "The mistress looks in your eyes and says, 'Romeo, I shall never leave you.'"
			print "She leads you out of the building and towards a forest."
			raw_input()
			amsnd()
		else:
			print feedback

			
def shire():
	print "You find yourself in a pastoral landscape."
	print "There is a small green hill with a door in the side."
	print "Beside the door, a small pony is tied up."
	print "What do you do?"
	
	while True:
		choice = raw_input(p)
		
		if "pony" in choice:
			print "As you approach the pony, three women on horses approach."
			print "The one in front tells you: 'We are knights of Rohan. The Shire is not safe. You must come with us now.'"
			print "You join the band of three and set off riding towards the setting sun..."
			raw_input()
			rohan()
		elif choice == "open door" or choice == "open the door":
			print "As you open the door, a stout figure with a long beard you inside."
			print "'There is a great evil in these parts. We are not safe here,' he says"
			print "'My dwarvish brothers and I will guide you to safety. Come now!'"
			print "The dwarf pulls you by the arm as he takes you into a room with two other companions."
			print "There is a passage deep through these hills...through the mines..."
			raw_input()
			moria()
		elif "run" in choice or "flee" in choice:
			dead("As you run away, you hear a screech as a faceless rider in black tramples you and hacks you down with a massive sword.")
		else:
			print feedback 

	
def library():
	print "You are standing alone in a dark room, the stone walls lit by dim candlelight."
	print "On a wooden table there are three books: red, gold, and black."
	print "What do you do?"
	
	while True:
		choice = raw_input(p)
		transition = "As your fingers clasp the book, the room spins 'round. You are transported to another world..."
		
		if "red" in choice:
			print transition
			shire()
		elif "gold" in choice:
			print transition
			apothecary()
		elif "black" in choice:
			print transition
			tatooine()
		else:
			print feedback
	

def dead(why):
	print why, "Good job, try again next time!"
	exit(0)
	
library()