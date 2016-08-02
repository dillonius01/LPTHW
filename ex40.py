class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])

my_neck = Song(["All you ladies pop your pussy like this",
				"Shake it up girl just don't miss",
				"Do it right, lick it good, suck that pussy just like you should"])

memphis = ["There was a dream", "I had it too", "You could see it coming true", 
			"It would travel in the air", "You could make it if you dared"]
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

my_neck.sing_me_a_song()

x = Song(memphis)
x.sing_me_a_song()

Kanye = {
	"College Dropout": "Throw your mutherfuckin hands, get 'em high",
	"Late Registration": "I ain't sayin' you're a gold digger",
	"Graduation": "Do it harder make it better work it faster makes us stronger",
	"MBDTF": "Now my mother brother grandmother hate me in that order",
	"Yeezus": "300 Romans, we're the Trojans"
}

for 