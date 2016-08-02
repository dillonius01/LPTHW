def countdown(days_left, happiness_level):
	print "You have %d days left at Lenovo." % days_left
	print "Your happiness level is at %d." % happiness_level
	print "Keep on truckin'!\n"
	
print "1: Just numbers"	
countdown(90, 7)

print "2: Now we do math"
countdown(30 * 3, 10 - 3)

unhappy_thoughts = 65
happy_thoughts = 9 

print "3: We assigned variables"
countdown(unhappy_thoughts, happy_thoughts)

print "4: We combined variables and math"
countdown(unhappy_thoughts - 10, happy_thoughts + 5)

print "5: We got input from a user and assigned it to a variable"
fewer_days = raw_input("How many days now? ")
less_unhappy = raw_input("Give a high happiness score! ")

countdown(int(fewer_days), int(less_unhappy))

print "6: We did math with the user's input"
countdown(int(fewer_days) - 2, int(less_unhappy) + 8)

print "7: We call the function with user input directly"
countdown(int(raw_input("Duo jiu? ")), int(raw_input("Hai hao ma? ")))

print "8: Combining math with direct user input"
countdown(int(raw_input("How long? "))-10, int(raw_input("How happy? "))+10)

print "9: We get one user input and assign it to a variable, then we do math!"
aha_moment = int(raw_input("How many months? "))
countdown(aha_moment * 30, 10 - aha_moment)

print "10: Two variables doing math with each other"
months_worked = raw_input("How many months have you worked? ")
gray_hairs = raw_input("How many gray hairs? ")
countdown(int(gray_hairs) - int(months_worked), int(months_worked) * 2)