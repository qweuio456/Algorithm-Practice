import sys

n = int(sys.stdin.readline())

coins = list(map(int, sys.stdin.readline().split()))
coins.sort()

target = 1
for i in coins:
    # 만들 수 없는 금액을 찾을 시 반복을 종료
    if target < i:
        break
    target = target + i

# 만들 수 없는 금액 출력
print(target)
