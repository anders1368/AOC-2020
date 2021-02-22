file1 = open('aoc03_1_input.txt', 'r')
Lines = file1.readlines()


startingposition = int('1000000000000000000000000000000',2)
#1073741824
wrapposition = int('1111111111111111111111111111111',2)
#2147483647

# Strips the newline character



#x = 0
#y = 0
length = 31
totalhitcounter = 1

for tracks in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    hitcounter = 0
    count = 0
    currentposition = startingposition
    for line in Lines:
        binarystring = line.strip()
        trackrow = int(binarystring, 2)
        if (count % tracks[1] == 0):
            if ((trackrow & currentposition) > 0) : hitcounter = hitcounter + 1
            print(f"{format(trackrow, '031b')} {format(currentposition, '031b')} Line{count}:{hitcounter}")
            currentposition = ((currentposition << (length - tracks[0])) % wrapposition)
        else:
            print(f"{format(trackrow, '031b')} {format(0, '031b')} Line{count}:{hitcounter}")
        count = count +1
    totalhitcounter *= hitcounter
    print(f'ans:{hitcounter} : {totalhitcounter}')