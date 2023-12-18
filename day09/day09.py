

def main():

    a, b = 0, 0
    lines = open(file="day09/input.txt", mode="r").read().split("\n")

    for line in lines:
        list_a = [int(i) for i in line.split(' ')]
        a += calc_a(list_a)
        list_b = [int(i) for i in line.split(' ')]
        b += calc_b(list_b)

    print(f"day 8; a: {a}, b: {b}")

def calc_b(check_list: list[int]) -> int:
    
    lists: list(list(int)) = []
    while True:
        lists.append(check_list)
        if all(v==0 for v in check_list):
            break
        check_list = diffs(check_list)

    for i in reversed(range(len(lists))):
        if i > 1:
            last_n = lists[i-1][0]
            last_n_min1 = lists[i-2][0]
            lists[i-2].insert(0, last_n_min1 - last_n)    
    return lists[0][0] 

def calc_a(check_list: list[int]) -> int:
    
    lists: list(list(int)) = []
    while True:
        lists.append(check_list)
        if all(v==0 for v in check_list):
            break
        check_list = diffs(check_list)

    for i in reversed(range(len(lists))):
        if i > 1:
            last_n = lists[i-1][-1]
            last_n_min1 = lists[i-2][-1]
            lists[i-2].append(last_n + last_n_min1)    

    #print(lists)

    return lists[0][-1]

def diffs(check_list: list[int]) -> list[int]:
    diff_list: list(int) = []
    for i in range(len(check_list)-1):
        diff_list.append(check_list[i+1] - check_list[i])
    return diff_list

main()

