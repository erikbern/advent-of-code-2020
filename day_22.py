import sys

cards = [[], []]

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

original_cards = cards = (tuple(cards[0]), tuple(cards[1]))

while len(cards[0]) and len(cards[1]):
    card_1, card_2 = cards[0][0], cards[1][0]
    winner = int(card_1 < card_2)
    new_cards = (max(card_1, card_2), min(card_1, card_2))
    cards = (cards[0][1:] + (new_cards if card_1 > card_2 else tuple()),
             cards[1][1:] + (new_cards if card_1 < card_2 else tuple()))

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
        if cards in has_seen:
            return 0, None
        has_seen.add(cards)
        if depth > 0 and abs(score(cards[0]) - score(cards[1])) > max_score_delta:
            break

        round_cards = cards[0][0], cards[1][0]
        if len(cards[0]) >= round_cards[0]+1 and len(cards[1]) >= round_cards[1]+1:
            cards_0 = cards[0][1:round_cards[0]+1]
            cards_1 = cards[1][1:round_cards[1]+1]
            winner, _ = play((cards_0, cards_1), depth+1, max_score_delta)
        else:
            winner = int(round_cards[1] > round_cards[0])
        new_cards = (round_cards[winner], round_cards[1-winner])
        cards = (cards[0][1:] + (new_cards if winner == 0 else tuple()),
                 cards[1][1:] + (new_cards if winner == 1 else tuple()))

    winner = int(score(cards[1]) > score(cards[0]))
    return winner, score(cards[winner])


for max_score_delta in range(0, 100000, 1000):
    print('max score delta', max_score_delta, 'winner:', play(original_cards, 0, max_score_delta))
