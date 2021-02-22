file1= open('aoc13_input.txt','r')
input_busses = []
for line in file1.readlines():
    input_busses = line.strip().split(',')



input_t = 1002576
max_t = input_t + 500

print(f"Time:{input_t} Buslines:{input_busses}")
for current_t in range(input_t,max_t):
    for each_bus in input_busses:
        if (each_bus != 'x'):
            bus = int(each_bus)
            if current_t % bus == 0:
                print(f"Bus:{each_bus} leaves now({current_t}) answer:{(current_t-input_t)*bus}")