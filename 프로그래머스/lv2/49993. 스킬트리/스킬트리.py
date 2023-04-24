def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        tmp = "".join([x for x in s if x in skill])
        if skill.startswith(tmp):
            answer += 1
    return answer