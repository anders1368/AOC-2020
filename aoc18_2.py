from collections import defaultdict
import time
import re

start_time = time.time()

file1= open('aoc18_input.txt', 'r')

expression_counter = 0
expressions = defaultdict(str)

for line in file1.readlines():
    expressions[expression_counter] = line.strip().replace(' ','')
    expression_counter += 1

#print(expressions)

def pair(input):
    s = input.split('+')
    if len(s) > 1:
        v1 = int(s[0])
        v2 = int(s[1])
        return str(v1 + v2)
    else:
        s = input.split('*')
        v1 = int(s[0])
        v2 = int(s[1])
        return str(v1 * v2)

def tripple(input):
    v1 = int(input[0])
    op1 = input[1]
    v2 = int(input[2])
    op2 = input[3]
    v3 = int(input[4])

    if op1 == '*' and op2 == '*': return v1 * v2 * v3
    if op1 == '+' and op2 == '+': return v1 + v2 + v3
    if op1 == '*' and op2 == '+': return v1 * (v2 + v3)
    if op1 == '+' and op2 == '*': return (v1 + v2) * v3

# [(m.start(0), m.end(0)) for m in re.finditer('[0-9]\+[0-9]', test)]

def func_reduce_add_pairs(input):
    m = re.search('[0-9]+\+[0-9]+', input)
    if m != None:
        return input[:m.start()] + pair(input[m.start():m.end()]) + func_reduce_add_pairs(input[m.end():])
    else:
        return input

def func_reduce_multi_pairs_p(input):
    m = re.search('\([0-9]+\*[0-9]+\)', input)
    if m != None:
        return input[:m.start()+1] + pair(input[m.start()+1:m.end()-1]) + func_reduce_multi_pairs_p(input[m.end()-1:])
    else:
        return input

def func_reduce_multi_pairs(input):
    m = re.search('(?<!\+)[0-9]+\*[0-9]+(?![\+0-9])', input)
    if m != None:
        return input[:m.start()] + pair(input[m.start():m.end()]) + func_reduce_multi_pairs(input[m.end():])
    else:
        return input

def func_reduce_p(input):
    m = re.search('\([0-9]+\)', input)
    if m != None:
        return input[:m.start()] + input[m.start()+1:m.end()-1] + func_reduce_p(input[m.end():])
    else:
        return input


def func_reducer(test):
    reducer = True
    last_counter = 0
    counter = -1
    while counter < 1000:
        lt = 0
        last_counter = counter
        while lt != len(test):
            lt = len(test)
            test = func_reduce_multi_pairs_p(test)
            test = func_reduce_p(test)
            test = func_reduce_multi_pairs(test)
            test = func_reduce_p(test)
            #print(f"Multi_(X*Y):{test}")

        lt = 0
        while lt != len(test):
            lt = len(test)
            test = func_reduce_add_pairs(test)
            test = func_reduce_p(test)
            #print(f"add:{test}")
        counter += 1
    return test

def func_final_reduce(param):
    s = param.split('*')
    if len(s) > 1:
        v1 = int(s[0])
        v2 = int(s[1])
        return str(v1 * v2)
    else:
        return param

ans = 0

for k,v in expressions.items():
    #a = func_final_reduce(func_reducer(v))
    a=func_reducer(v)
    print(f"DONE WITH:{a}")
    ans += int(a)
print(f"Sum:{ans}")



print("--- %s seconds ---" % (time.time() - start_time))