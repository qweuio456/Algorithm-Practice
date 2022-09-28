n = int(input())

for _ in range(0, n):
    x, y = map(int, input().split())
    distance = y - x # y지점과 x 지점 사이의 거리
    count = 0 # 이동 횟수
    move = 1 # count 별 이동 가능한 거리
    move_add = 0 # 이동한 거리 합
    while move_add < distance:
        count += 1
        move_add += move # count 수에 해당하는 move를 더한 것
        if count % 2 == 0: # count가 2의 배수인 경우 move에 1을 더함
            move += 1
    print(count)