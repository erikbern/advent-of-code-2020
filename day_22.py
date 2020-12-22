import collections
import sys

cards = [collections.deque(), collections.deque()]

deck = None
for line in open(sys.argv[1]):
    if line == 'Player 1:\n':
        deck = cards[0]
    elif line == 'Player 2:\n':
        deck = cards[1]
    elif line == '\n':
        continue
    else:
        deck.append(int(line.strip()))

original_cards = [c.copy() for c in cards]
while len(cards[0]) and len(cards[1]):
    card_1, card_2 = cards[0].popleft(), cards[1].popleft()
    assert card_1 != card_2
    winner = int(card_1 < card_2)
    cards[winner].append(max(card_1, card_2))
    cards[winner].append(min(card_1, card_2))

def score(deck):
    n = len(deck)
    return sum(card * (n-i) for i, card in enumerate(deck))
    
winning_deck = max(cards, key=lambda deck: len(deck))
print(score(winning_deck))

def play(cards, depth, max_score_delta):
    rounds = 0
    has_seen = set()
    while len(cards[0]) and len(cards[1]):
        rounds += 1
        k = (tuple(cards[0]), tuple(cards[1]))
        if k in has_seen:
            return 0, None
        has_seen.add(k)
        if depth > 0 and abs(score(cards[0]) - score(cards[1])) > max_score_delta:
            break

        round_cards = cards[0].popleft(), cards[1].popleft()
        if len(cards[0]) >= round_cards[0] and len(cards[1]) >= round_cards[1]:
            cards_0 = collections.deque(list(cards[0])[:round_cards[0]])
            cards_1 = collections.deque(list(cards[1])[:round_cards[1]])
            winner, _ = play([cards_0, cards_1], depth+1, max_score_delta)
        else:
            winner = int(round_cards[1] > round_cards[0])
        cards[winner].append(round_cards[winner])
        cards[winner].append(round_cards[1-winner])

    winner = int(score(cards[1]) > score(cards[0]))
    return winner, score(cards[winner])


for max_score_delta in range(0, 100000, 1000):
    cards = [c.copy() for c in original_cards]
    print('max score delta', max_score_delta, 'winner:', play(cards, 0, max_score_delta))
