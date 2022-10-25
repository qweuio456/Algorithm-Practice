K = int(input())

for i in range(K):
    S = list(map(int, input().split())) # 점수 입력
    del S[0] # 반 학생 수 제거
    S.sort() # 점수 오름차순
    diff = [] # 점수 차이 리스트
    print("Class", i + 1)
    for i in range(len(S) - 1):
        diff.append(S[i + 1] - S[i]) # 각각 점수 차이를 리스트에 저장
        
    print("Max", str(max(S)) + ',', "Min", str(min(S)) + ',', "Largest gap", max(diff))
    # 가장 높은 점수, 낮은 점수, 가장 큰 점수 차이 출력