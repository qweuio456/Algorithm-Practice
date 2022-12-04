import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # heap으로 리스트를 만듬

    while scoville[0] < K:
        mixed = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2) # 섞은 음식의 스코빌 지수를 계산
        heapq.heappush(scoville, mixed) # 계산한 스코빌 지수를 맨 앞에 출력
        answer = answer + 1 # 섞을 때 마다 횟수 증가
        if len(scoville) == 1 and scoville[0] < K: # 모든 음식의 스코빌 지수를 K 이상 만들 수 없고, 스코빌 지수가 1개인 경우
            return -1
        
    return answer

# 출력
print(solution([1, 2, 3, 9, 10, 12], 7))


