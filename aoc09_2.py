#file1 = open('aoc09_1_test_input.txt', 'r')
file1 = open('aoc09_1_input.txt', 'r')

#init
slidingwindowlist = []
inputlist = []
for line in file1.readlines():
    inputlist += [int(line.strip())]
#windowsum, target = 0, 62
windowsum, target = 0, 22477624
#looooop
while (len(inputlist) > 0):
    if (windowsum == target):
        print(f"Target:{target} is in the window:{slidingwindowlist}")
        break
    if (windowsum < target):
        slidingwindowlist = slidingwindowlist + [inputlist.pop(0)]
        windowsum = windowsum + slidingwindowlist[-1]
    else:
        removednumber = slidingwindowlist.pop(0)
        windowsum = windowsum - removednumber

slidingwindowlist.sort()
print(slidingwindowlist[0] + slidingwindowlist[-1])
