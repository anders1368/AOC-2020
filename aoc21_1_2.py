from collections import defaultdict, deque
import time
from itertools import combinations, permutations

start_time = time.time()

#file1= open('aoc19_test_rules.txt', 'r')
#file2= open('aoc19_test_input.txt', 'r')
#file1= open('aoc21_test_input.txt', 'r')
file1= open('aoc21_input.txt', 'r')


def filter_list(input_list,filter):
    return_list = []
    for i_set in input_list:
        if filter in i_set: return_list.append(i_set)
    return return_list


input = []
allergens = set()

for line in file1.readlines():
    dish = line.strip().split('(contains')
    d_part1 = dish[0].strip()
    d_part2 = dish[1].replace(')','').strip()
    l1 = [x.strip() for x in d_part1.split(' ')]
    l2 = [x.upper().strip() for x in d_part2.split(',')]
    allergens = allergens.union(set(l2))
    input.append(set(l1+l2))

reduced_allergens = []
count = 0
#loop over allergens
while count < 10:
    for a in allergens:
        sets_with_allergen = filter_list(input,a)
        if len(sets_with_allergen) != 0:
            intersection = set.intersection(*sets_with_allergen)
            if len(intersection) == 2 and not (all(i[0].islower() for i in intersection)):
                reduced_allergens.append(intersection)
            print(f"Reduced:{reduced_allergens}")
    for each in input:
        each.difference_update(*reduced_allergens)
    count += 1
    print(f"Input reduced:{input}")

d = defaultdict(list)
ans = 0
for each in input:
    ans += len(each)
print(f"Ans part 1:{ans}")
for each in reduced_allergens:
    k,v = '', []
    for i in each:
        if i[0].islower():
            v.append(i)
        else:
            k = i
    d[k] = v
print("Ans part2:",end='')
for key in sorted(d.keys()):
    print(d[key][0],end='')
    print(',',end='')
print('')
print("--- %s seconds ---" % (time.time() - start_time))
