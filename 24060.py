import sys
input = sys.stdin.readline

result = []

def merge_sort(A):
    if len(A) == 1:
        return A
    
    mid = (len(A) + 1) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    i, j = 0, 0
    nums = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums.append(left[i])
            result.append(left[i])
            i = i + 1
        else:
            nums.append(right[j])
            result.append(right[j])
            j = j + 1
    while i < len(left):
        nums.append(left[i])
        result.append(left[i])
        i = i + 1
    while j < len(right):
        nums.append(right[j])
        result.append(right[j])
        j = j + 1
    
    return nums

a, k = map(int, input().split())
x = list(map(int, input().split()))
merge_sort(x)

if len(result) >= k:
    print(result[k - 1])
else:
    print(-1)


