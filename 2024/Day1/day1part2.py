from collections import Counter

# Define your input data as a multiline string
input_data = """
 14832   78161
 19986   67025
 61574   40916
 87318   29281
 12651   42252
 43238   74483
 13498   83990
 89748   81193
 21897   61695
 56707   55826
 53149   71661
 35501   54251
 35575   64490
 93717   93097
 56811   38115
 59171   88932
 "list continues"
"""

# Parse the input into two separate lists of integers.
left_list = []
right_list = []
for line in input_data.strip().split('\n'):
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# Count occurrences of each number in the right list.
right_count = Counter(right_list)

# Calculate the similarity score.
similarity_score = sum(left * right_count[left] for left in left_list)

print(similarity_score)