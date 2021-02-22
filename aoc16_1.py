from collections import defaultdict

#input = [ '0','3','6']
#lastplayed = 6
#input = ['1','3','2']
#lastplayed = 2
#input = [ '3','1','2']
#lastplayed = 2

rules_file = open('aoc16_rules_input.txt', 'r')
your_ticket_file = open('aoc16_your_ticket_input.txt','r')
near_tickets_file = open('aoc16_near_tickets_input.txt','r')

def find_min_max(input_list1,input_list2):
    return_list = [0,0,0,0]
    return_list[0] = input_list2[0] if input_list2[0] < input_list1[0] else input_list1[0]
    return_list[1] = input_list2[1] if input_list2[1] > input_list1[1] else input_list1[1]
    return_list[2] = input_list2[2] if input_list2[2] < input_list1[2] else input_list1[2]
    return_list[3] = input_list2[3] if input_list2[3] > input_list1[3] else input_list1[3]
    return return_list

#print(find_min_max([32,842,854,967],[26,252,260,955]))

def scan_min_max(input_int,input_list1):
    input_ok = True
    if (input_int < input_list1[0]) and (input_int < input_list1[2]):
        input_ok = False
    if (input_int > input_list1[1]) and (input_int > input_list1[3]):
        input_ok = False
    if input_ok:
        return 0
    else:
        return input_int

def check_min_max(input_int,input_list1):
    input_ok = False
    if (input_int >= input_list1[0]) and (input_int <= input_list1[1]) or (input_int >= input_list1[2]) and (input_int <= input_list1[3]):
        input_ok = True
    if input_ok:
        return 0
    else:
        return input_int




rules_d = defaultdict(list)
rules_list = []
min_max_rule = []
for line in rules_file.readlines():
    field_name = line.strip().split(':')[0].strip()
    rules = line.strip().split(':')[1].strip().split('or')
    for s in rules:
        rules_list += [int(v) for v in s.strip().split('-')]
    rules_d[field_name] = rules_list
    if min_max_rule == []:
        min_max_rule = rules_list
    else:
        min_max_rule = find_min_max(min_max_rule,rules_list)
    rules_list = []

#print(rules_d)
#print(min_max_rule)

near_tickets_d = defaultdict(list)
near_tickets_list = []
ticket_counter = 1
for line in near_tickets_file.readlines():
    near_tickets_list = [int(v) for v in line.split(',')]
    near_tickets_d[str(ticket_counter)] = near_tickets_list
    near_tickets_list = []
    ticket_counter += 1
#print(near_tickets_d)

ans=0
remove_list = []
for k,v in near_tickets_d.items():
  #print(f"Ticket:{k} - {v} ",end='')
  for ticket_number in v:
      scan_result = scan_min_max(ticket_number,min_max_rule)
      if scan_result != 0:
          #print(f"failed:{scan_result}",end='')
          remove_list.append(k)
      ans += scan_result
  #print('')


for i in remove_list:
    near_tickets_d.pop(i)


#print(f"Svar:{ans}")
#print(remove_list)
#print(near_tickets_d)

rules_columns = defaultdict(list)

for rk, rv in rules_d.items():
    print(f"Rule Start:{rk}")
    length = len(near_tickets_d['1'])
    for i in range(length):
        check_result = 0
        for tk in near_tickets_d:
            input_value = near_tickets_d[tk][i]
            #print(f"Rule:{rk} checked vs column:{i} with value:{input_value}")
            check_result += check_min_max(input_value,rv)
        if check_result != 0:
            print(f"Fail rule:{rk} checked vs column:{i} with value:{input_value}")
        else:
            rules_columns[rk].append(i)

for k,v in rules_columns.items():
    v = list(set(v))
    print(f"key:{k} value:{v}")

#print(rules_columns)
rules_sorted = sorted(rules_columns.items(), key= lambda x: len(x[1]), reverse=False)
for j in rules_sorted:
    print(j)