N = int(input())
words = [input() for _ in range(N)]

answer = list(words[0])

for word in words[1:]:
    for i, c in enumerate(word):
        if c != answer[i]:
            answer[i] = "?"

print("".join(answer))
