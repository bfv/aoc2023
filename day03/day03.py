from dataclasses import dataclass
from typing import List

@dataclass
class Number:
    row: int
    col: int
    value: int

    def __len__(self):
        return len(str(self.value))

numbers: List[Number] = []
board = []

def main():

    lines = open(file="day03/input.txt", mode="r").read().split("\n")

    emptyRow = ["."] * (len(lines[0]) + 2)
    board.append(emptyRow)
    for row, line in enumerate(lines):
        chars = [*line]
        board.append(['.'] + chars + ['.'])
        getNumberFromLine(chars, row+1)
    board.append(emptyRow)

    a, b = 0, 0
    for n in numbers:
        if hasAdjacentChar(n):
            a += n.value
    
    b = iterateBoard()

    print(f"a: {a}, b: {b}")

def iterateBoard() -> int:
    b = 0
    for r, _ in enumerate(board):
        for c, _ in enumerate(board):
            ch = board[r][c]
            if ch == "*":
                b += calcAdjacent(r, c)
    return b

def calcAdjacent(row: int, col: int) -> int:
    res, found = 1, 0
    for n in numbers:
        if n.row >= row-1 and n.row <= row+1:
            rightCol = n.col + len(n) - 1
            if not(rightCol < col-1 or n.col > col+1):
                found += 1
                res *= n.value
    
    if res == 1 or found < 2:
        res = 0
    
    return res

def hasAdjacentChar(n: Number) -> bool:
    for row in range(n.row-1, n.row+2):
        for col in range(n.col-1, n.col+len(n)+1):
            c = board[row][col]
            if not c.isdigit() and not c == ".":
                return True
    return False

def getNumberFromLine(line: [], row: int):
    start = -1
    n = ""
    for col, c in enumerate(line):
        if c.isdigit():
            n += c
            if start < 0:
                start = col+1
        else:
            if start > 0:
                numbers.append(Number(row=row, col=(col+1-len(n)), value=int(n)))
                start, n = -1, ""
    if start > 0:
        numbers.append(Number(row=row, col=(col+1-len(n)), value=int(n)))

main()