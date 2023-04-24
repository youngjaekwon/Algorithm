def solution(str1, str2):
    answer = 0
    l1 = []
    l2 = []
    for i, x in enumerate(str1):
        y = str1[i:i+2].lower()
        if y.isalpha() and len(y) > 1:
            l1.append(y)
    for i, x in enumerate(str2):
        y = str2[i:i+2].lower()
        if y.isalpha() and len(y) > 1:
            l2.append(y)
    inter = []
    union = []
    for x in set(l1 + l2):
        y = min(l1.count(x), l2.count(x))
        z = max(l1.count(x), l2.count(x))
        if y:
            inter.extend([x] * y)
        union.extend([x] * z)
    return int((len(inter) / len(union)) * 65536) if l1 + l2 else 65536