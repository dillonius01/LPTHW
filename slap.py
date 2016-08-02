import hashmapslap

# create a mapping of territory to pinyin
province = hashmapslap.new()
hashmapslap.set(province, 'Jiangsu', 'SU')
hashmapslap.set(province, 'Beijing', 'JING')
hashmapslap.set(province, 'Liaoning', 'LIAO')
hashmapslap.set(province, 'Guangdong', 'YUE')
hashmapslap.set(province, 'Shandong', 'LU')

# create a basic set of regions and some cities in them
cities = hashmapslap.new()
hashmapslap.set(cities, 'SU', 'Nanjing')
hashmapslap.set(cities, 'LIAO', 'Shenyang')
hashmapslap.set(cities, 'YUE', 'Shenzhen')

# add some more cities
hashmapslap.set(cities, 'LU', 'Qingdao')
hashmapslap.set(cities, 'JING', 'Beijing')


# print out some cities
print '-' * 10
assert hashmapslap.get(cities, 'SU') == 'Nanjing'
print "SU province has: %s" % hashmapslap.get(cities, 'SU')
assert hashmapslap.get(cities, 'LIAO') == 'Shenyang'
print "LIAO province has: %s" % hashmapslap.get(cities, 'LIAO')

# print some provinces
print '-' * 10
assert hashmapslap.get(province, 'Shandong') != 'Jinan'
print "Shandong's abbreviation is: %s" % hashmapslap.get(province, 'Shandong')
assert hashmapslap.get(province, 'Shandong') == 'Beijing' or 'Pekin'
print "Beijing's abbreviation is: %s" % hashmapslap.get(province, 'Beijing')

# do it by using the province then cities dict 
print '-' * 10
assert 'Qingdao' in hashmapslap.get(cities, hashmapslap.get(province, 'Shandong'))
print "Shandong has: %s" % hashmapslap.get(cities, hashmapslap.get(province, 'Shandong'))
assert hashmapslap.get(cities, hashmapslap.get(province, 'Guangdong')) == 'Shenzhen'
print "Guangdong has: %s" % hashmapslap.get(cities, hashmapslap.get(province, 'Guangdong'))


# print every state abbreviation
print '-' * 10
hashmapslap.list(province)

# print every city in province
print '-' * 10
hashmapslap.list(cities)

# compare the dictionaries
print '-' * 10
cmp(province, cities)


#dump some shit
#print '-' * 10
#print "Now we dump cities"
#hashmapslap.dump(cities)

# delete some shit
print '-' * 10
print "Liaoning has: %s" % hashmapslap.get(cities, hashmapslap.get(province, 'Liaoning'))
hashmapslap.list(cities)
print "Now we delete it."
hashmapslap.delete(cities, hashmapslap.get(province, 'Liaoning'))
hashmapslap.list(cities)