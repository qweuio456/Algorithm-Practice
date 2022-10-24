N = int(input())

students = [] # 학생들의 정보를 담는 리스트

for _ in range(N): # 학생들의 정보 입력
    students.append(list(map(int, input().split())))

students.sort(key=lambda student: student[2], reverse = True) # 학생 성적을 기준으로 내림차순으로 정렬

gold = students[0] # 성적이 제일 높은 학생
silver = students[1] # 성적이 2번째로 높은 학생
bronze = 0 # 금메달과 은메달을 받은 사람이 같은 나라 학생이면 성적이 3번째로 높은 학생이 금메달과 은메달을 받은 사람과 같은 나라 학생인 경우 받을 수 없으므로 0으로 초기화

for i in range(2, len(students)):
    if gold[0] == silver[0] == students[i][0]: # 금, 은, 동 모두 같은 나라 학생인 경우 패스
        continue
    else:
        bronze = students[i] # 성적이 3번쨰로 높은 학생 
        break

print(gold[0], gold[1]) # 금메달 수상자 학생 소속국가 번호, 학생 번호
print(silver[0], silver[1]) # 은메달 수상자 학생 소속국가 번호, 학생 번호
print(bronze[0], bronze[1]) # 동메달 수상자 학생 소속국가 번호, 학생 번호



