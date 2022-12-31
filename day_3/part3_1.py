path = "input3.txt"

def items_list(ff):
    with open(ff, encoding="utf-8") as f:
        items = f.read().split("\n\n")
    item_list =  [list(map(str, item.strip().split("\n"))) for item in items]

    lt = []
    for item in item_list[0]:
        item_size = len(item) // 2 
        li = set(item[item_size:]) & set(item[:item_size])
        lt.append(li.pop())

    return lt

def day_3_p1(f):
    items = items_list(f)
    answer = 0
    li = []
    for it in items:
        answer += ord(it) - 96 if it.islower() else ord(it) - 38
    return answer

print(day_3_p1(path))


