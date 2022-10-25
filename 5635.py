students = [] # 학생들 리스트 
n = int(input())

for i in range(n):
    student = input().split() # 학생들 입력
    student[1:] = map(int, student[1:]) # 생년월일을 정수형으로 변환
    
    students.append(student)

students.sort(key = lambda student: (student[3], student[2], student[1])) # 생년월일 오름차순 정렬

print(students[-1][0]) # 나이가 가장 적은 사람
print(students[0][0]) # 나이가 가장 많은 사람