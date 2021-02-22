# Using readlines()
from re import finditer

file1 = open('aoc05_1_input.txt', 'r')
Lines = file1.readlines()

matrix = [[0 for x in range(8)] for y in range(128)]
ans = 0
id=0
#part 1
for line in Lines:
    rowint= int(line[0:7],2)        #row bits to int
    colint= int(line[7:10],2)       #col bits to int
    matrix[rowint][colint] = 1      # inject for part 2
    id=(rowint*8)+colint
    if (id>=ans): ans = id
print(f"Answer 1: {ans}")

#part 2

# flatten to string added for proper search
searchstring =""

for rowindex,x in enumerate(matrix):
    for colindex,y in enumerate(x):
        print(f"{y}",end='')
        searchstring+=str(y)        # search this string
    print(f":{rowindex}")
#Occular inspection, looking for that 101

#do the search
for match in finditer("101", searchstring):
    print(match.span(), match.group())

