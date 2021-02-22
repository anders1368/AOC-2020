import re

#file1 = open('aoc10_1_test2_input.txt', 'r')
#file1 = open('aoc10_1_test1_input.txt', 'r')
file1 = open('aoc10_1_input.txt', 'r')

def countgaps(sortedinputlist):
    trailer = 0  # init to wall socket value
    ones,twos,threes = 0,0,0
    for each in sortedinputlist:
        if (each - trailer) == 1:
            ones +=1
        elif (each - trailer) == 2:
            twos += 1
        elif (each - trailer) == 3:
            threes += 1
        else:
            print(f"Gap to wide")
            break
        trailer = each
    return [ones,twos,threes]

def groupgaps(sortedinputlist):
    trailer = 0  # init to wall socket value
    ones,twos,threes = [0],[],[]
    returnlist=[]

    for each in sortedinputlist:
        if (each - trailer) == 1:
            ones = ones + [each]
            if (twos != []):
                returnlist.append(twos)
                twos = []
            if (threes != []):
                returnlist.append(threes)
                threes = []
        elif (each - trailer) == 2:
            twos = twos + [each]
            if (ones != []):
                returnlist.append(ones)
                ones = []
            if (threes != []):
                returnlist.append(threes)
                threes = []
        elif (each - trailer) == 3:
            threes = threes + [each]
            if (ones != []):
                returnlist.append(ones)
                ones = []
            if (twos != []):
                returnlist.append(twos)
                twos = []
        else:
            print(f"Gap to wide")
            break
        trailer = each
    return returnlist

def grouponegaps(sortedinputlist):
    trailer = 0  # init to wall socket value
    ones,twos,threes = [0],[],[]
    returnlist=[]

    for each in sortedinputlist:
        if (each - trailer) == 1:
            if (ones != []) or trailer == 0:
                ones = ones + [each]
            else:
                ones = [trailer] + [each]
            if (twos != []):
                #returnlist.append(twos)
                twos = []
            if (threes != []):
                #returnlist.append(threes)
                threes = []
        elif (each - trailer) == 2:
            twos = twos + [each]
            if (ones != []):
                returnlist.append(ones)
                ones = []
            if (threes != []):
                #returnlist.append(threes)
                threes = []
        elif (each - trailer) == 3:
            threes = threes + [each]
            if (ones != []):
                returnlist.append(ones)
                ones = []
            if (twos != []):
                #returnlist.append(twos)
                twos = []
        else:
            print(f"Gap to wide")
            break
        trailer = each
    return returnlist

def func_lengthsofsublist(list):
    returnlist = [] #list with lengts of sublists in input
    for each in list:
       returnlist = returnlist + [len(each)]
    return returnlist

def func_combination_with_binary_mask(mask,number):
    maxcombinations = 2 ** number
    i = 0
    formatstring = "0" + str(number) + "b"
    countofnumberswithmask = 0
    while (i < maxcombinations):
        binarystring = format(i, formatstring)
        if (re.match(mask, binarystring)):
            countofnumberswithmask += 1
        i += 1
    return i-countofnumberswithmask

#init
inputlist = []
for line in file1.readlines():
    inputlist += [int(line.strip())]
print(inputlist)
inputlist.sort()
#add the socket and the built in adapter
inputlist = inputlist + [inputlist[-1] + 3]

print(countgaps(inputlist))
print(f"Answer:{countgaps(inputlist)[0]*countgaps(inputlist)[2]}")

extractedonegroups = grouponegaps(inputlist)

ans = 1
lengthlist = func_lengthsofsublist(extractedonegroups)
print(lengthlist)

for each in lengthlist:
    if each < 3:
        ans = ans
    else:
        ans = ans * func_combination_with_binary_mask(".*000.*",each-2)



print(f"Answer:{ans}")

