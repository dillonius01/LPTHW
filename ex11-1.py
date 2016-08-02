name = raw_input('What\'s your name? ')
print ("Hello %s, let\'s be friends!" % name)

print (30 * '-')
print (" M A I N - M E N U")
print (30 * '-')
print ("\t1. Backup")
print ("\t2. User management")
print ("\t3. Reboot the server")
print (30 * '-')

## get input
choice = raw_input('What would you like to do today, %s? ' % name)

choice = int(choice)

if choice == 1:
	print 'I\'d rather not do that, %s' % name
elif choice == 2:
	print 'Okay, %s, let\'s play a game' % name
elif choice == 3:
	print "Please don\'t do that, %s" % name
else: ##
	print 'I\'m sorry, %s, but I can\'t do that' % name