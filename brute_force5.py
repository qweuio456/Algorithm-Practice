from itertools import permutations

def solution(k, dungeons):
    dun_num = len(dungeons) # 던전의 갯수
    result = 0

    for per in permutations(dungeons, dun_num): # 던전의 갯수만큼 순열을 이용하여 탐험할 수 있는 최대 던전 수 계산
        hp = k
        count = 0
        for p in per:
            if hp >= p[0]: # 현재 피로도가 최소 필요 피로도보다 크거나 같으면
                hp = hp - p[1] # 현재 피로도에서 소모 피로도를 뺌
                count = count + 1 # 던전을 돌 수 있는 수를 1 늘림
        if count > result:
            result = count # 최대 던전 수 대입
    
    return result

# 출력
print(solution(80, [[80,20],[50,40],[30,10]]))
