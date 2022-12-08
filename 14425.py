import sys
input = sys.stdin.readline

cnt = 0
n, m = map(int, input().split())
s = set([input() for _ in range(n)])

for _ in range(m):
    x = input()
    if x in s:
        cnt = cnt + 1

print(cnt)
