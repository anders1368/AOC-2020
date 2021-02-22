import numpy as np

offset = 12
cube_size = 25
cube = np.zeros((cube_size, cube_size, cube_size), int)
#z,y,x

file1= open('aoc17_input.txt', 'r')
ycounter = 0
for line in file1.readlines():
    xcounter = 0
    for c in line.strip():
        if c == '#': cube[offset, offset + ycounter, offset + xcounter] = 1
        xcounter +=1
    ycounter +=1



#print(cube)
for i in range(6):
    print(f"Iteration:{i}")
    next_cube = np.zeros((cube_size, cube_size, cube_size), int)
    for index, v in np.ndenumerate(cube):
        z,y,x = index[0], index[1], index[2]
        neighbours = np.sum(cube[z - 1:z + 2, y - 1:y + 2, x - 1:x + 2])
        #print(f"idx:{index} {v} sum:{neighbours}")
        if (v == 1) and (neighbours == 3 or neighbours ==4): next_cube[z,y,x] = 1
        if (v == 0) and (neighbours == 3): next_cube[z, y, x] = 1
    cube = next_cube.copy()
print(cube)
print(np.sum(cube[:, :, :]))

