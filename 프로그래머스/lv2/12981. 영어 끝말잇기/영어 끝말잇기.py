def solution(n, words):
    players = [list() for i in range(n)]
    stack = list()

    for i, word in enumerate(words):
        num = (i + 1) % n
        num = n if num == 0 else num
        if stack and (word in stack or word[0] != stack[-1][-1]):
            return [num, len(players[num - 1]) + 1]
        else:
            players[num - 1].append(word)
            stack.append(word)

    return [0, 0]