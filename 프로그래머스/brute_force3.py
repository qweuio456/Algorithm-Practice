from itertools import permutations

def solution(numbers):
    answer = []
    n = [num for num in numbers] # 입력된 숫자를 하나씩 자름 
    per = []
    for i in range(1, len(numbers) + 1):
        per = per + list(permutations(n, i)) # 하나씩 자른 숫자로 모든 경우의 수를 만듬
    result_n = [int("".join(x)) for x in per] # 모든 경우의 수를 만든 것을 정수형으로 만듬

    for x in result_n:
        if x < 2: # 소수가 아님
            continue
        check = True
        for y in range(2, int(x ** 0.5) + 1): # x의 제곱근보다 작은 숫자까지 계산
            if x % y == 0: # 나머지가 0인 경우는 소수가 아님
                check = False
                break
        if check:
            answer.append(x)

    return len(set(answer))

# 출력
print(solution("011"))




