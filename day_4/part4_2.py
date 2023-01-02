path = "input4.txt"

def section_list(ff):
    with open(ff, encoding="utf-8") as f:
        sec = f.read().split("\n\n")
    sections =  [list(map(str, s.strip().split("\n"))) for s in sec]
    return sections[0]

def day_4_p2(f):
    sections = section_list(f)
    answer = 0
    li = []
    for sec in sections:
        s= sec.split(",")
        a = s[0].split("-")
        b = s[1].split("-") 
        if int(a[0]) <= int(b[0]) <= int(a[1])  or int(b[0]) <= int(a[0]) <= int(b[1]):
            answer += 1
    return answer

print(day_4_p2(path))


