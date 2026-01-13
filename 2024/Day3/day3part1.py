import re

# Load the content of the file
file_content = """Your Puzzle Input"""

# Regular expression to find valid mul(X,Y) patterns
pattern = r"mul\((\d+),(\d+)\)"

# Find all matches in the file content
matches = re.findall(pattern, file_content)

# Calculate the sum of products
total_sum = sum(int(x) * int(y) for x, y in matches)

print("Total Sum:", total_sum)
