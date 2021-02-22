from collections import defaultdict

#file1 = open('aoc07_1_test_input.txt', 'r')
#file1 = open('aoc07_2_test_input.txt', 'r')
file1 = open('aoc07_1_alternative_input.txt', 'r')
Lines = file1.readlines()

comboDict = defaultdict(list)


def parse_bags():
    combo_dict = defaultdict(list)
    for line in Lines:
        bagdep = line.strip().split(',')
        first = True
        for bag in bagdep:
            bagfeatures = bag.strip().split(' ')
            numberof = bagfeatures[0]
            finish = bagfeatures[1]
            color = bagfeatures[2]
            if first:
                key = finish + ":" + color
                first = False
                combo_dict[key] = []
            else:
                combo_dict[key].append(numberof + ":" + finish + ":" + color)
    return combo_dict

def dfs(inputList, inputDict):
    if inputList == []:
        return 0
    if (inputList == ['0:empty:other']):
        return 0

    head, *tail = inputList

    headitems=head.split(':')
    numberof = int(headitems[0])
    finish = headitems[1]
    color = headitems[2]

    if tail == []:
        return numberof + (numberof * dfs(inputDict[finish + ':'+ color], inputDict))
    else:
        return (numberof + (numberof * dfs(inputDict[finish + ':'+ color], inputDict))) + dfs(tail, inputDict)

#Parse the bags into a dict with contained bags as a List
comboDict = parse_bags()
print(f"Length: {len(comboDict)}:{comboDict}")

#print(f"{unravelrules(['bright:white','muted:yellow'], comboDict)}")
#print(f"Part2:{unravelrules(['1:dark:olive', '2:vibrant:plum'],comboDict)}")
#print(f"Part2:{unravelrules(['2:dark:red'],comboDict)}")
print(f"Part2:{dfs(['3:wavy:gold'], comboDict)}")

