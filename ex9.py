# Here's some new strange stuff, remember to type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
# The \n puts the next part of the string on a new line 
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like,
Even 4 lines if we want, or 5, or 6.
"""

colors = "red orange \ngreen blue \nviolet"
print colors

# \n does not work when using %r