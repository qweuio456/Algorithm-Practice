from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_weight = 0 # 다리 위의 트럭 무게
    waiting = deque(truck_weights) # 대기 중인 트럭
    bridge = deque([0 for _ in range(bridge_length)]) # 다리의 길이만큼 0을 채움

    while len(waiting) or bridge_weight > 0:
        truck_remove = bridge.popleft()
        bridge_weight = bridge_weight - truck_remove

        if len(waiting) and bridge_weight + waiting[0] <= weight: # 새 트럭이 다리에 올라갈 수 있는 경우
            trucks = waiting.popleft()
            bridge_weight = bridge_weight + trucks

            bridge.append(trucks) # 다리에 트럭을 추가
        else:
            bridge.append(0) # 오른쪽에 0을 삽입해서 다리 길이를 유지함

        answer = answer + 1

    return answer

# 출력
print(solution(2, 10, [7, 4, 5, 6]))
