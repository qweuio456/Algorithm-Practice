score = [] # 참가자의 점수 리스트
for i in range(0, 8): # 8문제를 입력하여 참가자의 점수 리스트에 추가
    score.append(int(input()))

score_sort = sorted(score, reverse = True) # 참가자의 점수 리스트를 내림차순함
x = [] # 가장 높은 점수 5개를 받는 리스트
for i in range(5): # 가장 높은 점수 5개를 리스트에 추가
    x.append(score_sort[i])

score_index = [] # 가장 높은 점수 5개 인덱스 리스트
sum = 0 # 가장 높은 점수 5개 총점

for i in x: # 가장 높은 점수 5개 인덱스들과 가장 높은 점수 5개 총점 계산
    sum = sum + i
    score_index.append(score.index(i))
print(sum)
score_index = sorted(score_index)
for i in score_index:
    print(i + 1, end = ' ')
