N = int(input()) # 사람의 수 입력
score = []

for _ in range(N): # 사람의 수 만큼 카드 입력
    card = list(map(int, input().split()))
    max_num = 0 # 가장 큰 일의 자리 수 선언
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                num = (card[i] + card[j] + card[k]) % 10 # 일의 자리 수 출력
                
                if num >= max_num: # 가장 큰 일의 자리 수를 구함
                    max_num = num
    score.append(max_num) # 사람당 가장 큰 일의 자리 수를 score에 추가

for i in range(N - 1, -1, -1): # 두 명 이상인 경우 번호가 가장 큰 사람의 번호를 구함
    if score[i] == max(score): 
        print(i + 1)
        break
        

