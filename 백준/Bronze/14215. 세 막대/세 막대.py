li = list(map(int, input().split()))
one = max(li)
others = sum(li) - max(li)
if one >= others:
    one = others - 1
print(one + others)