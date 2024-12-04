puzzle2D = []
width = 0
height = 0
counter = 0

def check_xmas(posRow, posCol, width, height):
    global puzzle2D
    if posCol + 3 > width or posRow + 3 > height:
        return False

    value = puzzle2D[posRow][posCol] + puzzle2D[posRow][posCol+2] + puzzle2D[posRow+1][posCol+1] + puzzle2D[posRow+2][posCol] + puzzle2D[posRow+2][posCol+2]

    # look for all the varations fos the X-MAS that can be had    
    if (value == "MSAMS" or value == "SMASM" or  value == "SSAMM" or value == "MMASS"):
        print(posRow,posCol,value, "BAM")
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
        if(check_xmas(posRow, posCol, width, height)):
            counter+=1

# you found all the things
print(counter)

