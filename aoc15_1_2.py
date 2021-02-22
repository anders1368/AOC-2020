from collections import defaultdict

#input = [ '0','3','6']
#lastplayed = 6
#input = ['1','3','2']
#lastplayed = 2
#input = [ '3','1','2']
#lastplayed = 2
input = [ '1','0','18','10','19','6']
lastplayed = 6

d_int = defaultdict(list)
count = 0
for i in input:
    d_int[i].append(count)
    count +=1

print(d_int)
#print(d_int['a'])

for j in range(len(d_int),30000001):
    turn_list = d_int[str(lastplayed)]
    # first time played?
    if len(turn_list) == 1:
        play = 0
    else:
        play = turn_list[-1] - turn_list[-2]
    d_int[str(play)].append(j)
    if len(d_int[str(play)]) > 2:
        d_int[str(play)].pop(0)
    #print every n loop
    if (j % 1000000) == 0:
        print(f"Turn:{j} played:{play} lastplayed:{lastplayed}")
    lastplayed = play