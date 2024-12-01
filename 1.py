# I
# pair up the numbers and measure how far apart they are; the smallest number in the left list with the smallest number in the right list
# add up the distances between all of the pairs you found  

# read in csv to list
puzzle_input = r"C:\Users\rylee\Documents\Coding Projects\advent of code\2024\1.txt"
pairs = []

with open(puzzle_input, 'r') as file:
    #add each line to list
    for line in file: # Read each line in the file
        pairs.append(line.strip())

#right and left columns
left_list = []
right_list = []

for pair in pairs: # Read each line in the file
        left_list.append(int(pair[0:5]))
        right_list.append(int(pair[-5:])) 

# sort columns smallest -> largest
left_list.sort()
right_list.sort()

# get differences between pairs
dist_list = []

for left_item in left_list:
    count = left_list.index(left_item)
    right_item = right_list[count]
    dist = abs(right_item - left_item)
    dist_list.append(dist)

# sum the differences
running_sum_1 = 0
for dist in dist_list:
     running_sum_1 = running_sum_1 + dist

# part 1 answer
print(running_sum_1)

# II
# figure out exactly how often each number from the left list appears in the right list
# calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list

#left_instances = []
similarity_score = []

for left_item in left_list:
    instances = 0
    for right_item in right_list:
        if left_item == right_item:
            instances += 1

    # multiplying it by the number of times that number appears in the right list
    similarity_score.append(left_item * instances)

# add up each number in left list
running_sum_2 = 0
for score in similarity_score:
     running_sum_2 = running_sum_2 + score

# part 2 answer
print(running_sum_2)