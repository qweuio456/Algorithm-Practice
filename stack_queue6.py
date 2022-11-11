from collections import deque

def solution(prices):
    queue = deque(prices) # 가격을 큐로 저장
    answer = []

    while queue:
        price = queue.popleft() # 인덱스가 0인 가격
        sec = 0
        for q in queue: # 가격이 떨어질 때 까지 계산
            sec = sec + 1
            if price > q:
                break
        answer.append(sec) # 각각 나온 초를 저장

    return answer

# 출력
print(solution([1,2,3,2,3]))

