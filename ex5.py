name = 'Dillon C. Powers'
age = 26 # not a lie
height = 71 # inches
weight = 185 #  lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cm = 2.54
lbs = 2.1 

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %d centimeters" % (height * cm)   
print "He's %d pounds heavy." % weight
print "That's %d kilos." % (weight / lbs)  
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "Will %r be replaced no matter what?" % height 