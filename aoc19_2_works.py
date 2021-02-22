from collections import defaultdict, deque
import time
import itertools

start_time = time.time()

file1= open('aoc19_rules_input.txt', 'r')
file2= open('aoc19_input.txt', 'r')
#file1= open('aoc192_rules2_test.txt', 'r')
#file2= open('aoc192_test2_input.txt', 'r')

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

input_per_length = defaultdict(set)

for each in input_to_check:
    input_per_length[len(each)].add(each)

def flatten_rules(input_rules,starting_rule):
    stack = deque()
    lookup = input_rules[starting_rule]
    stack.append(lookup[0])
    stack.append(lookup[1])
    return_rules = []
    while len(stack) != 0:
        current_rules = stack.popleft()
        left_rules, right_rules = [], []
        #['4','1','5']
        i = 0
        for rule in current_rules:
            i += 1
            if (rule == 'a') or (rule == 'b'):
                left_rules.append(rule)
                right_rules.append(rule)
            else:
                lookup = input_rules[rule]
                #[['2', '3'], ['3', '2']]
                if len(lookup) == 1:
                    #NO OR e.g. [['a']] or [['8']]
                    for r in lookup[0]:
                        left_rules.append(r)
                        right_rules.append(r)
                else:
                    #OR
                    #First group
                    for r in lookup[0]:
                        left_rules.append(r)
                    for r in lookup[1]:
                        right_rules.append(r)
                    for r in current_rules[i:]:
                        left_rules.append(r)
                        right_rules.append(r)
                    stack.append(right_rules)
                    break
        if (left_rules.count('a') + left_rules.count('b') == len(left_rules)):
            #Rule is complete move to finished rules
            #print(f"next rule from left:{''.join(left_rules)}")
            return_rules.append(''.join(left_rules))
        else:
            stack.append(left_rules)
        #print(f"Stack:{stack} depth:{i}")
        #print(f"Stack:{len(stack)} depth:{i}")
        #print(f"Expanded Rules({len(return_rules)}):{return_rules}")
        #print(f"Expanded Rules({len(return_rules)})")
    return return_rules

def append_rules(combined_rules):
    return_list = []
    for j in combined_rules:
        merged_rules = ''
        for each in j:
            merged_rules = merged_rules + each
        return_list.append(merged_rules)
    return return_list

def filter_rules_with_no_input_match(input_rules,input_to_check):
    return_rules = set()
    for rule in input_rules:
        count = 0
        for i in input_to_check:
            if rule in i:
                count += 1
                break
        if count > 0:
            return_rules.add(rule)
    return return_rules

def flatten_input_per_length(values):
    flat_input = set()
    for each in values:
        for v in each:
            flat_input.add(v)
    return flat_input

def match(rules,messages_per_length):
    matched_inputs = set()
    for i in range(1,15):
        print(f"Inner Loop:Iteration{i}")
        #Check length
        if (len(rules) == 0):
            break
        peek = rules.pop()
        key = len(peek)
        rules.add(peek)

        #Intersect the matches
        matched_inputs.update(messages_per_length[key].intersection(rules))
        print(f"Inner Loop:Matches Len:{len(matched_inputs)} Matches:{matched_inputs}")
        #Expand with 42
        rules = set(append_rules(list(itertools.product(expanded_rules_42,rules))))
        print(f"Inner Loop:Expanded with 42:({len(rules)})")
        #Filter rules
        flat_input = flatten_input_per_length(messages_per_length.values())
        rules = filter_rules_with_no_input_match(rules, set(flat_input))
        print(f"Inner Loop:Filtered rules:({len(rules)})")
    return matched_inputs

expanded_rules_42 = set(flatten_rules(input_rules,'42'))
expanded_rules_31 = set(flatten_rules(input_rules,'31'))
print(f"Expanded Rules 42({len(expanded_rules_42)}):{expanded_rules_42}")
print(f"Expanded Rules 31({len(expanded_rules_31)}):{expanded_rules_31}")

print("--- %s seconds ---" % (time.time() - start_time))
combined_rules = set(append_rules(list(itertools.product(expanded_rules_42,expanded_rules_42,expanded_rules_31))))
print("--- %s seconds ---" % (time.time() - start_time))
print(f"Len combined 42, 42, 31 Len:{len(combined_rules)}")

flat_input = flatten_input_per_length(input_per_length.values())
combined_rules = filter_rules_with_no_input_match(combined_rules, set(flat_input))
print(f"Len combined 42,42,31 Flat Len:{len(combined_rules)}")

total_matches = set()

for i in range(1,15):
    print(f"Outer Loop:Iteration{i}")
    total_matches.update(match(combined_rules,input_per_length))
    print(f"Outer Loop:Matches Len:{len(total_matches)} Matches:{total_matches}")
    #Add the 42,X,31
    combined_rules = set(append_rules(list(itertools.product(expanded_rules_42,combined_rules,expanded_rules_31))))
    print(f"Outer Loop:Expand with 42,X,31:{len(combined_rules)}")
    # Filter rules
    flat_input = flatten_input_per_length(input_per_length.values())
    combined_rules = filter_rules_with_no_input_match(combined_rules, set(flat_input))
    print(f"Outer Loop:Filtered rules:({len(combined_rules)})")

print(f"Matched({len(total_matches)}):{total_matches}")
print("--- %s seconds ---" % (time.time() - start_time))