def solution(numbers):
    answer = []
    for number in numbers:
        bnumber = bin(number)[2:]
        i = bnumber.rfind("0")
        if i == -1:
            bnumber = "10" + bnumber[1:]
        elif i != len(bnumber) - 1:
            bnumber = bnumber[:i] + "10" + bnumber[i+2:]
        else:
            bnumber = bnumber[:-1] + "1"
        answer.append(int("0b" + bnumber, 2))
    return answer