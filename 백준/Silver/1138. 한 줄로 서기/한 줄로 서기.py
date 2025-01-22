N = int(input())
l = list(enumerate(map(int, input().split()), 1))
l.sort(reverse=True)

answer = [l[0][0]]

for i, x in l[1:]:
    bigger = 0

    for j, y in enumerate(answer):
        if bigger == x:
            answer.insert(j, i)
            break
        if y > i:
            bigger += 1
    else:
        answer.append(i)


print(" ".join([str(n) for n in answer]))