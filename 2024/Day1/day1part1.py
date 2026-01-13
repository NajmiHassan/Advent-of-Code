# Define the input as a multiline string
input_data = """
 14832   78161
 19986   67025
 61574   40916
 87318   29281
 12651   42252
 43238   74483
 13498   83990
 89748   81193
 "Continue the list"
"""

# Parse the input into two separate lists of integers.
left_list =  []
right_list = []
for line in input_data.strip().split('\n'):
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# Sort both lists.
left_list.sort()
right_list.sort()

# Calculate the total distance between paired elements.
total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))

print(total_distance)