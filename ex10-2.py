maverick = "You can't handle the %r"
maverick2 = "You can't handle the %s"
#using %s means that rat's string doesn't print with quotes
iceman = "You're %s\n\tdangerous"
goose = '\n\t"Danger\"\n\t\"Zone\"'
rat = 'very'

print maverick % "truth"
print iceman % rat

print maverick % goose

print maverick2 % goose