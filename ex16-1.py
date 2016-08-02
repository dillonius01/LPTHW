#print "What file would you like to open?"

#filename = raw_input("> ")
#txt = open(filename)

#print "Press RETURN to see the file contents"

#raw_input("> ")

#print txt.read()

from sys import argv

script, filename = argv

txt = open(filename)
print txt.read()
txt.close()
