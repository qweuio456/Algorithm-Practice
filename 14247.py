import sys

# 입력
n = int(sys.stdin.readline())
Hi = list(map(int, sys.stdin.readline().split()))
Ai = list(map(int, sys.stdin.readline().split()))
I = list(range(n))

# 정렬
I = sorted(I, key=lambda i: Ai[i])

result = 0
for i in range(0, n):
    index = I[i]
    result = result + Hi[index] + i * Ai[index]

print(result)
    

