# Program to calculate the number of letters in a text file

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

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# call function 
for i in range(26):
    print( alphabet[i] ,letterFrequency('text2.txt', alphabet[i]))
