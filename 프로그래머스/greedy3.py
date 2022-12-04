def solution(number, k):
    answer = []
    
    for num in number:
        while k > 0 and answer and answer[-1] < num: # 작은 수 제거
            answer.pop()
            k = k - 1
        answer.append(num)
    
    return ''.join(answer[:len(answer) - k]) # k의 수를 제거한 값 결과

# 출력
print(solution("1231234", 3))

