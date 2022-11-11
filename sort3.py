def solution(citations):
    citations.sort()
    count = len(citations)

    for i in range(count):
        if citations[i] >= count - i:
            return count - i
    
    return 0

print(solution([3, 0, 6, 1, 5]))
