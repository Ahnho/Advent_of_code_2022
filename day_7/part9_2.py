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

def part9_2(f):
    dir_move = roinput(f)
    knots = [(0,0) for i in range(10)]
    visited_tail = {knots[-1]}
    for d,v in dir_move:
        for i in range(v):
            dx,dy = to_move(d)
            knots[0] = (knots[0][0] + dx, knots[0][1] +dy )
            for k in range(1,len(knots)):
                knots[k] = adjust_tail(knots[k], knots[k - 1])
            visited_tail.add(knots[-1])
    return len(visited_tail)

print(part9_2(path))