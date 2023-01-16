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

def draw(dr):
    for y in range(6):
        for x in range(40):
            if x + y * 40 in dr:
                print("#", end ="")
            else:
                print(".", end ="")
        print()

def part10_2(f):
    values = input_lines(f)
    dw = [ ]
    for p in range(240):
        cy = p + 1
        if cy in values : 
            val = values[cy]
        elif cy - 1 in values:
            val =  values[cy-1]
        if -1 <= p % 40 - val <= 1:
            dw.append(p)
    draw(dw)

print(part10_2(path))