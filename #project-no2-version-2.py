#project no.2 prototype version 2

#function
def letterFrequency(fileName, letter):
	# open file
	file = open(fileName, "r")

	# store content in a variable
	text = file.read()

	count = 0

	for char in text:

		if char == letter:
			count += 1

	return count

# call function 
print(letterFrequency('text2.txt', "a"))
