def new(num_buckets=256):
	""" Initializes a Map with the given number of buckets."""
	# creates list aMap 
	aMap = []
	# adds integer values of 0 to num_buckets to aMap 
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap
	
def hash_key(aMap, key):
	"""Given a key this will create a number and then convert it to 
	an index for the aMap's buckets."""
	# hash gives an integer value for the key. But it might be huge, so 
	# the % returns the remainder of after it's divided by the length
	# that means the hash value is less than the length 
	return hash(key) % len(aMap)
	 
def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	# this gets the bucket where the key could go. We know from hash_key that it fits in aMap  
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]
	
def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	bucket = get_bucket(aMap, key)
	
	# enumerate assigns integer values for each bucket 
	for i, kv in enumerate(bucket):
			k, v = kv 	
			if key == k:
				return i, k, v # really this just returns k as the key; v is equal to that
			
		# this returns that the default is when i is -1 
	return -1, key, default 
		
def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key)
	return v 
	
def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value"""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)
	
	if i>= 0:
		# the key exists, replace it 
		bucket[i] = (key, value)
	else:
		# the key does not, append to create it 
		bucket.append((key, value))
		
def delete(aMap, key):
	"""Deletes the given key from the Map."""
	bucket = get_bucket(aMap, key)
	
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			# break so that python doesn't go through any more of the buckets 
			break 
			
def list(aMap):
	"""Prints out what's in the Map"""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v 