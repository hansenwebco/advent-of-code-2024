# Advent of Code 2024
# https://adventofcode.com/2024/day/4 

puzzle2D = []
width = 0
height = 0
counter = 0

def check_right(posRow, posCol, width):
    global puzzle2D
    if posCol + 4 > width:
        return False

    value = puzzle2D[posRow][posCol] + puzzle2D[posRow][posCol+1] + puzzle2D[posRow][posCol+2] + puzzle2D[posRow][posCol+3]
    
    if (value == "XMAS" or value == "SAMX"):
        print(posRow,posCol,value, "right")
        return True

    return False

def check_down(posRow, posCol,height):
    global puzzle2D
    if posRow + 4 > height:
        return False

    value = puzzle2D[posRow][posCol] + puzzle2D[posRow+1][posCol] + puzzle2D[posRow+2][posCol] + puzzle2D[posRow+3][posCol]

    if (value == "XMAS" or value == "SAMX"):
        print(posRow,posCol,value, "down")
        return True

    return False

def check_diag_right(posRow,posCol,width, height):
    global puzzle2D
    if posRow + 4 > height or posCol + 4 > width:
        return False

    value = puzzle2D[posRow][posCol] + puzzle2D[posRow+1][posCol+1] + puzzle2D[posRow+2][posCol+2] + puzzle2D[posRow+3][posCol+3]
 
    if (value == "XMAS" or value == "SAMX"):
        print(posRow,posCol,value,"diag-right-down")
        return True

    return False

def check_diag_left(posRow,posCol,width,height):
    global puzzle2D

    if posCol - 3 < 0 or posRow + 4 > height:
        return False
    
    value = puzzle2D[posRow][posCol] + puzzle2D[posRow+1][posCol-1] + puzzle2D[posRow+2][posCol-2] + puzzle2D[posRow+3][posCol-3]
    #print(posRow,posCol,value)
  
    if (value == "XMAS" or value == "SAMX"):
        print(posRow,posCol,value,'diag-left-down')
        return True

    return False

# readfile and split the line into an int array of numbers
with open("input-day04-01.txt", "r") as file:
    for line in file:
        puzzle2D.append(list(line.rstrip("\n")))

width = len(puzzle2D)
height = len(puzzle2D[0])

posRow = 0
posCol = 0

for posRow in range(0, height):
    for posCol in range(0, width):
        if(check_right(posRow, posCol, width)):
            counter+=1
        if(check_down(posRow,posCol,height)):
            counter+=1
        if(check_diag_right(posRow,posCol,width,height)):
            counter+=1
        if(check_diag_left(posRow,posCol,width,height)):
            counter+=1

print(counter)

