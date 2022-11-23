import sys
n = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))
data.sort()

result = 0 # 총 그룹 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count = count + 1 # 현재 그룹에 해당 모험가를 포함
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면
        result = result + 1 # 총 그룹 수 증가
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화 

# 총 그룹의 수 출력
print(result)

