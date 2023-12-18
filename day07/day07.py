from typing import List


class Hand:
    
    def __init__(self, input: str):
        self.cards = input.split(' ')[0]
        self.bid = int(input.split(' ')[1])
        self.type_a = calc_type_a(self.cards)
        self.sort_str_a = str(self.type_a) + get_sort_str(self.cards) 
        self.type_b = calc_type_b(self.cards)
        self.sort_str_b = str(self.type_b) + get_sort_str_b(self.cards) 

        #self.eval_str = calc_optimum(self.cards)

def main():

    a, b = 0, 0
    lines = open(file="day07/input.txt", mode="r").read().split("\n")

    hands: List[Hand] = []
    for line in lines:
        hands.append(Hand(line))

    ordered_hands_a = sorted(hands, key=lambda card: card.sort_str_a)
    
    for rank, hand in enumerate(ordered_hands_a):
        #print(f"{hand.cards}, type: {hand.type_a}, rank: {rank+1}")
        a += hand.bid * (rank+1)

    ordered_hands_b = sorted(hands, key=lambda card: card.sort_str_b)
    
    for rank_b, hand in enumerate(ordered_hands_b):
        #print(f"{hand.cards}, type: {hand.type_b}, sort: {hand.sort_str_b}, rank: {rank_b+1}")
        b += hand.bid * (rank_b+1)

    print(f"day 7; a: {a}, b: {b}") 

def calc_type_b(card_str) -> int:
    card_count = dict(zip(card_types, [0] * len(card_types)))
    cards = list(card_str)
    
    for card in cards:
        card_count[card] += 1

    card_counts = sorted(card_count.items(), key=lambda v: v[1], reverse=True)
    card_counts = list(map(lambda x: x[1], card_counts))

    card0 = card_counts[0]
    card1 = card_counts[1]
    if card_count['J'] >= card0:
        card0 = card_counts[1]
        card1 = card_counts[2]
    
    card0 += card_count['J']

    return calc_type(card0, card1)

def calc_type_a(card_str: str) -> int:
    card_count = dict(zip(card_types, [0] * len(card_types)))
    cards = list(card_str)
    
    for card in cards:
        card_count[card] += 1

    card_counts = sorted(card_count.items(), key=lambda v: v[1], reverse=True)
    card_counts = list(map(lambda x: x[1], card_counts))
    
    return calc_type(card_counts[0], card_counts[1])

def calc_type(card0: int, card1: int) -> int:
    if card0 == 10:  # 5 J's
        card0 = 5
    type = 1
    if card0 == 1: type = 2
    elif card0 == 2 and card1 ==2: type = 4
    elif card0 == 2: type = 3
    elif card0 == 3 and card1 ==2: type = 6
    elif card0 == 3: type = 5
    elif card0 == 4: type = 7
    elif card0 == 5: type = 8

    return type

def get_sort_str(cards: str) -> str:
    cs = list(cards)
    result = ""
    for c in cs:
        i = card_types.index(c)
        result += sort_chars[i]
    return result

def get_sort_str_b(cards: str) -> str:
    cs = list(cards)
    result = ""
    for c in cs:
        i = card_types2.index(c)
        result += sort_chars[i]

    return result

def calc_optimum(cards: str) -> str:
    pass

card_types = list("23456789TJQKA")
card_types2 = list("J23456789TQKA")
sort_chars = list("ABCDEFGHabcde")

main()
      