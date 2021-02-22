
from collections import deque, defaultdict
import time
import numpy as np
start_time = time.time()

#file1= open('aoc201_test_input.txt', 'r')
file1 = open('aoc20_2_input.txt', 'r')
file2 = open('aoc20_2_monster.txt', 'r')
tiles = defaultdict()
edges = defaultdict()
corners = defaultdict()
inside = defaultdict()
edgeset = defaultdict()
tile_size = 10

def pp_tile(tile):
    for i in tile:
        for j in i:
            if j == 0: print('.',end='')
            if j == 1: print('#', end='')
        print('')
    print('')


def binary_array_to_numbers(input_array):
    binarystring = ''
    for each in input_array:
        binarystring += str(each)
    return (int(binarystring,2),int(binarystring[::-1],2))

def tile_to_numbers(tile):
    return (
        #Top
        binary_array_to_numbers(tile[0,:]),
        #Right
        binary_array_to_numbers(tile[:,tile_size-1]),
        #Bottom
        binary_array_to_numbers(tile[tile_size-1,:]),
        #Left
        binary_array_to_numbers(tile[:,0])
    )

def find_connecting_tiles(t,tiles):
    return_list = []
    for key, value in tiles.items():
        tile_values = tile_to_numbers(value)
        if (t in tile_values) or ((t[1],t[0]) in tile_values):
            #print(f"{key} : {tile_values}")
            return_list.append(key)
    return return_list

def unique_edges(tiles):
    edge_set = set()
    for key, value in tiles.items():
        flat = set(sum(tile_to_numbers(value), ()))
        edge_set = edge_set.union(flat)
    return edge_set

def align_tile_to_the_left(t,tile):
    return_tile = tile
    for i in range(4):
        left = tile_to_numbers(return_tile)[3]
        if t == left: break
        if (t[1], t[0]) == left:
            return_tile = np.flipud(return_tile)
            break
        return_tile = np.rot90(return_tile)
    return return_tile

def align_tile_to_the_above(t,tile):
    return_tile = tile
    for i in range(4):
        up = tile_to_numbers(return_tile)[0]
        if t == up: break
        if (t[1], t[0]) == up:
            return_tile = np.fliplr(return_tile)
            break
        return_tile = np.rot90(return_tile)
    return return_tile

def count_connections(tile_name,tiles):
    input_edges = tile_to_numbers(tiles[tile_name])
    nr_of_connections = 0
    for t in input_edges:
        for key, value in tiles.items():
            if key != tile_name:
                for i in tile_to_numbers(value):
                    if t == i: nr_of_connections += 1
                    elif (t[1], t[0]) == i: nr_of_connections += 1
    return nr_of_connections

def count_uniq_edges(tiles):
    for key, value in tiles.items():
        edges = tile_to_numbers(value)
        for e in edges:
            if edgeset.get(e,0) == 0:
                if edgeset.get((e[1],e[0]),0) == 0:
                    edgeset[e] = 1
                else:
                    edgeset[(e[1],e[0])] += 1
            else:
                edgeset[e] += 1
    return len(edgeset)

for lines in file1.read().split('\n\n'):
    ycounter = 0
    tile_id = ''
    # y,x
    tile = np.zeros((tile_size, tile_size), int)
    for line in lines.split('\n'):
        if line.startswith("Tile"):
            tile_id = line
        else:
            xcounter = 0
            for c in line.strip():
                if c == '#': tile[ycounter,xcounter] = 1
                xcounter += 1
            ycounter += 1
    tiles[tile_id] = tile

# y,x
monster = np.zeros((3, 20), int)
ycounter = 0
for line in file2.readlines():
    xcounter = 0
    for c in line:
        if c == '#': monster[ycounter,xcounter] = 1
        xcounter += 1
    ycounter += 1


reduced = []

sym_diff_set = set()


def find_corners():
    for key, value in tiles.items():
        flat = set(sum(tile_to_numbers(value),()))
        sym_diff_set = sym_diff_set.symmetric_difference(flat)
        reduced.append(flat)
        #print(f"{key} {tile_to_numbers(value)}")
        #print(f"{key} {flat}")
        #pp_tile(value)

    #print(set.symmetric_difference(*reduced))
    print(sym_diff_set)
    ans=1
    for key, value in tiles.items():
        flat = set(sum(tile_to_numbers(value),()))
        if len(flat.intersection(sym_diff_set)) > -1:
            print(f"{key} {flat.intersection(sym_diff_set)} : {tile_to_numbers(value)}")
            ans *= int(key.split(' ')[1][:-1])
        #pp_tile(value)

#Part 1:
    #Tile 1327: {296, 426, 82, 342} : ((82, 296), (342, 426), (358, 410), (238, 476))
    #Tile 3571: {729, 877, 731, 621} : ((169, 596), (729, 621), (877, 731), (265, 578))
    #Tile 3391: {474, 508, 366, 254} : ((254, 508), (366, 474), (298, 338), (376, 122))
    #Tile 1823: {954, 740, 157, 375} : ((42, 336), (228, 156), (954, 375), (157, 740))

print(f"Ans Part1:{1327*3571*3391*1823}")

    #Starting Tile: top left corner
    #Tile 1327: {296, 426, 82, 342} : ((82, 296), (342, 426), (358, 410), (238, 476))

def fix_a_row(i):
    # loop through the row
    for j in range(11):
        current_tile = tiles[tile_matrix[i, j]]
        tile_to_numbers(current_tile)
        # Right side
        #print(tile_to_numbers(current_tile))
        right = tile_to_numbers(current_tile)[1]
        # find connecting tile to the right
        c = find_connecting_tiles(right, tiles)
        # remove slef
        c.remove(tile_matrix[i, j])
        print(c)
        # flip it right by rotating and if needed flip
        #print(current_tile)
        next_tile = align_tile_to_the_left(right, tiles[c[0]])
        #print(next_tile)
        # update back
        tile_matrix[i, j + 1] = c[0]
        tiles[c[0]] = next_tile
        print(f"{c[0]} {tile_to_numbers(next_tile)}")

print(f"Number of tiles:{len(tiles)}")
def verify_input_slask():
    print(f"Number of uniq edges {count_uniq_edges(tiles)}")
    c_1 = 0
    c_2 = 0
    c_3 = 0
    for key, value in edgeset.items():
        if value == 1: c_1 +=1
        if value == 2: c_2 +=1
        if value >= 3: c_3 +=1
        print(f"Edge:{key}:{value}")
    print(f"1:{c_1} 2:{c_2} 3:{c_3}")

    for key, value in tiles.items():
        n = count_connections(key,tiles)
        if n == 4: inside[key] = value
        if n == 3: edges[key] = value
        if n == 2: corners[key] = value
        if n == 1: print("WTF! 1 connection")
        if n == 0: print("WTF! 0 connection")

    print(f"Insides {len(inside)}")
    print(f"Edges {len(edges)}")
    print(f"Corners {len(edges)}")

#part2
tile_matrix = np.empty((12, 12), dtype=object)
# y,x inititlize the top left corner.
tile_matrix[0, 0] = 'Tile 1327:'
tiles['Tile 1327:'] = np.rot90(tiles['Tile 1327:'])
i, j = 0, 0
print(f"Tile 1327: {tile_to_numbers(tiles['Tile 1327:'])}")
fix_a_row(i)
print(f"--------")

for i in range(1, 12):
    # Find starting tile
    first_tile = tiles[tile_matrix[i - 1, 0]]
    bottom = tile_to_numbers(first_tile)[2]
    # find connecting tile to the right
    c = find_connecting_tiles(bottom, tiles)
    # remove slef
    c.remove(tile_matrix[i - 1, 0])
    next_tile = align_tile_to_the_above(bottom, tiles[c[0]])
    # update back
    tile_matrix[i, 0] = c[0]
    tiles[c[0]] = next_tile
    print(f"{c[0]} {tile_to_numbers(next_tile)}")
    fix_a_row(i)
    print(f"--------")

print(tile_matrix)

big_pic = np.zeros((96, 96),int)
for i in range(12):
    for j in range(12):
        k = tile_matrix[i,j]
        a = tiles[k][1:9,1:9]
        big_pic[i*8:(i*8)+8,j*8:(j*8)+8] = a

big_pic =np.rot90(big_pic)
big_pic =np.rot90(big_pic)
print(big_pic)
print(np.sum(big_pic))
print(monster)
print(np.sum(monster))
monster_counter = 0
for i in range(93):
    for j in range(76):
        sub = big_pic[i:i+3,j:j+20]
        sub_and_monster = sub & monster
        if np.array_equiv(monster,sub_and_monster): monster_counter +=1
print(monster_counter)
print(np.sum(big_pic)-(np.sum(monster)*monster_counter))

print("--- %s seconds ---" % (time.time() - start_time))