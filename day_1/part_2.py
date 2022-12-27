path = "input.txt"

def calories_list(ff):
    with open(ff, encoding="utf-8") as f:
        elves = f.read().split("\n\n")
    return [list(map(int, cal.strip().split("\n"))) for cal in elves]

def day_1_p2(f):
    calories = calories_list(f)
    sum_calories = [sum(cal) for cal in calories]
    top3_calories = sorted(sum_calories)[-3:]
    return sum(top3_calories)

print(day_1_p2(path))