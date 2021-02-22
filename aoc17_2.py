import numpy as np
import time
start_time = time.time()

offset = 7
cube_size = 30
#z,w,y,x
cube = np.zeros((cube_size, cube_size, cube_size,cube_size), int)

#parse input #->1
file1= open('aoc17_input.txt', 'r')
#init cube from file
ycounter = 0
for line in file1.readlines():
    xcounter = 0
    for c in line.strip():
        if c == '#': cube[offset, offset, offset + ycounter, offset + xcounter] = 1
        xcounter +=1
    ycounter +=1


for i in range(6):
    print(f"Iteration:{i}")
    next_cube = np.zeros((cube_size, cube_size, cube_size,cube_size), int)
    for index, v in np.ndenumerate(cube):
        z,w,y,x = index[0], index[1], index[2],index[3]
        neighbours = np.sum(cube[z - 1:z + 2,w - 1:w + 2, y - 1:y + 2, x - 1:x + 2])
        #print(f"idx:{index} {v} sum:{neighbours}")
        if (v == 1) and (neighbours == 3 or neighbours ==4): next_cube[z, w, y, x] = 1
        if (v == 0) and (neighbours == 3): next_cube[z, w, y, x] = 1
    cube = next_cube.copy()

print(np.sum(cube[:, :, :, :]))
print("--- %s seconds ---" % (time.time() - start_time))
