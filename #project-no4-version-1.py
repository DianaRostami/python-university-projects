#project-no4-prototype version-1
#Program to get Count occurrences of each word in a text file

num_words = 0
 
# Open the file
with open("text2.txt", 'r') as file:
    for line in file:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)
