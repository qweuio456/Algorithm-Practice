from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0]) # 큐에 첫번째 숫자 추가
    queue.append([-1 * numbers[0], 0]) # 큐에 부호를 바꾼 첫번째 숫자 추가  

    while queue:
        temp, idx = queue.popleft() # 큐에 맨앞 숫자를 꺼냄
        idx = idx + 1
        if idx < n:
            queue.append([temp + numbers[idx], idx]) 
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target: # temp가 target이랑 같을 때 result에 1을 추가
                answer = answer + 1
    
    return answer

# 출력
print(solution([1, 1, 1, 1, 1], 3))
