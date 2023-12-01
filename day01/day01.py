import re

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def main():

    a, b = 0, 0

    lines = open(file="day01/input.txt", mode="r").read().split("\n")
    
    for line in lines:
        a += int(re.search(r"\d", line).group() + re.search(r"\d", line [::-1]).group())
        b += int(first(line) + last(line))

    print(f"a: {a}, b: {b}") 

def first(s: str) -> str:
    
    idx = len(s) + 1
    digit = ''

    for d in digits:
        try:
            i = s.index(d)
            if i < idx:
                idx = i
                digit = d
        except:
            pass

    idx = digits.index(digit)
    s1 = str(digits[idx % 10])
    return s1

def last(s: str) -> str:
    idx = -1
    digit = ''

    for d in digits:
        try:
            i = s.rindex(d)
            if i > idx:
                idx = i
                digit = d
        except:
            pass

    idx = digits.index(digit)
    s1 = str(digits[idx % 10])
    return s1

main()