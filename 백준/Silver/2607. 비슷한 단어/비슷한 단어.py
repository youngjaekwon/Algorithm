N = int(input())
words = [list(input()) for _ in range(N)]


def compare(a, b):
    diff = []
    for c in a:
        if c in b:
            b.remove(c)
        else:
            diff.append(c)

    if len(diff) > 1 or len(b) > 1:
        return 0

    return 1


answer = 0
target = words[0]

for word in words[1:]:
    answer += compare(target, word)

print(answer)
