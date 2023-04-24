def solution(s):
    m = int(len(s)/2)
    return s[m] if len(s) % 2 else s[m-1:m+1] 