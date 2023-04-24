def solution(polynomial):
    xt = 0
    t = 0
    for x in polynomial.split():
        if "x" in x:
            x = x.replace("x", "")
            xt += int(x) if x else 1
        elif x == "+":
            continue
        else:
            t += int(x)
    if xt > 1 and t:
        return f"{xt}x + {t}"
    elif xt and t:
        return f"x + {t}"
    elif xt > 1:
        return f"{xt}x"
    elif xt:
        return f"x"
    else:
        return f"{t}"