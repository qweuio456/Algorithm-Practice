s = input()

count_zero = 0
count_one = 0

# 첫 번째 원소 처리
if s[0] == '1':
    count_zero = count_zero + 1
else:
    count_one = count_one + 1

# 두 번째 원소부터 모든 원소를 확인
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if s[i + 1] == '1':
            count_zero = count_zero + 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count_one = count_one + 1

print(min(count_zero, count_one))

