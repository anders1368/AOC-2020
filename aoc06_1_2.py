ans = 0

file1 = open('aoc06_1_input.txt', 'r')
Lines = file1.readlines()

#ngn print(sum(len(set.intersection(*map(set,g.split()))) for g in sys.stdin.read().split('\n\n')))

groupString = ""
groupDict = {}
peopleCounter = 0
#compactedLines= Lines.split('\n\n')

for line in Lines:
    if line != '\n':
        peopleCounter += 1
        for c in line:
            if c != '\n':
                if groupDict.get(c) is not None:
                    groupDict[c] = groupDict[c] + 1
                else:
                    groupDict[c] = 1
    else:
        print(f"Part answer:{ans} People in Group:{peopleCounter} :{groupDict} : {len(groupDict)} ")
        for x in groupDict:
            if (groupDict.get(x) is not None) and (groupDict.get(x) == peopleCounter): ans += 1
        groupDict = {}
        peopleCounter = 0


print(f"Answer:{ans}")







