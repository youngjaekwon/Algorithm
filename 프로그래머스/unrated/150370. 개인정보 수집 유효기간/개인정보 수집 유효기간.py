def solution(today, terms, privacies):
    today_y, today_m, today_d = tuple(map(int, today.split(".")))
    terms = dict([tuple(v.split()) for v in terms])
    answer = []
    for i, v in enumerate(privacies):
        day, term = tuple(v.split())
        y, m, d = tuple(map(int, day.split(".")))
        m += int(terms[term])
        tmp, m = divmod(m, 12)
        if m == 0:
            tmp -= 1
            m = 12
        y += tmp
        if ((y < today_y)
        or (y == today_y and m < today_m)
        or (y == today_y and m == today_m and d <= today_d)
        ):
            answer.append(i+1)
    return answer
