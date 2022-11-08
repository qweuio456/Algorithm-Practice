import sys

# 입력
N, M = map(int, sys.stdin.readline().split())
N_num = list(map(int, sys.stdin.readline().split()))

psum = []
result = 0
# N_num 리스트의 누적합을 구함
for i in range(N):  
    result = result + N_num[i]
    psum.append(result)


for _ in range(M):
    answer = 0
    # A번째 수부터 B번째 수까지 합을 구함
    A, B = map(int, sys.stdin.readline().split())
    if A - 2 < 0:
        answer = psum[B - 1]
    else:
        answer = psum[B - 1] - psum[A - 2]
    print(answer)
    


