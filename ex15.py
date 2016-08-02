from sys import argv #import argument module

script, filename = argv #defining argument variable

txt = open(filename) #turns a file into a file object (txt) so that it can be opened

print "Here's your file %r:" % filename #prints filename as defined earlier
print txt.read() #tells computer to read txt with no parameters

txt.close()

print "Closed or not?" , txt.closed #prints False if open and True if closed

print "Type the filename again:"
file_again = raw_input("> ") #defines file_again as what user types

txt_again = open(file_again) #opens file_again

print txt_again.read() #reads and prints txt with no parameters

txt_again.close()

## when running python in shell, need to do open("ex15.py")