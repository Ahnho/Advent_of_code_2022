path = "input5.txt"

def stack_command(ff):
    with open(ff, encoding="utf-8") as f:
        stacklis, commands = f.read().split("\n\n")
    stack_list = stacklis.split("\n")
    lenst = stack_list[-1].split()
    stack_list.pop()
    
    stacks = []
    num = 1
    for i in lenst:
        st = []
        for s in stack_list:
            if s[num] != " ":
                st.append(s[num])
        num += 4
        stacks.append(st[::-1])

    instructions = []
    for command in commands.strip().split("\n"):
        _, n, _, to, _, dest = command.split()
        instructions.append(list(map(int, [n, to, dest])))
    return stacks, instructions

def day_5_p2(f):
    stacks, instructions = stack_command(f)
    answer = ""
    for ins in instructions:
        n = len(stacks[ins[1]-1]) - int(ins[0]) 
        stacks[ins[2]-1].extend(stacks[ins[1]-1][n:])
        del stacks[ins[1]-1][n:]

    for m in stacks:
        if len(m) > 0:
            answer += m[-1]
    return answer

print(day_5_p2(path))


# LJSVLTWQM
