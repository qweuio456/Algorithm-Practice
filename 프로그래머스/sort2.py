def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse = True) # numbers 인수값이 1000이하이므로 3자리수로 맞춰 내림차순
    return str(int(''.join(numbers))) # 0값을 처리하기 위해 numers를 int형식으로 합친 후 다시 str형식으로 변환

# 출력
print(solution([3, 30, 34, 5, 9]))
