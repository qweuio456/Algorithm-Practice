def solution(n, lost, reserve):
    reserved = set(reserve) - set(lost) # 여분을 가져온 학생 번호 중 옷을 잃어버리지 않은 학생 번호
    losted = set(lost) - set(reserve) # 옷을 잃어버린 학생 중 여분의 옷이 없는 학생

    for i in reserved: # 여분의 옷이 있는 학생
        if i - 1 in losted:
            losted.remove(i - 1) # 여분의 옷이 있는 학생의 앞번호 학생이 옷을 잃어버린 경우 
        elif i + 1 in losted:
            losted.remove(i + 1) # 여분의 옷이 있는 학생의 뒷번호 학생이 옷을 잃어버린 경우 
        
    answer = n - len(losted)

    return answer

# 출력
print(solution(5, [2, 4], [1, 3, 5]))
