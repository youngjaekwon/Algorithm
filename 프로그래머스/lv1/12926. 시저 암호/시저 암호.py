def solution(s, n):
    answer = ''
    for c in s:
        if c.isalpha():
            if c.isupper():
                i = ord(c)
                i = i + n if i + n <= 90 else i + n - 26
                c = chr(i)
            else:
                i = ord(c)
                i = i + n if i + n <= 122 else i + n - 26
                c = chr(i)
        answer += c
    return answer