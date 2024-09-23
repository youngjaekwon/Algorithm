def solution(topping):
    l1 = []
    l2 = []
    s1 = set()
    s2 = set()
    for i in range(len(topping)):
        s1.add(topping[i])
        s2.add(topping[-(i + 1)])
        l1.append(len(s1))
        l2.append(len(s2))
    l2 = l2[::-1]
    answer = 0
    for i in range(len(topping) - 1):
        if l1[i] == l2[i+1]:
            answer += 1
    return answer