import numpy as np
import time
start_time = time.time()

hex_grid_size = 250
offset = 125
#y,x
#0 = white
#1 = black
hexboard = np.zeros((hex_grid_size, hex_grid_size), int)

#y,x
reference_point = (offset,offset)

#y,x
#hex tile represeted as double X coordinate
def e(input_position):
    return (input_position[0],input_position[1]+2)
def w(input_position):
    return (input_position[0],input_position[1]-2)
def ne(input_position):
    return (input_position[0]-1,input_position[1]+1)
def nw(input_position):
    return (input_position[0]-1,input_position[1]-1)
def se(input_position):
    return (input_position[0]+1,input_position[1]+1)
def sw(input_position):
    return (input_position[0]+1,input_position[1]-1)

def count_neighbours(input_position, input_hexgrid):
    sum_neighbours = 0
    #e
    p = e(input_position)
    sum_neighbours += input_hexgrid[p[0],p[1]]
    #w
    p = w(input_position)
    sum_neighbours += input_hexgrid[p[0], p[1]]
    #ne
    p = ne(input_position)
    sum_neighbours += input_hexgrid[p[0], p[1]]
    #nw
    p = nw(input_position)
    sum_neighbours += input_hexgrid[p[0], p[1]]
    #se
    p = se(input_position)
    sum_neighbours += input_hexgrid[p[0], p[1]]
    #sw
    p = sw(input_position)
    sum_neighbours += input_hexgrid[p[0], p[1]]
    return sum_neighbours

def move_direction(input_direction, input_position):
    if input_direction == 'e':
        return e(input_position)
    elif input_direction == 'w':
        return w(input_position)
    elif input_direction == 'ne':
        return ne(input_position)
    elif input_direction == 'nw':
        return nw(input_position)
    elif input_direction == 'se':
        return se(input_position)
    elif input_direction == 'sw':
        return sw(input_position)
    else:
        print(f"WTF!! Illigal direction:{input_direction}!")

#part 1
file1= open('aoc24_input.txt', 'r')
for line in file1.readlines():
    trailing = ''
    position = reference_point
    for c in line.strip():
        if c == 'n' or c == 's':
            trailing = c
        else:
            move = trailing + c
            position = move_direction(move,position)
            trailing = ''
    #flip
    if (position[0] > hex_grid_size -2) or (position[1] > hex_grid_size -2) or (position[0] < 2) or (position[1] < 2):
        print(f"OUT OF BOUNDS!")
    hexboard[position[0],position[1]] = ((hexboard[position[0],position[1]] + 1) % 2)

print(hexboard)
print(f"Part1: {np.sum(hexboard[:, :])}")

#part 2
for i in range(100):
    next_hexboard = np.zeros((hex_grid_size,hex_grid_size), int)
    row = 2
    while (row < (hex_grid_size - 2)):
        #odd even starting x coordinate
        col = 2 if ((row %2) == 0) else 3
        while (col < (hex_grid_size -2)):
            y,x = row, col
            v= hexboard[y,x]
            neighbours = count_neighbours((y,x),hexboard)
            #copy value then apply rules
            next_hexboard[y, x] = v
            #if black and.... flip to white
            if (v == 1) and (neighbours == 0 or neighbours > 2): next_hexboard[y, x] = 0
            #if white and ... flip to black
            if (v == 0) and (neighbours == 2): next_hexboard[y, x] = 1
            #double x coordinate. So jump 2
            col += 2
        row += 1
    hexboard = next_hexboard.copy()
    #print(hexboard)
    print(f"Day{i+1} {np.sum(hexboard[:, :])}")

#print(f"e:{e((4,6))} w:{w((4,6))} ne:{ne((4,6))} nw:{nw((4,6))} {se((4,6))} {sw((4,6))}")
print(hexboard)
print("--- %s seconds ---" % (time.time() - start_time))