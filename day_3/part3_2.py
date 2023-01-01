path = "input3.txt"

def items_list(ff):
    with open(ff, encoding="utf-8") as f:
        items = f.read().split("\n\n")
    item_list =  [list(map(str, item.strip().split("\n"))) for item in items]

    lt = []
    for index in range(0,len(item_list[0]),3):
        li = set(item_list[0][index]) & set(item_list[0][index+1]) & set(item_list[0][index+2])
        lt.append(li.pop())

    return lt

def day_3_p2(f):
    items = items_list(f)
    answer = 0
    li = []
    for it in items:
        answer += ord(it) - 96 if it.islower() else ord(it) - 38
    return answer

print(day_3_p2(path))


