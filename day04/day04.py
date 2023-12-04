
from typing import List

class Card:
    nr: int
    winning: List[int] = []
    numbers: List[int] = []
    matching_count: int
    
    def __init__(self, card: str):
        self.nr = int(card.split(':')[0].split()[1])  
        self.winning = list(map(int, card.split(':')[1].split('|')[0].split()))
        self.numbers = list(map(int, card.split(':')[1].split('|')[1].split()))
        self.matching_count = len([value for value in self.numbers if value in self.winning])
        self.a = int(2**(self.matching_count-1))

def process_copies(card: Card, cards: List[Card]) -> int:
    b = 1
    for i in range(card.nr + 1, card.nr + card.matching_count + 1):
        if i <= len(cards):
            b += process_copies(cards[i-1], cards)
    return b

def main():
    lines = open(file="day04/input.txt", mode='r').read().split('\n')
    
    a, b = 0, 0
    cards: List[Card] = []

    for line in lines:
        card = Card(line)
        cards.append(card)
        a += card.a

    for card in cards:
        b += process_copies(card, cards)

    print(f"a: {a}, b: {b}")

main()