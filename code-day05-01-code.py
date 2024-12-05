# Advent of Code 2024
# https://adventofcode.com/2024/day/5

total = 0
page_rules = []
pagesEnd = False

def check_pages(data):
    global page_rules, total
    check_pages = [int(x) for x in data.split(",")]

    # we only care about rules that are in the page_rules - the problem stated numbers not mentioned don't matter so we don't care
    # therefore we can take each set of numbers for beginning to end of our pages and look for inverted rules that means we've spefically broken a defined rule
    i = 0
    while i < len(check_pages) - 1:
        current_number = check_pages[i]
        next_number = check_pages[i + 1]

        if (next_number, current_number) in page_rules:
            #print ("FAIL: ", check_pages, "RULE : " , current_number,",", next_number)
            return False

        i = i + 1
   
    mid_point = int((len(check_pages)+1)/2)-1
    total = total + check_pages[mid_point]

    #print("PASS: ", check_pages, "MID: ", mid_point, "VALUE: ", check_pages[mid_point])

    return True


# readfile and build a rules array we can use to verify our pages against
with open("input-day05-01.txt", "r") as file:
    for line in file:
        clean = line.rstrip("\n")
        if len(clean) == 0:
            pagesEnd = True
        elif pagesEnd == True:
            check_pages(line)
        else:
            parts = line.strip().split("|")
            page_rules.append((int(parts[0]), int(parts[1])))

print(total)
