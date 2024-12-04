# Advent of Code 2024
#https://adventofcode.com/2024/day/2 

left = []
right = []
total = 0

def validate_reading(readings):

    # basically loop through all the readings removing one item each time and doing a check if it works success
    # if not continue to the next number in the readings and try again.  The shortcut everyone else did I guess :D
    for x in range(0, len(readings)):
        
        trun_readings = readings.copy()  # copy readings
        trun_readings.pop(x) # remove a number and test
        
        pairs = list(zip(trun_readings, trun_readings[1:]))

        if all(i > j and i - j <= 3 for i, j in pairs):  # check counting down
            return True
        elif all(i < j and j - i <= 3 for i, j in pairs):  # check counting up
            return True

    return False

# readfile and split the line into an int array of numbers
with open("input-day02-01.txt", "r") as file:
    for line in file:
        readings = [int(n) for n in line.split()]
        if validate_reading(readings):
            total += 1

# collect star
print("The winner is you:", total)
