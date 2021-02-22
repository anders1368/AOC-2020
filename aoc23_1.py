#test_input = '389125467'
#test_input = '123456789'
test_input = '198753462'

circle = [int(x) for x in test_input]
#circle_part2 = [int(x) for x in range(10,20)]
#circle =  circle + circle_part2

def pretty_print(input_list,position, destination):
    print(f"[",end='')
    for idx,each in enumerate(input_list):
        if idx == position:
            print(f"({each}),",end='')
        elif idx == destination:
            print((f"[{each}],"),end='')
        else:
            print(f"{each},",end='')
    print(f"]")

current_cup = 0
destination_cup = -1
moves = 0
modulo = len(circle) + 1
pretty_print(circle,current_cup,destination_cup)




while moves < 100:
    pickup_list = circle[1:4]
    circle = [circle[0]] + circle[4:]
    current_cup_value = circle[current_cup] -1
    while True:
        try:
            next_val = current_cup_value % modulo
            destination_index = circle.index(next_val)
            #print(f"Found!")
            break
        except ValueError:
            current_cup_value -= 1
            #print(f"Not found lower one more step")
    circle = circle[0:destination_index + 1] + pickup_list + circle[destination_index+1:]
    circle = circle[1:] + [circle[0]]
    moves += 1
    #if moves % 100 == 0:
    #    print(f"Move:{moves} {circle[-2:] + circle[0:2]}")
    print(f"Move:{moves} {pretty_print(circle,current_cup,destination_index)}")


