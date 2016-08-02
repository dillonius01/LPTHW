def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b 
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b 
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b 
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b 
	
	
print "Let's do some math with just functions!"

age = add(22, 5)
height = subtract(82, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

#print (30 + 5) + ((78 - 4) - ((90 * 2) * ((100 / 2) / 2))) 

food = add(50, 100)
rent = divide(3300, 30)
months = subtract(12, 9)
misc = multiply(10, 4)

expenses = subtract(misc, add(rent, multiply(food, add(months, 2))))
print "That becomes", expenses, "Which is weird."