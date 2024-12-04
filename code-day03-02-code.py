# Advent of Code 2024
# https://adventofcode.com/2024/day/3 

import re

total = 0
do = True

# Open the file and read all text
with open('input-day03-01.txt', 'r') as file:
    # Read the entire contents
    text = file.read()

# Apply regex to find mul(#,#)
pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"  # Replace with your desired regex pattern
matches = re.findall(pattern, text)

# loop through matches and keep track if we've seen a do() or don't() only do math if do was the last seen
for match in matches:
    if (match == "do()"):
        do = True
    elif (match == "don't()"):
        do = False
    elif (do):
        nums = re.findall(r'\b\d+\b',match)
        total = total + int(nums[0])*int(nums[1])

# you are a winrar
print(total)