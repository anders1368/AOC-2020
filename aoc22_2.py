from collections import deque, defaultdict

#file1 = open('aoc221_test_input_p1.txt', 'r')
#file2 = open('aoc221_test_input_p2.txt', 'r')
file1= open('aoc22_1_input_p1.txt', 'r')
file2= open('aoc22_1_input_p2.txt', 'r')

# Decks are stacks
p1_deck = deque()
p2_deck = deque()
# loop tracker
deck_played = defaultdict(int)
#global counter:
game_counter = 1

for line in file1.readlines():
    p1_deck.appendleft(int(line))

for line in file2.readlines():
    p2_deck.appendleft(int(line))


def deck_fingerprint(input_deck, player):
    return_fingerprint = player
    d = input_deck.copy()
    while len(d) > 0:
        return_fingerprint += ':' + str(d.popleft())
    return return_fingerprint


def sub_game(p1_c, p1_d, p2_c, p2_d):
    for i in range(len(p1_d) - p1_c): p1_d.popleft()
    for i in range(len(p2_d) - p2_c): p2_d.popleft()
    round = 1
    global game_counter
    game = game_counter
    while (len(p1_d) != 0) and (len(p2_d) != 0):
        print(f"Round:({round}) (Game:{game})")
        print_deck(p1_d, p2_d)
        # Check if either hand has been played before
        p1_number_of_times = deck_played[deck_fingerprint(p1_d, str(game) + '-p1')]
        p2_number_of_times = deck_played[deck_fingerprint(p2_d, str(game) + '-p2')]

        if p1_number_of_times == 1:
            print(f"P1's deck has been played BEFORE!:{p1_d}")
            return 'p1'
        else:
            deck_played[deck_fingerprint(p1_d, str(game) + '-p1')] = 1

        if p2_number_of_times == 1:
            print(f"P2's deck has been played BEFORE!:{p2_d}")
            return 'p1'
        else:
            deck_played[deck_fingerprint(p2_d, str(game) + '-p2')] = 1
        # play hand
        p1_card = p1_d.pop()
        p2_card = p2_d.pop()
        print(f"P1 plays:{p1_card}")
        print(f"P2 plays:{p2_card}")
        # Check if it is time for recursive
        if (p1_card <= len(p1_d)) and (p2_card <= len(p2_d)):
            print(f"Playing a sub-game...")
            game_counter += 1
            winner = sub_game(p1_card, p1_d.copy(), p2_card, p2_d.copy())
            if winner == 'p1':
                p1_d.appendleft(p1_card)
                p1_d.appendleft(p2_card)
            else:
                p2_d.appendleft(p2_card)
                p2_d.appendleft(p1_card)
        else:
            if p1_card > p2_card:
                print(f"P1 WINS! Round:{round} Game:{game} ")
                print('')
                p1_d.appendleft(p1_card)
                p1_d.appendleft(p2_card)
            else:
                print(f"P2 WINS! Round:{round} Game:{game}")
                print('')
                p2_d.appendleft(p2_card)
                p2_d.appendleft(p1_card)
        round += 1
    print(f"Done. Back to up:{game - 1}")
    print('')
    if len(p1_d) > 0:
        return 'p1'
    else:
        return 'p2'


def print_deck(input_p1_deck, input_p2_deck):
    # printable copies:
    copy_p1_deck = input_p1_deck.copy()
    copy_p2_deck = input_p2_deck.copy()
    copy_p1_deck.reverse()
    copy_p2_deck.reverse()
    print(f"Player 1:{copy_p1_deck}")
    print(f"Player 2:{copy_p2_deck}")



result_string = sub_game(100, p1_deck, 100, p2_deck)

print(f"Post-game results")
print_deck(p1_deck, p2_deck)

if len(p1_deck) > 0:
    winner_stack = p1_deck
else:
    winner_stack = p2_deck

ans = 0
counter = 1
for each in winner_stack:
    ans += each * counter
    counter += 1
print(f"Ans part2:{ans}")
