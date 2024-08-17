X = int(input())

num = 1
count = 1

while X > num:
    count += 1
    num += count

start = num - count + 1

if count % 2:
    answer = (count, 1)

    for i in range(start + 1, X + 1):
        answer = (answer[0] - 1, answer[1] + 1)
else:
    answer = (1, count)

    for i in range(start + 1, X + 1):
        answer = (answer[0] + 1, answer[1] - 1)


print(f"{answer[0]}/{answer[1]}")