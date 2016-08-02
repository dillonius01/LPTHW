def square(x):
	print "I'm squaring your number"
	return x * x 
	
a = square(float(raw_input("What is your first square? ")))
b = square(float(raw_input("How about your second? ")))

print "Your two squares are %s and %s" % (a, b)

