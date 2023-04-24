from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0

    while len(people) > 1:
        if people[0] + people.pop() <= limit:
            people.popleft()
        answer += 1
    
    answer += len(people)

    return answer