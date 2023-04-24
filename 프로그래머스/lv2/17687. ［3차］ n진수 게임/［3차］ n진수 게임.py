def get_num(n, k):
    T = "0123456789ABCDEF"
    q, r = divmod(n, k)
    return get_num(q, k) + T[r] if q else T[r]

def solution(n, t, m, p):
    al = ""
    for i in range(t*m+1):
        al += get_num(i, n)
    return al[p-1::m][:t]