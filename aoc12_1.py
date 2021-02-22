file1= open('aoc12_1_input.txt', 'r')

nav_instructions = []

for line in file1.readlines():
    nav_instructions.append(list(line.strip()))


#print(func_turn(starting_position,'R90'))

position = list((0,0,90))
for instruction in nav_instructions:
    type = instruction[0]
    value = int(''.join(instruction[1:]))
    if type == 'L': position[2] = (position[2] - value) % 360
    if type == 'R': position[2]  = (position[2]  + value) % 360
    if type == 'F':
            direction = position[2]
            if direction == 0: position[1] = position[1] + value
            if direction == 90: position[0] = position[0] + value
            if direction == 180: position[1] = position[1] - value
            if direction == 270: position[0] = position[0] - value
    else:
        if type == 'N': position[1] = position[1] + value
        if type == 'E': position[0] = position[0] + value
        if type == 'S': position[1] = position[1] - value
        if type == 'W': position[0] = position[0] - value

print(f"{abs(position[0])+abs(position[1])}")
