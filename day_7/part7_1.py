from collections import defaultdict

path = "input7.txt"

def commands_list(ff):
    cwd, sizes = "", defaultdict(int)
    with open(ff, encoding="utf-8") as f:
        for line in f:
            match line.split():
                case ("$", "cd", "/"):
                    cwd = ""
                case ("$", "cd", ".."):
                    idx = cwd.rindex("/") if "/" in cwd else 0
                    cwd = cwd[:idx]
                case ("$", "cd", path):
                    cwd = f"{cwd}/{path}" if cwd else path
                case (size, *_):
                    try:
                        size = int(size)
                    except ValueError:
                        continue
                    path = cwd
                    while 1 :
                        sizes[path] += size
                        if not path:
                            break
                        path = path[: path.rindex("/") if "/" in path else 0]
        return sizes

def day_7_p1(path):
    commands = commands_list(path)
    answer = 0
    for size in commands.values():
        if size <= 100000:
            answer += size
    return answer

print(day_7_p1(path))


