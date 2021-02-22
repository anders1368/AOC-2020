from collections import defaultdict

file1 = open('aoc14_1_input.txt', 'r')

memory = defaultdict(int)
memory['0'] = 0
m1and = 0
m2or = 0

for line in file1.readlines():
    command = line.strip().split('=')[0].strip()
    command_input = line.strip().split('=')[1].strip()
    if command == 'mask':
        m1and = int(command_input.replace('X','1'),2)
        m2or = int(command_input.replace('X','0'),2)
        print(f"M1{m1and} M2{m2or}")
    else:
        memoryaddress = command[4:-1]
        value = int(command_input)
        memory[memoryaddress] = (value & m1and) | m2or
        print(f"{memoryaddress}:{value}")

    print(f"Mem:{memory}")
ans = 0

for index in memory:
    print(memory[index])
    ans += memory[index]
print(f"Ans:{ans}")

