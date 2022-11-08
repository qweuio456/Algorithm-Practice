import sys
from itertools import combinations

# 입력
N, S = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

answer = 0
for num_elements in range(1, N + 1):
    for c in list(combinations(N_list, num_elements)):
        if sum(c) == S:
            answer = answer + 1

print(answer)

