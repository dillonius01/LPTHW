states = {
	'Oregon': 'OR',
	'Washington': 'WA',
	'Idaho': 'ID',
	'Wyoming': 'WY'
}

key = raw_input('> ')
for i, kv in enumerate(states):
	k, v = kv
	if key == k:
		print "Here are %r, %r, and %r" % (i, k, v)

