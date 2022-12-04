def solution(nums):
    choice = int(len(nums) / 2) # 가져갈 수 있는 폰켓몬의 갯수
    kind = len(list(set(nums))) # 폰켓몬의 종류 갯수
    result = 0 

    if choice >= kind: # 가져갈 수 있는 폰켓몬의 갯수가 폰켓몬의 종류 갯수보다 크거나 같으면 
        result = kind # 폰켓몬의 종류 갯수를 결과 변수에 대입
    else: # 가져갈 수 있는 폰켓몬의 갯수가 폰켓몬의 종류 갯수보다 작으면
        result = choice # 가져갈 수 있는 폰켓몬의 갯수를 결과 변수에 대입

    return result

# 입출력
print(solution([3,1,2,3]))
