# This defines x as a string of text, plus 10 is formatted in via %d 
x = "There are %d types of people." % 10
# This defines binary as text  
binary = "binary"
# Similar to above
do_not = "don't"
# This defines y as a string of text, with two variables formatted in 
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints x and y, plus the formatted variables for both 
print x
print y 

# Prints a string with x formatted in 
print "I said: %r." % x
# Prints a string with y in quotes
print "I also said: '%s'." % y 

# Defining two new variables 
hilarious = False 
joke_evaluation = "Isn't that joke so funny?! %r"

# formats the variable 'hilarious' into the string 'joke_evaluation'
print joke_evaluation % hilarious 

w = "This is the left side of..."
e = "a string with a right side."
print w + e #can print two strings continuously using +