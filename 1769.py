X = list(map(int, str(input())))

num_count = 0 # 각 자리수를 더한 횟수
while True:
    if len(X) == 1: # 값이 한자리 수면
        result = X[0] # 결과 값이 한자리 수인 값 대입
        break 

    num_count = num_count + 1 # 결과 값이 두 자리 이상이면 각 자리수를 더한 횟수를 1 증가
    result = 0 # 각 자리수를 더한 결과 값 

    for i in X: # 리스트 형태의 각 자리수를 각각 더함
        result += i
    
    if result < 10: # 결과 값이 10보다 작으면 while문 종료
        break
    else: # 결과 값이 10 이상이면 X의 각 자리수를 list 형태로 대입 
        X = list(map(int, str(result)))

if result % 3 == 0: # 결과 값이 3의 배수이면 각 자리수를 더한 횟수와 YES를 출력
    print(num_count)
    print('YES')
else: # 결과 값이 3의 배수가 아니면 각 자리수를 더한 횟수와 NO를 출력
    print(num_count)
    print('NO')


