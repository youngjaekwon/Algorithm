def solution(code):
    mode = 0
    ret = ""
    
    for i, v in enumerate(code):
        if v == "1":
       		mode = int(mode == 0)
        	continue
        if not mode and not i % 2:
            ret += v
        elif mode and i % 2:
            ret += v
            
    return ret if ret else "EMPTY"