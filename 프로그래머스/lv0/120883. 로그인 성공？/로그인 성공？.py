def solution(id_pw, db):
    if id_pw in db:
        return "login"
    else:
        for pair in db:
            if pair[0] == id_pw[0]:
                return "wrong pw"
        return "fail"