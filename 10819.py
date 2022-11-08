import sys
from itertools import permutations

# 입력
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

answer = -1

# 순열을 사용하여 최대를 구함
for p in list(permutations(A)):
    sum = 0
    for i in range(N - 1):
        sum = sum + abs(p[i] - p[i + 1])
    
    if answer < sum:
        answer = sum

print(answer)


