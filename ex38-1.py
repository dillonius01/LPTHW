thelist = ["Christine", "Linda", "Jordan", "Joan", "Rose", "Tenley", "Sara", "Sisi", "Starfish", "Britt", "Ginny", "Genie", "Rinka"]


def adder():
	global thelist
	print "The list is %d long" % len(thelist)
	print "Is there anyone to add?"
	print "1: Yes"
	print "2: No"
	
	choice = raw_input("> ")
	
	if choice == "1":
		new = raw_input("Who's the lucky lady? ")
		thelist.append(new)
		counter = thelist.index(new) + 1
		print "Added %s to the list! She's number %d" % (new, counter)
	if choice == "2":
		print "Okay, step up your game!"
	else:
		print "Type a number, dude!"
		
		
		
def finder():
	global thelist
	
	print "Whom are we looking for?"
	girl = raw_input("> ")
	
	try:
		i = thelist.index(girl) + 1
		print "%s is number %d" % (girl, i)
	except:
		print "idk who dad is"
		
adder()
finder()