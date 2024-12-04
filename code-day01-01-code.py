# Advent of Code 2024
#https://adventofcode.com/2024/day/1 


left = []
right = []
total = 0

# readfile and build an array of left and right
with open('input-day01-01.txt', 'r') as file:
    for line in file:
        left.append(line[0:5])    
        right.append(line[8:13])    
    
# sort them, default is smallest to biggest cool cool
left.sort()
right.sort()

# assume arrays match in length and loop through and subtract the sides always taking absolute  value for distance
while len(left) > 0 :
    total = total + abs((int(left[0]))- int(right[0])) 
    left.pop(0)
    right.pop(0)

# collect star
print ("The winner is you:" , total)