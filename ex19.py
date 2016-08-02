#defines function cheese_and_crackers 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#prints line of text with cheese_count called in 
	print "You have %d cheeses!" % cheese_count
	#prints line of text with boxes_of_crackers called in 
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#two more lines of text printed, including an escaped space \n 
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	

#prints a line of text 
print "We can just give the function numbers directly:"
#calls cheese_and_crackers with two variables defined as 20, 30
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
#defines two variables from the script 
amount_of_cheese = 10
amount_of_crackers = 50

#runs cheese_and_crackers with variables just defined above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#uses cheese_and_crackers with basic math as variables 
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


#runs cheese_and_crackers with script variables and math 
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)