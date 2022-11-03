def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)): # genres와 plays를 묶어 dic1와 dic2에 추가
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))
        
        # {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]} 

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] = dic2[g] + p
        # {'classic': 1450, 'pop': 3100}

    for (x, y) in sorted(dic2.items(), key=lambda x:x[1], reverse = True):
        for (i, j) in sorted(dic1[x], key=lambda x:x[1], reverse = True)[:2]: # 최대 두 개까지 모아 베스트 앨범을 출시하므로 [:2]로 슬라이싱
            answer.append(i)
    
    return answer

# 입출력
print(solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500]))
