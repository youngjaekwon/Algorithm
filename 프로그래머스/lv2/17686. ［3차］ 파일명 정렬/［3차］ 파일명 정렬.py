def solution(files):
    answer = []
    l = []
    for i, file_name in enumerate(files):
        head = ""
        number = ""
        for c in file_name:
            if c.isnumeric():
                number += c
            elif not number:
                head += c
            elif number and (c in [" ", ".", "-"] or c.isalpha()):
                break
        l.append((i, head, number, file_name))
    l.sort(key=lambda x: (x[1].upper(), int(x[2]), x[0]))
        
    return [x[-1] for x in l]