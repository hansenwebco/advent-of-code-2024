# Advent of Code 2024
#https://adventofcode.com/2024/day/2 

left = []
right = []
total = 0

def validate_reading(readings):

    # creates pairs of each item next to each other in the readings array
    # The zip object is an iterator, meaning it can only be consumed once, so make it a list.. guess how I learned this....
    pairs = list(zip(readings, readings[1:]))

    if all(i > j and i - j <= 3 for i, j in pairs):  # check counting down
        return True
    elif all(i < j and j - i <= 3 for i, j in pairs):  # check counting up
        return True
    else:  # neither matches
        return False


# readfile and split the line into an int array of numbers
with open("input-day02-01.txt", "r") as file:
    for line in file:
        readings = [int(n) for n in line.split()]
        if validate_reading(readings):
            total += 1

# collect star
print("The winner is you:", total)
