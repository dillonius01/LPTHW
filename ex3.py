print "I will not count my chickens:"

print "Hens", 25 + 30 / 6 #total is 30, so 30/6 is calculated first
print "Roosters", 100 - 25 * 3 % 4 # the % sign is "mod", which means the integer remainder of the division
#that means the order of operations is */ then % then +-, since 25 * 3 % 4 is 75 % 4, which is 3, because 75/4 = 18 3/4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 #1 / 4 is actually 0, as is 4 % 2
# so this line is 3 + 2 + 1 - 5 + 0 - 0 + 6, which is 7 

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7 #prints "False" because 3 + 2 is not less than 5 - 7 
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5>= -2 
print "Is it less or equal?", 5<= -2

print "7.0 / 4.0", 7.0 / 4.0
print "Square root of two", 2**0.5