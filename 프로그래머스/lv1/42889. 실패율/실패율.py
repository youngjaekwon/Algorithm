def solution(N, stages):
    return sorted(range(1, N+1), key=lambda x: (stages.count(x) / y if (y := len([i for i in stages if i >= x])) else 0, -x), reverse=True)