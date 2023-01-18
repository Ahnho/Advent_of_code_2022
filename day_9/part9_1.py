path = "input9.txt"

def roinput(ff):
    with open(ff,"r" ,encoding="utf8") as f : 
        return [(d,int(v)) for (d,v) in [tuple(line.strip().split()) for line  in f.readlines()]]

def to_move(d):
    move = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0),
    }
    return move[d]

def adjust_tail(head, tail) :
    match head[0] - tail[0], head[1] - tail[1]:
        case _ as dx, _ as dy if abs(dx) <= 1 and abs(dy) <= 1: return (tail[0], tail[1])
        case 0, _ as dy: return (tail[0], tail[1] + dy // abs(dy))
        case _ as dx, 0: return (tail[0] + dx // abs(dx), tail[1])
        case _ as dx, _ as dy: return (tail[0] + dx // abs(dx), tail[1] + dy // abs(dy))
    return (0, 0)

def part_1(f):
    dir_move = roinput(f)
    head = (0,0)
    tail = (0,0)
    visited_tail = {tail}
    for d,v in dir_move:
        for i in range(v):
            dx,dy = to_move(d)
            head = (head[0] + dx ,head[1]+dy)
            tail = adjust_tail(head,tail)
            visited_tail.add(tail)
    return len(visited_tail)

print(part_1(path))
