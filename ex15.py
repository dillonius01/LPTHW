#import argv module
from sys import argv

#assigning the variables used in argv
script, filename = argv

#defines txt, by using the open function
txt = open(filename)

#prints filename 
print "Here's your file %r:" % filename
#prints txt by asking to read the open filename 
print txt.read()

txt.close()

#prints a prompt
print "Type the filename again:"
#defines file_again via raw input 
file_again = raw_input("> ")

#opens the file_again and defines that as txt_again 
txt_again = open (file_again)

print txt_again.read()