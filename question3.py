# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])


 # Solution 2: Using list slicing

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)
for i in x[0::2]:
    print(i)