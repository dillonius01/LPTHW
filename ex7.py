print "Mary had a little lamb."
# 'snow' isn't a variable,  it's a string that is formatted in (has quotes)
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do?
# printed ten . in a row

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# the comma prints both strings on the same line
print end1 + end2 + end3 + end4 + end5 + end6,
# no spaces between the added strings 
print end7 + end8 + end9 + end10 + end11 + end12 

# using commas leaves spaces 
print end1, end2, end3, end4, end5, end6
