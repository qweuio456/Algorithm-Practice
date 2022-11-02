def solution(clothes):
    answer = 1
    types = [] # 의상 종류
    cnt = [] # 종류 별 갯수
    for i, j in clothes:
        types.append(j) # 의상 종류를 저장
    
    for k in set(types):
        cnt.append(types.count(k)) # 중복되는 의상을 제외하고 의상 별 갯수를 저장
    
    for x in cnt:
        answer = answer * (x + 1)  # 각 의상 종류별로 의상을 고르는 경우의 수

    return answer - 1 # 의상을 하나도 고르지 않는 경우는 제외

# 입출력
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))