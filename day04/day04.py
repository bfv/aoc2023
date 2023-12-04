
from typing import List

class Card:
    nr: int
    winning: List[int] = []
    numbers: List[int] = []
    matching_count: int = 0
    
    def __init__(self):
        self.nr = 0

    def __init__(self, card: str):
        self.nr = int(card.split(':')[0].split()[1])  
        self.winning = list(map(int, card.split(':')[1].split('|')[0].split()))
        self.numbers = list(map(int, card.split(':')[1].split('|')[1].split()))
        self.matching_count = len([value for value in self.numbers if value in self.winning])
        self.a = int(2**(self.matching_count-1))
        
        return 

cards: List[Card] = []

def process_copies(card: Card):
    global b
    for i in range(card.nr + 1, card.nr + card.matching_count + 1):
        if i <= len(cards):
            b += 1
            process_copies(cards[i-1])

def main():
    lines = open(file="day04/input.txt", mode='r').read().split('\n')
    
    a = 0
    for line in lines:
        card = Card(line)
        cards.append(card)
        a += card.a

    for card in cards:
        process_copies(card)

    global b
    b += len(cards)

    print(f"a: {a}, b: {b}")

b = 0
main()