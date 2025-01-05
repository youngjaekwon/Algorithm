N, K = list(map(int, input().split()))
baskets = [tuple(map(int, input().split())) for _ in range(N)]
locations = [b[1] for b in baskets]
max_location = max(locations)
board = [0] * (max_location + 1)
for value, location in baskets:
    board[location] = value

answers = []
s, e = 0, K * 2 + 1
sub_sum = sum(board[s:e])
answers.append(sub_sum)
while e < max_location:
    sub_sum -= board[s]
    sub_sum += board[e]
    answers.append(sub_sum)
    s += 1
    e += 1

print(max(answers))