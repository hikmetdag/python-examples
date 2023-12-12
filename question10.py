# Create a new list from two list using the following condition

# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.


def two_lists(a, b):
    new_list = []
    for i in a:
        if i % 2 != 0:
            new_list.append(i)

    for x in b:
        if x % 2 == 0:
            new_list.append(x)
    return new_list


print(two_lists([1, 2, 3, 4], [10, 11, 12, 1, 3]))
