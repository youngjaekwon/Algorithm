import sys

input = sys.stdin.readline

N = int(input())
arr = sorted(
    [list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0])
)

if arr[0][0] > arr[0][1]:
    print(-1)
else:
    answer = arr[0][1] - arr[0][0]
    time = arr[0][1]

    for task in arr[1:]:
        end = time + task[0]
        gap = end - task[1]
        if gap > 0:
            if gap > answer:
                answer = -1
                break
            answer -= gap
            time = end - gap
        else:
            time = end

    print(answer)