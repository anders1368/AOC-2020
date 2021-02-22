from collections import deque, defaultdict

#file1 = open('aoc08_1_test1_input.txt', 'r')
file1 = open('aoc08_1_input.txt', 'r')


def extract_row(input_tuple):
    return int(input_tuple[0])
def extract_operator(input_tuple):
    return input_tuple[1]
def extract_value(input_tuple):
    return int(input_tuple[2])
def extract_loop_depth(input_tuple):
    return int(input_tuple[3])
def increase_depth(input_tuple):
    return tuple((input_tuple[0],input_tuple[1],input_tuple[2],str(int(input_tuple[3])+1)))

def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph.get(state, []):
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))


program = deque()
accumulator = 0

lines=file1.readlines()
index=0

for line in lines:
    #print(f"{index},{line}")
    program.append(tuple((str(index) + ' ' + line + ' 0').strip().split()))
    index += 1

for each in program:
    print(f"{extract_row(each)}:{extract_operator(each)}:{extract_value(each)}:{extract_loop_depth(each)}")

jmpandnoptargetlist = list()

programpointer = 0
run = True
instructioncounter = 0

while run:
    instructioncounter +=1
    if programpointer >= len(program):
        break
    #Get the instruction and increase depth
    instruction = increase_depth(program[programpointer])
    print(f"Row:{instructioncounter}:{programpointer}:Instruction:{instruction}")
    if extract_loop_depth(instruction) > 1:
        break
    # instruction decoder
    program[programpointer] = instruction
    if extract_operator(instruction) == 'nop':
        jmpandnoptargetlist.append(programpointer + extract_value(instruction))
        programpointer +=1
    elif extract_operator(instruction) == 'acc':
        accumulator += extract_value(instruction)
        programpointer += 1
    elif extract_operator(instruction) == 'jmp':
        jmpandnoptargetlist.append(programpointer + extract_value(instruction))
        programpointer += extract_value(instruction)
    else:
        break
print(f"Programpointer:{programpointer}:Accumulator:{accumulator}:program:{program}")
print(jmpandnoptargetlist)



graph = defaultdict()

#Build the graph
programpointer = 0
for instruction in program:
    print(f"{programpointer}: {instruction}")
    if extract_operator(instruction) == 'nop':
        graph[extract_row(instruction)] = [extract_row(instruction) + 1]
    elif extract_operator(instruction) == 'acc':
        graph[extract_row(instruction)] = [extract_row(instruction) + 1]
    elif extract_operator(instruction) == 'jmp':
        graph[extract_row(instruction)] = [extract_row(instruction) + extract_value(instruction)]
    else:
        print(f"Opps")
    programpointer +=1


#print(graph)
cycles = [[node]+path for node in graph for path in dfs(graph, node, node)]
#print(cycles)
#print(len(cycles))
for each in cycles:
    print(f"{max(each)}:{each}")

