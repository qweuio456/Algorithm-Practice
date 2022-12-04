def solution(s):
    par = []
    for i in s:
        if i == '(':
            par.append(i)
        else:
            if par == []:
                return False
            else:
                par.pop()
    
    return par == []

print(solution(")()("))
