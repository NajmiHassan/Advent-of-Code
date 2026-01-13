import re

# Load the content of the file
file_content = """Your Puzzle Input"""

# Regular expression to find valid mul(X,Y) patterns
pattern = r"(?<!\w)mul\((\d+),(\d+)\)"

# Regular expression to find do and don't instructions
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Initialize variables
enabled = True
total_sum = 0

# Split the content into tokens using regex to preserve order
tokens = re.split(r"(do\(\)|don't\(\)|(?<!\w)mul\(\d+,\d+\))", file_content)

for token in tokens:
    if re.match(do_pattern, token):
        enabled = True
    elif re.match(dont_pattern, token):
        enabled = False
    else:
        match = re.match(pattern, token)
        if match and enabled:
            x = int(match.group(1))
            y = int(match.group(2))
            total_sum += x * y

print("Total Sum:", total_sum)
