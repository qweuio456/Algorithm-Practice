n = int(input())
requests = list(map(int, input().split()))
budget = int(input())

def caculate_needed_budget(upper_bound):
    # 상한액이 upper_bound일 때 필요한 예산을 계산하는 함수
    needed_budget = 0
    for request in requests:
        needed_budget = needed_budget + min(request, upper_bound)
    
    return needed_budget

# 이분 탐색
low = 0
high = max(requests)
good_upper_bound = -1

while low <= high:
    mid = (low + high) // 2

    if caculate_needed_budget(mid) <= budget:
        good_upper_bound = mid
        low = mid + 1
    else:
        high = mid - 1

answer = -1

for request in requests:
    given = min(request, good_upper_bound)
    answer = max(answer, given)
print(answer)


