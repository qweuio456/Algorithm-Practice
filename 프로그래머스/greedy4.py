def solution(people, limit):
    answer = 0
    people.sort() # 사람들을 오름차순으로 정렬

    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit: # 보트를 2명이서 타는 경우
            a = a + 1
            answer = answer + 1 
        b = b - 1

    return len(people) - answer # 사람 수에서 보트를 2명이서 타는 경우를 뺌

# 출력
print(solution([70, 50, 80, 50], 100))
