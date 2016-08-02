from sys import argv

script, input_file = argv

def print_all(f): 
	#defines new function with single variable
	print f.read() 
	#prints the file object contents
	
def rewind(f): 
	#defines new function also on f 
	f.seek(0) 
	#returns the pointer to start of file object 
	
def print_a_line(line_count, f): 
	#defines new function with two variables
	print line_count, f.readline() 
	#prints the variable line_count and one line of text 
	
current_file = open(input_file)
#opens input_file into a file object we're calling current_file

print "First let's print the whole file:\n"

print_all(current_file)
#prints the current_file, which is defined based on the argument variable 

print "Now let's rewind, kind of like a tape."

rewind(current_file)
#this brings the pointer back to 0 on current_file, which we just printed all of 

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
#since current_line is 1, this prints 1 and the text on line 1

current_line += 1
#current_line = current_line + 1 #was the old code 
#redefines current_line by adding one...didn't know you could do that
print_a_line(current_line, current_file)
#since current_line is now 2, this prints 2 and the text on line 2  

current_line += 1
print_a_line(current_line, current_file)
#same as above, now 3 and line 3 