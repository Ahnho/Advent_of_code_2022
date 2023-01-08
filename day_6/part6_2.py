path = "input6.txt"

def marker_list(ff):
    with open(ff, encoding="utf-8") as f:
        stream = f.read().strip("")
    return stream

def day_6_p1(path):
    stream = marker_list(path)
    print(stream)
    for s in range(len(stream)):
        if len(stream[s : s + 14]) == len(set(stream[s : s + 14])):
            return s + 14
    return 0

print(day_6_p1(path))
