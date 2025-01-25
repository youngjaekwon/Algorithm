S = input()
T = input()


def func1(t):
    return t[:-1]


def func2(t):
    return "".join(reversed(t[:-1]))


answer = 0

while True:
    if T[-1] == "A":
        T = func1(T)
    else:
        T = func2(T)

    if T == S:
        answer = 1
        break
    elif len(T) <= len(S):
        break

print(answer)
