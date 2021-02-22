import time
from collections import defaultdict

start_time = time.time()

#test_input = '389125467'
#test_input = '123456789'
test_input = '198753462'

max_value = 1000000
circle = [int(x) for x in test_input]
circle_part2 = [int(x) for x in range(10,max_value + 1)]
circle = circle + circle_part2


ll = defaultdict(int)
modulo = len(circle)
for i in range(modulo):
    ll[circle[i]] = circle[(i+1) % modulo]


def pretty_print(input_ll,position):
    print(f"Cups: ",end='')
    #always start from value 1
    cup_value = 1
    next_cup_value = input_ll[cup_value]
    while next_cup_value != 1:
        if cup_value == position:
            print(f"({cup_value}) ",end='')
        else:
            print(f"{cup_value} ", end='')
        cup_value = next_cup_value
        next_cup_value = input_ll[cup_value]
    if cup_value == position:
        print(f"({cup_value}) ",end='')
    else:
        print(f"{cup_value} ", end='')
    print(f"")


moves = 1
cc = 1

while moves < 10000001:
    #Print nice
    #print(f"-- Move:{moves} --")
    #pretty_print(ll, cc)
    #Pick up 3 after current cup
    pickup_list = []
    pickup = ll[cc]
    for i in range(3):
        pickup_list.append(pickup)
        pickup = ll[pickup]
    #Repoint current to first cup after pickup
    ll[cc] = ll[pickup_list[2]]

    #print(f"Pick up:{pickup_list}")

    #destination
    destination = cc - 1 if cc > 1 else max_value
    while destination in pickup_list:
        destination = destination - 1 if destination > 1 else max_value

    #drop in pickup list
    ll[pickup_list[2]] = ll[destination]
    ll[destination] = pickup_list[0]
    cc = ll[cc]
    moves +=1

#final
print(f"Final:")
print(ll[1]*ll[ll[1]])



print("--- %s seconds ---" % (time.time() - start_time))