import sys

# 입력
N, K = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

# 누적합 구하기
psum = [0] * N
psum[0] = N_list[0]

for i in range(1, N):
    psum[i] = psum[i - 1] + N_list[i]

count = {}
answer = 0
for i in range(N):
    goal = psum[i] - K

    if goal in count:
        answer = answer + count[goal]
    if goal == 0:
        answer = answer + 1
    
    if psum[i] not in count:
        count[psum[i]] = 0
    count[psum[i]] = count[psum[i]] + 1

print(answer)
print(count)




    