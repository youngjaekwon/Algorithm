d = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
def solution(numbers):
    tmp = ""
    word = ""
    for c in numbers:
        word += c
        if word in d:
            tmp += d[word]
            word = ""
    return int(tmp)