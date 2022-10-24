N = int(input()) # 첫 번째 수

max_num = [] 

for i in range(1, N + 1): # 두 번째 수 부터 모두 검사
    num_list = [N] # 최대 길이를 가진 수들을 저장하는 리스트
    num_list.append(i)

    cnt = 1
    while True: # 세 번째 수부터 num_list에 저장
        next_num = num_list[cnt - 1] - num_list[cnt]
        if next_num < 0:
            break
        num_list.append(next_num)
        cnt += 1
    
    if len(max_num) < len(num_list): # num_list의 길이를 max_num의 길이와 비교하여 num_list가 더 길면 max_num으로 저장
        max_num = num_list 

print(len(max_num))  
for i in max_num:
    print(i, end=' ')     