from itertools import permutations

def solution(k, dungeons):
    l = list(permutations(dungeons))
    answer = 0
    for case in l:
        tmp = int(k)
        cnt = 0
        for dungeon in case:
            if tmp >= dungeon[0]:
                tmp -= dungeon[1]
                cnt += 1
            else:
                break
        if cnt > answer:
            answer = cnt
    return answer