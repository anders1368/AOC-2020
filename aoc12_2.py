file1 = open('aoc12_1_input.txt', 'r')
nav_instructions = []

for line in file1.readlines():
    nav_instructions.append(list(line.strip()))

def R90(pos):
    return [pos[1], pos[0] * -1]

b_pos = list((0, 0))
wp_pos = list((10, 1))

for ins in nav_instructions:
    ins_t = ins[0]
    ins_val = int(''.join(ins[1:]))
    if (ins_t == 'L' and ins_val == 270) or (ins_t == 'R' and ins_val == 90):
        wp_pos = R90(wp_pos)
    if (ins_t == 'L' and ins_val == 180) or (ins_t == 'R' and ins_val == 180):
        for i in range(2): wp_pos = R90(wp_pos)
    if (ins_t == 'L' and ins_val == 90) or (ins_t == 'R' and ins_val == 270):
        for i in range(3): wp_pos = R90(wp_pos)
    if ins_t == 'F':
        #Only boat action
        b_pos[0] = b_pos[0] + (ins_val * wp_pos[0])
        b_pos[1] = b_pos[1] + (ins_val * wp_pos[1])
    else:
        if ins_t == 'N': wp_pos[1] = wp_pos[1] + ins_val
        if ins_t == 'E': wp_pos[0] = wp_pos[0] + ins_val
        if ins_t == 'S': wp_pos[1] = wp_pos[1] - ins_val
        if ins_t == 'W': wp_pos[0] = wp_pos[0] - ins_val

print(f"{b_pos}")
print(f"{wp_pos}")
print(f"{abs(b_pos[0]) + abs(b_pos[1])}")
