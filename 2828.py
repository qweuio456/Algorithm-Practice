N, M = map(int, input().split()) # 스크린 칸과 바구니 칸 입력
J = int(input()) # 떨어지는 사과의 개수 입력

now = 1 # 현재 위치
apples = [] # 사과가 떨어지는 위치
answer = 0 # 총 이동해야 하는 거리
for _ in range(J):
    apples.append(int(input()))

for x in apples:
    if now <= x and now + (M - 1) >= x: # 현재 자리에서 사과를 받는 경우(이동하지 않아도 됨) 
        pass
    elif now > x: # 현재 자리가 사과가 떨어지는 위치보다 수가 큰 경우
        answer = answer + abs(x - now)
        now = x
    else: # 현재 자리가 사과가 떨어지는 위치보다 수가 작은 경우
        answer = answer + x - (M - 1) - now
        now = x - (M - 1)
print(answer)

