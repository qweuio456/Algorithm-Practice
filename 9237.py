n  = int(input()) # 묘목의 수
trees = [] # 나무가 다 자라는데 걸리는 시간 리스트
trees = list(map(int, input().split()))

trees.sort(reverse = True) # 나무가 다 자라는데 걸리는 시간을 내림차순
result = [] # 나무들을 심어 다 자랄 때 까지의 최소한의 시간 리스트
for index, j in enumerate(trees):
    result.append(index + j + 2) # 제일 오래 걸리는 나무를 먼저 심어 최소한의 시간 리스트에 저장
print(max(result))
    