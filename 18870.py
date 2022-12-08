import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

sorted_nums = sorted(list(set(nums)))
result = {sorted_nums[i] : i for i in range(len(sorted_nums))}

for i in nums:
    print(result[i], end = ' ')



