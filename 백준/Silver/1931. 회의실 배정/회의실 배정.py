N = int(input())
arr = sorted(
    [list(map(int, input().split())) for _ in range(N)], key=lambda l: (l[1], l[0])
)

first = arr.pop(0)
end = first[1]
answer = 1

for m in arr:
    m_start, m_end = m
    if m_start >= end:
        answer += 1
        end = m_end

print(answer)