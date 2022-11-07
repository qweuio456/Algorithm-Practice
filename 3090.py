# 입력
N, T = tuple(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

def needed_num_operation(x):
    # 차이를 x 이하로 만들기 위해 필요한 연산(1을 감소시키는)의 횟수를 구함
    B = [A[i] for i in range(N)]

    num_operation = 0
    for i in range(N - 1): 
    # 왼쪽에서 오른쪽으로    
        if B[i] + x < B[i + 1]:
            num_operation = num_operation + B[i + 1] - B[i] - x
            B[i + 1] = B[i] + x
    
    for i in range(N - 1, 0, -1):
    # 오른쪽에서 왼쪽으로
        if B[i] + x < B[i - 1]:
            num_operation = num_operation + B[i - 1] - B[i] - x
            B[i - 1] = B[i] + x
    
    return num_operation

low = 0
high = int(1e9)
answer = -1

# 이분탐색
while low <= high:
    mid = (low + high) // 2

    if needed_num_operation(mid) <= T:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

for i in range(N - 1):
    if A[i] + answer < A[i + 1]:
        A[i + 1] = A[i] + answer
    
for i in range(N - 1, 0 , -1):
    if A[i] + answer < A[i - 1]:
        A[i - 1] = A[i] + answer
    
print(" ".join(list(map(str, A))))
