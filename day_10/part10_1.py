path = "input10.txt"

def input_lines(ff):
    with open(ff, encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
    x = 1
    cycle = 1
    values = {cycle:x}
    for l in lines:
        match l.split(" "):
            case ["noop"]:
                cycle += 1
            case ["addx", val]:
                cycle += 2
                x += int(val)
        values[cycle] = x
    return values


def part10_1(f):
    values = input_lines(f)
    answer = 0
    for st in [20,60,100,140,180,220]:
        if st in values:
            answer += st * values[st]
        elif st - 1 in values:
            answer += st * values[st - 1]
    return answer

print(part10_1(path))
