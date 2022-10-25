n = int(input()) # 출입 기록 수
company = {} # 회사에 있는 사람 딕셔너리

for i in range(n):
    x, y = map(str, input().split())
    if y == "enter": # 회사에 출근한 경우
        company[x] = 1 # value에 1을 추가(출근)
    else: # 회사에 퇴근한 경우
        del company[x] # 회사에 있는 사람 딕셔너리에서 삭제
        
company = sorted(company.keys(), reverse = True) # 회사에 있는 사람 내림차순
for s in company: # 회사에 있는 사람 출력
    print(s)