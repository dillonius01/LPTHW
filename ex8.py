# defines formatter as a string of variables to be formatted in 
formatter = "%r %r %r %r"

# formats in integer values 
print formatter % (1, 2, 3, 4)
# formats in text strings 
print formatter % ("one", "two", "three", "four")
# formats in Boolean values 
print formatter % (True, False, False, True)
# formats in the string of the formatter variable as defined 
print formatter % (formatter, formatter, formatter, formatter)
# formats in four strings of text. Note: printed all on the same line.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)