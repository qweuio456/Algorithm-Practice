import sys
input = sys.stdin.readline

cnt = {}

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    
    if array[mid] == target:
        return cnt.get(target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

n = int(input())
x = sorted(list(map(int, input().split())))
m = int(input())
y = list(map(int, input().split()))

for i in x:
    if i in cnt:
        cnt[i] = cnt[i] + 1
    else:
        cnt[i] = 1

for i in y:
    print(binary_search(x, i, 0, len(x) - 1), end = ' ')
