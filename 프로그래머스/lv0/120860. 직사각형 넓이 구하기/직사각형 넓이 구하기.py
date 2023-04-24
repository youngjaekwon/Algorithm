def solution(dots):
    x = list()
    y = list()
    for dot in dots:
        x.append(dot[0])
        y.append(dot[1])
    
    dot1 = (max(x), max(y))
    dot2 = (min(x), min(y))
    
    return (dot1[0] - dot2[0]) * (dot1[1] - dot2[1])