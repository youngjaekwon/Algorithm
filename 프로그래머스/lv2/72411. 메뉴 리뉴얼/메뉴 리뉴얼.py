import itertools

def solution(orders, course):
    orders = [set(order) for order in orders]
    answer = list()
    total = dict([(i, dict()) for i in course])
    for i, order in enumerate(orders):
        for order2 in orders[i+1:]:
            inter = order & order2
            inter = "".join(sorted(inter))
            for i in course:
                if i <= len(inter):
                    for menu in itertools.combinations(inter, i):
                        menu = "".join(menu)
                        if menu in total[i]:
                            total[i][menu] += 1
                        else:
                            total[i][menu] = 1

    for course in total.values():
        l = sorted(course.items(), key=lambda x: x[1])
        if l:
            mx = max([v for k, v in l])
            answer.extend([k for k, v in l if v == mx])

    return sorted(answer)