# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers


def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)

    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]


# Get user input for the number
user_number = int(input("Enter a number: "))

# Check if the entered number is a palindrome
if is_palindrome(user_number):
    print(f"{user_number} is a palindrome number.")
else:
    print(f"{user_number} is not a palindrome number.")
