def solution(wallpaper):
    x = []
    y = []
    for i, row in enumerate(wallpaper):
        for j, item in enumerate(row):
            if item == "#":
                x.extend([i, i+1])
                y.extend([j, j+1])
    
    return [min(x), min(y), max(x), max(y)]