path = "input2.txt"

def guide_list(ff):
    with open(ff, encoding="utf-8") as f:
        elves = f.read().split("\n\n")
    return [list(map(str, cal.strip().split("\n"))) for cal in elves]

def score(opp, me):
    return (me-opp + 1) % 3 * 3 + me 

def day_2_p1(f):
    guides = guide_list(f)
    answer = 0
    for g in guides[0]:
        opp = ord(g[0]) - ord("A") +1
        me = ord(g[2]) - ord("X") +1
        answer += score(opp,me)
    return answer

print(day_2_p1(path))
