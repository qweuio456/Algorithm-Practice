def solution(citations):
    citations.sort()
    count = len(citations)

    for i in range(count):
        if citations[i] >= count - i:
            return count - i
    
    return 0

# 출력
print(solution([3, 0, 6, 1, 5]))

# 다른 풀이
def solution(citations):
    citations.sort(reverse = True)
    answer = max(map(min, enumerate(citations, start = 1)))

    return answer

# 출력
print(solution([3, 0, 6, 1, 5]))

# 다른 풀이
def solution(citations):
    citations.sort()
    length = len(citations)
    for idx, c in enumerate(citations):
        level = length - idx
        if c >= level:
            return level

    return level

# 출력
print(solution([3, 0, 6, 1, 5]))

