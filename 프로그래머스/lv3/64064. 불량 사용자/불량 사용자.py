import fnmatch
import itertools


def solution(user_id, banned_id):
    l = []
    for i in banned_id:
        i = i.replace("*", "?")

        total = []

        for uid in user_id:
            if fnmatch.fnmatch(uid, i):
                total.append(uid)

        l.append(total)

    result = set(
        [
            tuple(sorted(comb))
            for comb in itertools.product(*l)
            if len(set(comb)) == len(banned_id)
        ]
    )

    return len(result)