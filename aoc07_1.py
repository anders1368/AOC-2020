from collections import defaultdict

file1 = open('aoc07_1_alternative_input.txt', 'r')
Lines = file1.readlines()
finishDict = defaultdict(int)
colorDict = defaultdict(int)
comboDict = defaultdict(list)

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
            comboDict[key] = []
        else:
            comboDict[key].append(finish + ":" + color)

#print(f"Length: {len(comboDict)}:{comboDict}")


def unravelrules(inputList, inputDict):
#    print(inputList)
    if inputList == []:
        return False
    if (inputList == ['shiny:gold'] or inputList[0] == ('shiny:gold')):
        return True
    if (inputList == ['empty:other']):
        return False
    head, *tail = inputList
    headlookup = inputDict[head]
    lookupfirstelement = unravelrules(headlookup,inputDict)
    if lookupfirstelement:
        return True
    else:
        return unravelrules(tail, inputDict)


#print(f"{unravelrules(['bright:white','muted:yellow'], comboDict)}")

ans = 0
for rule in comboDict:
    ruleslist=comboDict[rule]
    if unravelrules(ruleslist,comboDict):
        ans +=1
        print(f"Rule with Shiny Golde Bag! Total:{ans}")


#print(f"Part2:{unravelrules(['shiny:gold'],comboDict)}")

