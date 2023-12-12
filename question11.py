# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.


def extract_digits_reverse(number):
    # Convert the number to a string and reverse it
    number_str = str(number)[::-1]

    # Iterate through each character and print the digits
    for digit in number_str:
        print(digit, end=" ")
