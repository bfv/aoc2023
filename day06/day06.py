
def main():

    a, b = 1, 0
    lines = open(file="day06/input.txt", mode="r").read().split("\n")
    
    times = list(map(int, lines[0].split()[1:]))
    records = list(map(int, lines[1].split()[1:]))

    for i, record in enumerate(records):
        t_tot = times[i]
        a *= calc_possibilities(t_tot, record)

    t_tot, record = int("".join(lines[0].split()[1:])), int("".join(lines[1].split()[1:]))
    b = calc_possibilities(t_tot, record)

    print(f"day 6; a: {a}, b: {b}") 

def calc_possibilities(t_tot, record) -> int:
    wins = 0
    for t in range(0, t_tot):
        if -t**2 + t*t_tot > record:
            wins += 1
    return wins

main()