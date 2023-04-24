from collections import defaultdict

def solution(genres, plays):
    hash_genres = defaultdict(list)
    answer = []

    for i, genre in enumerate(genres):
        hash_genres[genre].append((i, plays[i]))

    [genre.sort(key=lambda x: x[1], reverse=True) for genre in hash_genres.values()]

    sorted_genres = list(hash_genres.items())
    sorted_genres.sort(key=lambda x: sum([y[1] for y in x[1]]), reverse=True)
    
    for genre in sorted_genres:
        if len(genre[1]) > 1:
            if genre[1][0][1] == genre[1][1][1]:
                answer.append(min(genre[1][0][0], genre[1][1][0]))
                answer.append(max(genre[1][0][0], genre[1][1][0]))
            else:
                answer.append(genre[1][0][0])
                answer.append(genre[1][1][0])
        else:
            answer.append(genre[1][0][0])

    return answer