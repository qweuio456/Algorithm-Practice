N = int(input())

x = 1 

while True:
    if x * (x + 1) / 2 <= N: # 1부터 x까지 더한 값이 N보다 작거나 같으면
        x = x + 1 # x를 1씩 증가
    else:
        print(x - 1) 
        break
