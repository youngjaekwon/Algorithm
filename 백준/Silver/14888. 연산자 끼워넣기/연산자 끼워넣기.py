N = int(input())
arr = list(map(int, input().split()))
ops = list(map(int, input().split()))
p, mi, mu, d = ops

len_arr = len(arr)
mx = float("-inf")
mn = float("inf")
max_arr = [0] * len_arr
min_arr = [float("inf")] * len_arr


def divide(a, b):
    quotient = abs(a) // abs(b)

    if (a < 0) != (b < 0):
        quotient = -quotient

    return quotient


def cal(li):
    tmp = 0
    prev = ""

    for v in li:
        if prev == "":
            tmp += v
        elif isinstance(prev, int):
            if isinstance(v, int):
                break
        elif isinstance(v, int):
            if prev == "+":
                tmp += v
            elif prev == "-":
                tmp -= v
            elif prev == "*":
                tmp *= v
            else:
                tmp = divide(tmp, v)
        prev = v

    return tmp


def solution(li, idx, op, p, mi, mu, d):
    global mx
    global mn
    li.insert(idx, op)
    res = cal(li)

    if idx < len_arr:
        if res < max_arr[idx] and res > min_arr[idx]:
            return
        if res > max_arr[idx]:
            max_arr[idx] = res
        if res > min_arr[idx]:
            min_arr[idx] = res

    if any([p, mi, mu, d]):
        if p:
            solution(list(li), idx + 2, "+", p - 1, mi, mu, d)
        if mi:
            solution(list(li), idx + 2, "-", p, mi - 1, mu, d)
        if mu:
            solution(list(li), idx + 2, "*", p, mi, mu - 1, d)
        if d:
            solution(list(li), idx + 2, "//", p, mi, mu, d - 1)
    else:
        if res > mx:
            mx = res
        if res < mn:
            mn = res


if p:
    solution(list(arr), 1, "+", p - 1, mi, mu, d)
if mi:
    solution(list(arr), 1, "-", p, mi - 1, mu, d)
if mu:
    solution(list(arr), 1, "*", p, mi, mu - 1, d)
if d:
    solution(list(arr), 1, "//", p, mi, mu, d - 1)

print(mx)
print(mn)
