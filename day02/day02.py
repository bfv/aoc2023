colors = {"red": 12, "green": 13, "blue": 14 }       
a, b = 0, 0
lines = open(file="day02/input.txt", mode="r").read().split("\n")
for line in lines:
    gameOK, powers = True, {"red": 0, "green": 0, "blue": 0}
    id, sets = int(line.split(":")[0].replace("Game ", "")), line.split(":")[1].split(";")
    for set in sets:
        for c in set.split(","):
            count, color = int(c.split(" ")[1]), c.split(" ")[2]
            gameOK = gameOK and count <= colors[color]
            powers[color] = max(powers[color], count)
    if gameOK:
        a += id
    b += powers["red"] * powers["green"] * powers["blue"]

print(f"a: {a}, b: {b}")