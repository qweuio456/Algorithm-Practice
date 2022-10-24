N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr_sum = [[0] * (M + 1) for _ in range(N + 1)] # 누적 합의 배열 선언

for i in range(1, N + 1):
    for j in range(1, M + 1):
        arr_sum[i][j] = arr[i - 1][j - 1] + arr_sum[i - 1][j] + arr_sum[i][j - 1] - arr_sum[i - 1][j - 1] # 누적 합을 저장

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(arr_sum[x][y] - arr_sum[i- 1][y] - arr_sum[x][j - 1] + arr_sum[i - 1][j - 1]) # (i, j)에서 (x, y)까지의 합
    

