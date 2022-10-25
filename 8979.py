n, k = map(int, input().split()) # 국가의 수와 등수를 알고 싶은 국가 입력
x = [] # 각 국가를 나타내는 정수와 그 국가가 얻은 금, 은, 동 리스트
for i in range(n):
    x.append(list(map(int, input().split())))
x.sort(key=lambda x: (-x[1], -x[2], -x[3])) # 금, 은, 동으로 많은 순으로 내림차순

for i in range(n): # 등수를 알고 싶은 국가 인덱스 찾기
    if x[i][0] == k:
        index = i

for i in range(n): # 국가번호 index를 찾아 금, 은, 동메달의 수와 같으면 i에 1을 더한 값을 출력
    if x[index][1:] == x[i][1:]:
        print(i + 1)
        break