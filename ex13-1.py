from sys import argv

script, first, second, third = argv

print "The name of this script is:", script
print "The first variable is:", first
print "The second variable is:", second
print "The third variable is:", third 

print "What is the fourth variable? ",
fourth = raw_input()

print "The fourth variable is %r" % fourth

print "Okay, your variables 
are %r, %r, %r, and %r." % (first, second,  third, fourth)