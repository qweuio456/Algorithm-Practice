import sys
from collections import Counter

nums = []
n = int(sys.stdin.readline())

for i in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
c = Counter(nums).most_common(2)

# 산술평균
print(round(sum(nums) / n))
# 중앙값
print(nums[int(n / 2)])
# 최빈값
if len(nums) > 1:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])
# 범위
print(max(nums) - min(nums))