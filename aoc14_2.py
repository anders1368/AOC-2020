from collections import defaultdict

file1 = open('aoc14_1_input.txt', 'r')


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def mem_exp(memory_pointer, mask):
    expander = find(mask, 'X')
    expander_binary_length = len(expander)
    address_binary = format(memory_pointer, '036b')
    memory_pointer_list = list()
    for i in range(2**expander_binary_length):
        b = format(i, '0'+str(expander_binary_length)+'b')
        for j in range(expander_binary_length):
            address_binary = address_binary[:expander[j]] + b[-j] + address_binary[expander[j] + 1:]
        memory_pointer_list.append(int(address_binary, 2))
    return memory_pointer_list

memory = defaultdict(int)

for line in file1.readlines():
    command = line.strip().split('=')[0].strip()
    command_input = line.strip().split('=')[1].strip()
    if command == 'mask':
        mask0 = command_input
        mask1 = command_input.replace('X', '0')
    else:
        memory_pointer = int(command[4:-1]) | int(mask1, 2)
        value = int(command_input)
        memory_pointer_list = mem_exp(memory_pointer, mask0)
        for memory_pointer_from_list in memory_pointer_list:
            memory[str(memory_pointer_from_list)] = value
ans = 0
for i in memory:
    ans += memory[i]
print(f"Ans:{ans}")
#print(f"Mem:{memory}")

