d = {
    '2': '0',
    '0': '5',
    '5': '2'
}
def solution(rsp):
    return "".join(d[c] for c in rsp)