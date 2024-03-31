#Program to get Count occurrences of each word in a text file

num_words = 0
d = dict()
 
# Open the file
with open("text2.txt", 'r') as file:
    for line in file:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)

with open("text2.txt", 'r') as file:
    for line in file:
        # Remove the leading spaces and newline character 
        line = line.strip() 
  
            # Convert the characters in line to 
            # lowercase to avoid case mismatch 
        line = line.lower() 
  
        # Split the line into words 
        words = line.split(" ") 
                         
  
        for word in words: 
            # Check if the word is already in dictionary 
            if word in d:  
                d[word] = d[word] + 1
            else: 
                d[word] = 1
                
# Print the contents of dictionary 
for key in list(d.keys()): 
    print(key, ":", d[key])  