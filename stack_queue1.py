def solution(arr):
    answer = []
    
    answer.append(arr[0]) # arr의 0번째 원소 추가
    for i in range(1, len(arr)): # arr의 1번째부터 마지막번째까지 반복 
        if arr[i] != arr[i - 1]: # 중복 체크하여 같지 않으면 answer 리스트에 추가
            answer.append(arr[i])
        
    return answer

print(solution([1,1,3,3,0,1,1]))