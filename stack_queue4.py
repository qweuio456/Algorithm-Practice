def solution(priorities, location):
    answer = 0
    max_num = max(priorities) # 중요도가 제일 높은 것
    while True:
        v = priorities.pop(0)
        if max_num == v: # 중요도가 높은 순서대로 인쇄
            answer = answer + 1
            if location == 0: # 현재 대기 목록의 위치가 0이면 종료 
                break
            else:
                location = location - 1
            max_num = max(priorities) # 중요도가 제일 높은 것이 삭제된 경우 초기화를 해줘야 하기 때문에 사용 
        else: # 중요도가 제일 높은 것이 리스트의 첫번째가 아니면  
            priorities.append(v) # 리스트의 맨 뒤로 보냄
            if location == 0: 
                location = len(priorities) - 1 # 대기 목록이 0인 경우
            else:
                location = location - 1 # 대기 목록이 0이 아닌 경우
    
    return answer

# 출력
print(solution([2, 1, 3, 2], 2))