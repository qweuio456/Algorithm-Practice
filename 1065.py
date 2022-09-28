n = int(input()) 
hansu = 0

for i in range(1, n + 1): # 1부터 99까지는 한수임
    if i <= 99:
        hansu += 1       
    else:
        num = list(map(int, str(i))) # 3자리수부터 한자리씩 분리   
        if num[0] - num[1] == num[1] - num[2]: # 각 자리가 등차수열을 이루면 한수
            hansu += 1

print(hansu)