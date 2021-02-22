from collections import deque, defaultdict

#file1= open('aoc221_test_input_p1.txt', 'r')
#file2= open('aoc221_test_input_p2.txt', 'r')
file1= open('aoc22_1_input_p1.txt', 'r')
file2= open('aoc22_1_input_p2.txt', 'r')

#Decks are stacks
p1_deck = deque()
p2_deck = deque()
#loop tracker
deck_played = defaultdict(int)

for line in file1.readlines():
    p1_deck.appendleft(int(line))

for line in file2.readlines():
    p2_deck.appendleft(int(line))

def deck_fingerprint(input_deck,player):
    return_fingerprint = player
    d = input_deck.copy()
    while len(d) >0:
        return_fingerprint += ':' + str(d.popleft())
    return return_fingerprint


print(p1_deck)
print(p2_deck)

while (len(p1_deck) != 0) and (len(p2_deck) != 0):
    #play hand
    p1_card = p1_deck.pop()
    p2_card = p2_deck.pop()
    print(f"P1:{p1_card} vs P2:{p2_card}")
    if p1_card > p2_card:
        print(f"P1 wins")
        p1_deck.appendleft(p1_card)
        p1_deck.appendleft(p2_card)
    else:
        print(f"P2 wins")
        p2_deck.appendleft(p2_card)
        p2_deck.appendleft(p1_card)
    print(f"Player 1:{p1_deck}")
    print(f"------")
    print(f"Player 2:{p2_deck}")
    print(f"######")


if len(p1_deck) > 0:
    winner_stack = p1_deck
else:
    winner_stack = p2_deck

#print(deck_fingerprint(winner_stack,'p2'))

ans = 0
counter = 1
for each in winner_stack:
    ans += each * counter
    counter +=1
print(f"Ans part1:{ans}")