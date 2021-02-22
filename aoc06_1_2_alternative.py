from collections import defaultdict

file1 = open('aoc06_1_input.txt', 'r')
groups = file1.read().split('\n\n')

ans = 0
peopleInGroupCounter = 0
groupDict = defaultdict(int)

for group in groups:
    #reset
    peopleInGroupCounter = 0
    groupDict.clear()
    #per person loop
    people = group.split()
    #count for part 2
    peopleInGroupCounter = len(people)
    for person in people:
        for c in person: groupDict[c] += 1
    for x in groupDict:
        #part 2 only count if the answer == number of people in the group
        if (groupDict.get(x) is not None) and (groupDict.get(x) == peopleInGroupCounter):
            ans += 1
    print(f"Part answer:{ans} People in Group:{peopleInGroupCounter} :{groupDict} : {len(groupDict)} ")


print(f"Answer:{ans}")







