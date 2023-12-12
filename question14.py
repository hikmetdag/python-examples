# Print a downward Half-Pyramid Pattern of Star (asterisk)
# * * * * *
# * * * *
# * * *
# * *
# *


def print_downward_half_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
