def solution(spell, dic):
    return 1 if sorted(spell) in map(sorted, dic) else 2