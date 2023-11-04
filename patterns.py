
"""
1. Print the following patterns based on user inputs
a. Height of the Pattern ex: n = 4
#
##
###
####
b. Modify the pattern to include alignment as parameter.
c. Ex Height = 4 and Alignment = Right
     #
    ##
   ###
  ####
"""

def print_pattern(height, alignment):
    num = height
    if alignment == 'Left':
        for i in range(1, height + 1):
            print('#' * num)
            num -= 1
    elif alignment == 'Right':
        for i in range(1, height + 1):
            left_spaces = ' ' * (height - i)
            hashes = '#' * i
            print(left_spaces + hashes)
    else:
        print("Invalid alignment. Please use 'Left' or 'Right'.")

height = int(input("Enter the height of the pattern: "))
alignment = input("Enter the alignment (Left/Right): ").capitalize()

if alignment in ['Left', 'Right']:
    print_pattern(height, alignment)
else:
    print("Invalid alignment. Please use 'Left' or 'Right'.")
