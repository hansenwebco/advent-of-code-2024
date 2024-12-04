# Advent of Code 2024
#https://adventofcode.com/2024/day/1 

left = []
right = []
total = 0

# readfile and build an array of left and right
with open('input-day01-01.txt', 'r') as file:
    for line in file:
        left.append(int(line[0:5]))    
        right.append(int(line[8:13]))    

# take the item in the left list and check in the right list how many time it appears
while len(left) > 0 :
    num = int(left[0])
    total = total + num * right.count(num)
    left.pop(0)

# collect star
print ("The winner is you:" , total)