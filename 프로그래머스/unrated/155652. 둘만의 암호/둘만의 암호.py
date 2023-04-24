alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def solution(s, skip, index):
    for c in skip:
        alphabets.remove(c)
    index %= len(alphabets)
    answer = "".join([alphabets[(alphabets.index(c) + index) % len(alphabets)] for c in s])
    return answer