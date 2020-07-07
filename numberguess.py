import random

number=random.randrange(0,100)

guessCheck="wrong"

print "Welcome to Number Guess"

while guessCheck=="wrong":
	response=raw_input("Please input a number between 0 and 100:")
	try:
		val=int(response)
	except ValueError:
		print "This is not a valid integer. Please try again"
		continue
	val=int (response)
	if val<number:
		print "This is lower than actual number. Please try again."
	elif val>number:
		print "This is higher than actual number. Please try again."
	else:
		print "This is the correct number"
		guessCheck="correct"

print "Thank you for playing Number Guess. See you again"
© 2020 GitHub, Inc.
