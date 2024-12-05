# Advent of Code 2024
# https://adventofcode.com/2024/day/5

total = 0
page_rules = []
pagesEnd = False

# basically check if we broke a rule and if so flip the numbers
def check_pages(data):
    global page_rules, total
    check_pages = [int(x) for x in data.split(",")]

    i = 0
    fixed = False
    while i < len(check_pages) - 1:
        current_number = check_pages[i]
        next_number = check_pages[i + 1]

        if (next_number, current_number) in page_rules:
            check_pages[i] = next_number
            check_pages[i + 1] = current_number
            fixed = True
            i = 0
        else:
            i = i + 1

    if (fixed):
        mid_point = int((len(check_pages)+1)/2)-1
        total = total + check_pages[mid_point]

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
