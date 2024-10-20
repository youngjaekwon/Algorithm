from collections import deque

def solution(begin, target, words):
    answer = len(words) + 1
    def back(visited, begin):
        nonlocal answer
        if begin == target:
            answer = min(len(visited) - 1, answer)
        
        for w in words:
            if w in visited:
                continue
            
            n = 0
            for a, b in zip(begin, w):
                if a == b:
                    n += 1
            if n == len(begin) - 1:
                visited.add(w)
                back(visited, w)
                visited.remove(w)

    back(set([begin]), begin)
    
    return answer if answer < len(words) + 1 else 0

        