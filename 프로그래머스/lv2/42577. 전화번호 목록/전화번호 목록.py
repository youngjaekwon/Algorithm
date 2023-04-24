def solution(phone_book):
    phone_book.sort()
    for i, x in enumerate(phone_book):
        if i != len(phone_book) - 1 and phone_book[i + 1].startswith(x):
            return False
    return True