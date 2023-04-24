def solution(s):
    li = list()
    for w in s.split(" "):
        t = ""
        for i, c in enumerate(w):
            if i % 2:
                t += c.lower()
            else:
                t += c.upper()
        li.append(t)
    return " ".join(li)