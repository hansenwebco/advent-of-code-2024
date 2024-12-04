# Advent of Code 2024
# https://adventofcode.com/2024/day/3 

import re

total = 0

# Open the file and read all text
with open('input-day03-01.txt', 'r') as file:
    # Read the entire contents
    text = file.read()

# Apply regex to find mul(#,#)
pattern = r"mul\(\d{1,3},\d{1,3}\)" 
matches = re.findall(pattern, text)

# loop through matches and multiply, we could have a used a more specific regex here but eh
for match in matches:
    nums = re.findall(r'\b\d+\b',match)
    total = total + int(nums[0])*int(nums[1])

# you are a winrar
print(total)
