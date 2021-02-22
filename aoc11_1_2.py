from copy import deepcopy

file1 = open('aoc11_1_input.txt', 'r')

roommatrix = []

row_maxindex = 0
col_maxindex = 0

for line in file1.readlines():
    roommatrix.append(list(line.strip()))

row_maxindex = len(roommatrix)
if row_maxindex > 0:
    col_maxindex = len(roommatrix[0])

def func_pp_matrix(inputmatrix):
    for i in range(len(inputmatrix)):
        for j in range(len(inputmatrix[i])):
            print(inputmatrix[i][j],end='')
        print('')

def func_isemptyaround(row,col,inputmatrix):
    #emptypattern = [['L','L','L'],['L','L','L'],['L','L','L']]
    #nochairpattern = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    e = 'L'
    floor = '.'
    full = '#'
    returnvalue = True
    for i in range(3):
        row_offset = row - 1 + i
        if row_offset < 0 or row_offset >= row_maxindex:
            returnvalue = True
        else:
            for j in range(3):
                col_offset = col - 1 + j
                if col_offset < 0 or col_offset >= col_maxindex:
                    returnvalue = True
                else:
                    seat = inputmatrix[row_offset][col_offset]
                    returnvalue = (full != seat)
                if returnvalue == False:
                    break
        if returnvalue == False:
            break
    return returnvalue

def func_isfullaround(row,col,inputmatrix):
    e = 'L'
    floor = '.'
    full = '#'
    countfull=0

    for i in range(3):
        row_offset = row - 1 + i
        if row_offset >= 0 and row_offset < row_maxindex:
            for j in range(3):
                col_offset = col - 1 + j
                if col_offset >= 0 and col_offset < col_maxindex:
                    seat = inputmatrix[row_offset][col_offset]
                    if seat == full:
                        countfull += 1

    return countfull >= 4

def func_look_x_steps(row,col,row_dir,col_dir,steps,inputmatrix):
    #print(f"row:{row}:col{col} d:{row_dir}:{col_dir} ",end='')
    for i in range(steps):
        #print(f"step{i}:",end='')
        row += row_dir
        col += col_dir
        if row < 0 or row >= row_maxindex:
            #print("X")
            return True
        elif col < 0 or col >= col_maxindex:
            #print("X")
            return True
        elif inputmatrix[row][col] == '#':
            c = inputmatrix[row][col]
            #print(f"{c}")
            return False
        elif inputmatrix[row][col] == 'L':
            c = inputmatrix[row][col]
            #print(f"{c}")
            return True
        else:
            c = inputmatrix[row][col]
            #print(f"{c}",end='')
    #print("WTF!")
    #func_pp_matrix(inputmatrix)
    return True




def func_isfreeXsteps(row,col,steps,inputmatrix):
   ans = 0
   if func_look_x_steps(row, col, 0, -1, steps, inputmatrix): ans += 1
   if func_look_x_steps(row, col, -1, -1, steps, inputmatrix): ans += 1
   if func_look_x_steps(row, col, -1, 0, steps, inputmatrix): ans += 1
   if func_look_x_steps(row, col, -1, 1, steps, inputmatrix): ans += 1
   if func_look_x_steps(row, col, 0, 1, steps, inputmatrix): ans += 1
   if func_look_x_steps(row, col, 1, 1, steps, inputmatrix): ans += 1
   if func_look_x_steps(row, col, 1, 0, steps, inputmatrix): ans += 1
   if func_look_x_steps(row, col, 1, -1, steps, inputmatrix): ans += 1
   #print(f"row:{row}:col{col} numberof free: {ans}:{ans >= 8} ")
   return ans >= 8

def func_isvisiblyfullaround(row,col,steps,inputmatrix):
    ans = 0
    if not func_look_x_steps(row, col, 0, -1, steps, inputmatrix): ans += 1
    if not func_look_x_steps(row, col, -1, -1, steps, inputmatrix): ans += 1
    if not func_look_x_steps(row, col, -1, 0, steps, inputmatrix): ans += 1
    if not func_look_x_steps(row, col, -1, 1, steps, inputmatrix): ans += 1
    if not func_look_x_steps(row, col, 0, 1, steps, inputmatrix): ans += 1
    if not func_look_x_steps(row, col, 1, 1, steps, inputmatrix): ans += 1
    if not func_look_x_steps(row, col, 1, 0, steps, inputmatrix): ans += 1
    if not func_look_x_steps(row, col, 1, -1, steps, inputmatrix): ans += 1
    #print(f"row:{row}:col{col} occupied: {ans}:{ans >= 5}")
    return ans >= 5

def func_countoccupied(inputmatrix):
    returvalue = 0
    for each in inputmatrix:
        returvalue = returvalue + each.count('#')
    return returvalue

print(f"width:{col_maxindex}:height:{row_maxindex}")
func_pp_matrix(roommatrix)

last_matrix = deepcopy(roommatrix)
new_matrix = deepcopy(roommatrix)
i = 0
for i in range(100):
    new_matrix = deepcopy(last_matrix)
    print(f"Round{i}")
    print("Sit")
    for i in range(row_maxindex):
        for j in range(col_maxindex):
            if last_matrix[i][j] != '.':
                if func_isfreeXsteps(i,j,105,last_matrix):
                    new_matrix[i][j] ='#'
    #func_pp_matrix(new_matrix)
    print(f"Occu: {func_countoccupied(new_matrix)}")
    last_matrix = deepcopy(new_matrix)

    print("Leave")
    for i in range(row_maxindex):
        for j in range(col_maxindex):
            if last_matrix[i][j] == '#':
                if func_isvisiblyfullaround(i,j,105,last_matrix):
                    new_matrix[i][j] = 'L'
    #func_pp_matrix(new_matrix)
    print(f"Occu: {func_countoccupied(new_matrix)}")
    last_matrix = deepcopy(new_matrix)
    #print(last_matrix == res2matrix)