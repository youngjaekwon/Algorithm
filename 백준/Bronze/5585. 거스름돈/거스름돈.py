N = int(input())
l = [500, 100, 50, 10, 5, 1]
target = 1000 - N
answer = 0

for x in l:
    target, c = target % x, target // x
    answer += c

print(answer)