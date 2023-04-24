from collections import deque

def solution(tickets: list):
    queue = deque([(["ICN"], list(tickets))])
    tickets.sort()
    print(tickets)
    final_path = []

    while queue:
        p, t = queue.popleft()

        if not t:
            final_path.append(p)
            continue
        
        for ticket in tickets:
            if p[-1] == ticket[0] and ticket in t:
                nxt = ticket[1]
                np = list(p)
                np.append(nxt)
                nt = list(t)
                nt.remove(ticket)
                queue.append((np, nt))

    final_path.sort()
    return final_path[0]
