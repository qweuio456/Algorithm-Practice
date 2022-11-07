import sys

# 입력
N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]

# 정렬
A.sort()

answer = -1
# 오름차순으로 정렬한 뒤 뒤에서부터 for문을 돌려 삼각형을 만들 수 있는 조건을 만족하면 세 변의 길이으이 합을 구한 뒤 빠져나감
for i in range(N - 1, 1, -1):
    if A[i] < A[i - 1] + A[i - 2]:
        answer = A[i] + A[i - 1] + A[i - 2]
        break

print(answer)