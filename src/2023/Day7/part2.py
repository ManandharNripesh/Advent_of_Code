from ...common.input_reader import read_input
from functools import cmp_to_key

input_lines = read_input("src/2023/Day7/test.txt")

hands = []
bids  = []

# get hands
for i, input_line in enumerate(input_lines):
    hand, bid = input_line.split()
    hands.append(hand)
    bids.append(int(bid))

FIVE_OF_A_KIND  = 0
FOUR_OF_A_KIND  = 1
FULL_HOUSE      = 2
THREE_OF_A_KIND = 3
TWO_PAIR        = 4
ONE_PAIR        = 5
HIGH_CARD       = 6

hands_typed = []
for i in range(HIGH_CARD + 1):
    hands_typed.append(list())

# sort hands into types
for i in range(len(hands)):
    hand = hands[i]
    bid = bids[i]

    possible_cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    cards = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "J": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0
    }

    for card in hand:
        cards[card] += 1
    
    counts = []

    for index in possible_cards:
        if cards[index] > 0 and index != "J":
            counts.append(cards[index])

    pairs = 0
    triples = 0
    hand_type = HIGH_CARD

    for count in counts:
        if count == 5:
            hand_type = FIVE_OF_A_KIND
            break
        elif count == 4:
            hand_type = FOUR_OF_A_KIND
            break
        elif count == 3:
            triples += 1
            if pairs == 1:
                hand_type = FULL_HOUSE
                break
            else:
                hand_type = THREE_OF_A_KIND
        elif count == 2:
            pairs += 1
            if triples == 1:
                hand_type = FULL_HOUSE
                break
            elif pairs == 2:
                hand_type = TWO_PAIR
            else:
                hand_type = ONE_PAIR
    
    if hand_type == FOUR_OF_A_KIND:
        if cards["J"] > 0:
            hand_type = FIVE_OF_A_KIND
    elif hand_type == THREE_OF_A_KIND:
        if cards["J"] == 1:
            hand_type = FOUR_OF_A_KIND
        elif cards["J"] == 2:
            hand_type = FIVE_OF_A_KIND
    elif hand_type == TWO_PAIR:
        if cards["J"] > 0:
            hand_type = FULL_HOUSE
    elif hand_type == ONE_PAIR:
        if cards["J"] == 1:
            hand_type = THREE_OF_A_KIND
        elif cards["J"] == 2:
            hand_type = FOUR_OF_A_KIND
        elif cards["J"] == 3:
            hand_type = FIVE_OF_A_KIND
    elif hand_type == HIGH_CARD:
        if cards["J"] == 1:
            hand_type = ONE_PAIR
        elif cards["J"] == 2:
            hand_type = THREE_OF_A_KIND
        elif cards["J"] == 3:
            hand_type = FOUR_OF_A_KIND
        elif cards["J"] == 4:
            hand_type = FIVE_OF_A_KIND
        elif cards["J"] == 5:
            hand_type = FIVE_OF_A_KIND

    hands_typed[hand_type].append((hand, bid))


card_to_value = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

def compare_hands(hand_bid_a, hand_bid_b):
    hand_a = hand_bid_a[0]
    hand_b = hand_bid_b[0]
    for i in range(len(hand_a)):
        value_a = card_to_value[hand_a[i]]
        value_b = card_to_value[hand_b[i]]

        if value_a > value_b:
            return 1
        elif value_a < value_b:
            return -1
    return 0

# sort within each hand type by each card
for hand_type in range(len(hands_typed)):
    hands_typed[hand_type].sort(key=cmp_to_key(compare_hands), reverse=True)

rank = len(hands)
winnings = 0

# calculate winnings
for hand_type in range(len(hands_typed)):
    for hand_bid in hands_typed[hand_type]:
        hand, bid = hand_bid
        winnings += rank * bid
        rank -= 1

print(winnings)