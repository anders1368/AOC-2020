from collections import defaultdict, deque
import time
start_time = time.time()

#file1= open('aoc19_test_rules.txt', 'r')
#file2= open('aoc19_test_input.txt', 'r')
file1= open('aoc19_1_rules_input.txt', 'r')
file2= open('aoc19_1_input.txt', 'r')



input_rules = defaultdict(list)
for line in file1.readlines():
    rule = line.strip().split(':')
    node = []
    for i in rule[1].strip().split('|'):
        for j in i.strip().split(' '):
            node.append(j.replace('"',''))
        input_rules[rule[0]].append(node)
        node = []

input_to_check = []
for line in file2.readlines():
    input_to_check.append(line.strip())

print(input_rules)
print(input_to_check)
#sort_rules = sorted(input_rules.items())
#print(sort_rules)
stack = deque()
stack.append(input_rules['0'][0])

expanded_rules = []



while len(stack) != 0:
    current_rules = stack.pop()
    next_rules,split_rules = [],[]
    #['4','1','5']
    i = 0
    for rule in current_rules:
        i += 1
        if (rule == 'a') or (rule == 'b'):
            next_rules.append(rule)
            split_rules.append(rule)
        else:
            lookup = input_rules[rule]
            #[['2', '3'], ['3', '2']]
            if len(lookup) == 1:
                #NO OR e.g. [['a']] or [['8']]
                for r in lookup[0]:
                    next_rules.append(r)
                    split_rules.append(r)
            else:
                #OR
                #First group
                for r in lookup[0]:
                    next_rules.append(r)
                for r in lookup[1]:
                    split_rules.append(r)
                for r in current_rules[i:]:
                    next_rules.append(r)
                    split_rules.append(r)
                stack.append(split_rules)
                break
    if next_rules.count('a') + next_rules.count('b') == len(next_rules):
        #Rule is complete move to finished rules
        expanded_rules.append(''.join(next_rules))
    else:
        stack.append(next_rules)
    #print(f"Stack:{len(stack)} depth:{i}")
    #print(f"Stack:{len(stack)}")
    #print(f"Expanded Rules({len(expanded_rules)}):{expanded_rules}")
    #print(f"Expanded Rules({len(expanded_rules)})")


#print(f"Expanded Rules({len(expanded_rules)}):{expanded_rules}")
#print(f"Input_to_check({len(input_to_check)}):{input_to_check}")
print(f"{len(set(expanded_rules).intersection(input_to_check))} {set(expanded_rules).intersection(input_to_check)}")
print("--- %s seconds ---" % (time.time() - start_time))