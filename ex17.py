from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how? JUST DID IT WHATT
#in_file = open(from_file)
#indata = in_file.read()

#indata = open(from_file).read()
#must have line 12 if using indata variable

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#out_file = open(to_file, 'w')
#out_file.write(indata)

#open(to_file, 'w').write(indata)

######## GOOD STUFF HERE

open(to_file, 'w').write(open(from_file).read())

######## SEE ABOVE

#print "Alright, all done."

#out_file.close()
#in_file.close()