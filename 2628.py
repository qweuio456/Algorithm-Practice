X, Y = map(int, input().split()) # 가로, 세로 길이
N = int(input()) # 잘라야하는 점선의 개수
Xarr = [0] # 가로로 자른 위치 저장
Yarr = [0] # 세로로 자른 위치 저장

for i in range(N):
    p, q = map(int, input().split()) # p : 가로인지 세로인지 구분, q : 좌표
    if p == 0:
        Yarr.append(q) # 세로로 자른 위치 
    else:
        Xarr.append(q) # 가로로 자른 위치
Yarr.append(Y)
Xarr.append(X)
Yarr.sort()
Xarr.sort()

maxX = 0 # 최대 가로 길이
maxY = 0 # 최대 세로 길이

for i in range(1 , len(Xarr)): # 최대 가로 길이 계산
    tmp_X = Xarr[i] - Xarr[i - 1]
    if maxX < tmp_X:
        maxX = tmp_X
        
for i in range(1, len(Yarr)): # 최대 세로 길이 계산
    tmp_Y = Yarr[i] - Yarr[i - 1]
    if maxY < tmp_Y:
        maxY = tmp_Y

print(maxX * maxY) # 최대 넓이 출력