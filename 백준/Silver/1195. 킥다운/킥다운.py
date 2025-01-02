l1 = list(map(int, list(input())))
l2 = list(map(int, list(input())))

answers = []
ll1 = len(l1)
ll2 = len(l2)

l1 = l1 + [0] * (ll2 - 1)
l2 = [0] * (ll1 - 1) + l2
f = True

while True:
    ll = []
    for a, b in zip(l1, l2):
        if a + b > 3:
            break
        if a + b != 0:
            ll.append(a + b)
    else:
        answers.append(len(ll))

    if l1[-1] != 0 and l2[0] != 0:
        break

    if f:
        f = False
        if l1[-1] == 0:
            l1 = [0] + l1[:-1]
    else:
        f = True
        if l2[0] == 0:
            l2 = l2[1:] + [0]

print(min(answers) if answers else ll1 + ll2)