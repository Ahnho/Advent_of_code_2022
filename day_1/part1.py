path = "input.txt"

def calories_list(ff):
    with open(ff, encoding="utf-8") as f:
        elves = f.read().split("\n\n")
    return [list(map(int, cal.strip().split("\n"))) for cal in elves]

def day_1_p1(f):
    calories = calories_list(f)
    answer = 0
    for cal in calories:
        if answer <= sum(cal): answer = sum(cal)
    return answer

print(day_1_p1(path))
