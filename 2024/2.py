# PART 1
# only counts as safe if both of the following are true:
#   The levels are either all increasing or all decreasing.
#   Any two adjacent levels differ by at least one and at most three.
# how many reports are safe?

# read in csv to list
puzzle_input = r"C:\Users\rylee\Documents\Coding Projects\advent of code\2024\2.txt"
reports = []
with open(puzzle_input, 'r') as file:
    for line in file: 
        reports.append(line.strip())

safe_reports1 = []

for report in reports: #report = line
    levels = []
    values = list(map(int, report.split(' ')))  #convert the split values to integers, prev levels.append(report.split(' '))
    levels.extend(values)  #add these integers directly to 'levels' (flat structure)

    i = 0
    level_diffs = [] #differences of each pair

    for level in levels:
        if (i + 1) < len(levels): #are there still pairs left to consider in the list
            i1 = levels[i]
            i2 = levels[i + 1]
            diff = int(i2) - int(i1)
            level_diffs.append(diff)
        i += 1

    incr_or_decr = any(all(x > 0 for x in level_diffs) or all(x < 0 for x in level_diffs) for x in level_diffs) #check if all increasing or descreasing
    diff_judgement = any(abs(x) < 1 for x in level_diffs) or any(abs(x) > 3 for x in level_diffs) #any two adjacent levels differ by at least one and at most three

    if incr_or_decr == True and diff_judgement == False: 
        safe_reports1.append(levels)

#part 1 answer
print(len(safe_reports1))

# PART 2
# now, if removing a single level from an unsafe report would make it safe, the report instead counts as safe
safe_reports2 = []

for report in reports: #report = line
    levels = []
    values = list(map(int, report.split(' ')))  #convert the split values to integers, prev levels.append(report.split(' '))
    levels.extend(values)  #add these integers directly to 'levels' (flat structure)
    
    i = 0
    level_diffs = [] #differences of each pair
    for level in levels:
        if (i + 1) < len(levels): #are there still pairs left to consider in the list
            i1 = levels[i]
            i2 = levels[i + 1]
            diff = int(i2) - int(i1)
            level_diffs.append(diff)
        i += 1

    incr_or_decr = any(all(x > 0 for x in level_diffs) or all(x < 0 for x in level_diffs) for x in level_diffs) #check if all increasing or descreasing
    diff_judgement = any(abs(x) < 1 for x in level_diffs) or any(abs(x) > 3 for x in level_diffs) #any two adjacent levels differ by at least one and at most three

    if incr_or_decr == True and diff_judgement == False: 
        safe_reports2.append(levels)

    else: # try removing one at a time, then rechecking if safe
        ii = 0
        levels = tuple(levels) # these are just the ones that were not safe
        for level in levels: # try removing each digit then store in levels_dampened
            levels_dampened = []
            levels_dampen = list(levels) 
            levels_dampen.pop(ii)
            levels_dampened.extend(levels_dampen) #has value removed

            iii = 0
            level_diffs_dampened = [] # get differences between each pair
            for level in levels_dampened:
                if (iii + 1) < len(levels_dampened):
                    ii1 = levels_dampened[iii]
                    ii2 = levels_dampened[iii + 1]
                    diff2 = int(ii2) - int(ii1)
                    level_diffs_dampened.append(diff2)
                iii += 1

            incr_or_decr2 = any(all(x > 0 for x in level_diffs_dampened) or all(x < 0 for x in level_diffs_dampened) for x in level_diffs_dampened) #check if all increasing or descreasing
            diff_judgement2 = any(abs(x) < 1 for x in level_diffs_dampened) or any(abs(x) > 3 for x in level_diffs_dampened) #any two adjacent levels differ by at least one and at most three

            if incr_or_decr2 == True and diff_judgement2 == False: 
                safe_reports2.append(levels)
                
            ii += 1

safe_reports3 = []
for value in safe_reports2: # remove duplicate values
    if value not in safe_reports3:
        safe_reports3.append(value)

# part 2 answer
print(len(safe_reports3)) #looking for ans  = 2 until put all data back