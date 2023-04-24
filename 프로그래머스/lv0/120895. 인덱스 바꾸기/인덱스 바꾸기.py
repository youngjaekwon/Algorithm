def solution(my_string, num1, num2):
    return my_string[:(mn:=min(num1,num2))] + my_string[(mx:=max(num1,num2))] + my_string[mn+1:mx] + my_string[mn] + my_string[mx+1:]