from collections import deque

def solution(progresses, speeds):
    progresses_queue = deque(progresses)
    speeds_queue = deque(speeds)
    count = 0
    answer = []
    while progresses_queue:
        if progresses_queue[0] + speeds_queue[0] >= 100:
            progresses_queue.popleft()
            speeds_queue.popleft()
            count = count + 1
        else:
            if count:
                answer.append(count)
                count = 0
            for i in range(len(progresses_queue)):
                progresses_queue[i] = progresses_queue[i] + speeds_queue[i]
    
    answer.append(count)

    return answer

# 입출력
print(solution([93, 30, 55], [1, 30, 5]))
        
