from collections import defaultdict
import time
start_time = time.time()

file1= open('aoc18_input.txt', 'r')

expression_counter = 0
expressions = defaultdict(str)

for line in file1.readlines():
    expressions[expression_counter] = line.strip().replace(' ','')
    expression_counter += 1

print(expressions)

def find_matching_p(input):
    count_p = 0
    index = 0
    for c in input:
        if c == ')':
            count_p +=1
        elif c == '(' and count_p == 1:
            return index
        elif c == '(' and count_p != 1:
            count_p -= 1
        index +=1
    return index

def funkis(input):
    c = input[0]
    input_length = len(input)
    if input_length == 1:
        return int(c)
    op = input[1]
    if op == '+':
        return  funkis(input[2:]) + int(c)
    elif op == '*':
        return  funkis(input[2:]) * int(c)
    elif c == ')':
        p = find_matching_p(input)
        if p == input_length -1:
            return funkis(input[1:p])
        else:
            if input[p + 1] == '+': return funkis(input[p + 2:]) + funkis(input[1:p])
            if input[p + 1] == '*': return funkis(input[p + 2:]) * funkis(input[1:p])
        #funkis(input[0:find_matching(input)]
    else:
        print(f"WTF:{c} {op}")
        return 0


#test1 = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'.replace(' ','')
#test = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'.replace(' ','')
#test = '1 + 2 * 3 + 4 * 5 + 6'.replace(' ','')[::-1]
#print(f"Sum:{funkis(test)}")

ans = 0
for k,v in expressions.items():
    ans += funkis(v[::-1])
print(f"Sum:{ans}")

print("--- %s seconds ---" % (time.time() - start_time))