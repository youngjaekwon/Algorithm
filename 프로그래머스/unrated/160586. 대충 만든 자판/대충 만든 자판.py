def solution(keymap, targets):
    answer = []
    d = dict()
    for key in keymap:
        for i, k in enumerate(key):
            cnt = i + 1
            if k in d and d[k] < cnt:
                continue
            
            d[k] = cnt
                
    targets = [[d[c] if c in d else -1 for c in word] for word in targets]
    targets = [sum(word) if -1 not in word else -1 for word in targets]
    return targets