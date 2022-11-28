n = int(input())

house = list(map(int, input().split()))
house.sort()

# 중간값이 안테나로부터 모든 집까지의 거리의 총합이 최소
print(house[(n - 1) // 2])