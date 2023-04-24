def solution(s):
    stack = list()
    
    for c in s:
        if c == "(":
            stack.append(c)
        elif stack and c == ")":
            stack.pop()
        else:
            return False
        
    return False if stack else True
            
            
                