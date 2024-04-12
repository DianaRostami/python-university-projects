#project no.2 prototype version 1
#count all characters in a textfile

#function
def charCount(fileName):
	# open file
	file = open(fileName, "r")

	# store content in a variable
	text = file.read()

	count = 0

	for char in text:
		count += 1

	return count

# call function 
print(charCount('text2.txt'))
