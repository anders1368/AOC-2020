# importing "heapq" to implement heap queue
import heapq
import itertools as it

# initializing list
#file1 = open('aoc09_1_test_input.txt', 'r')
file1 = open('aoc09_1_input.txt', 'r')
#li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
inputlist = []
slidingwindowlist = []

lines=file1.readlines()
for line in lines:
    inputlist += [int(line.strip())]

windowsize = 25
# init window and input
i = 0
while (i < windowsize):
    slidingwindowlist = slidingwindowlist + [inputlist.pop(0)]
    i += 1

while (len(inputlist) > 0):
    # dedup the sliding window and pop first of rest to be the target sum
    lst = list(dict.fromkeys(slidingwindowlist))
    target = inputlist.pop(0)
    sumcombolist = [sum(i) for i in list(it.combinations(lst, 2))]
    hits = [i for i in sumcombolist if i == target]
    if hits == []:
        print(f"Target:{target} does not exist!")
        break
    #slide window
    slidingwindowlist.pop(0)
    slidingwindowlist = slidingwindowlist + [target]



#lst, target = slidingwindowlist, 40
#lst, target = [1, 1, 4, 6, 7, 8], 5
#print(lst)
#lst = list(dict.fromkeys(lst))
#print(lst)
#results = [sum(i) for i in list(it.combinations(lst, 2))]
#print(results)

#print([i for i in results if i == target])

print(slidingwindowlist)

# using heapify() to convert list into heap
#heapq.heapify(slidingwindowlist)
#print(slidingwindowlist)