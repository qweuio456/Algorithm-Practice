def solution(answers):
    result = []
    person_1 = [1, 2, 3, 4, 5] # 1번 수포자의 패턴
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5] # 2번 수포자의 패턴
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번 수포자의 패턴
    count_person = [0, 0, 0] # 각 수포자의 점수

    for index, answer in enumerate(answers): # 맞출 때마다 각 수포자에게 점수를 1점씩 추가
        if answer == person_1[index % len(person_1)]:
            count_person[0] = count_person[0] + 1
        if answer == person_2[index % len(person_2)]:
            count_person[1] = count_person[1] + 1
        if answer == person_3[index % len(person_3)]:
            count_person[2] = count_person[2] + 1

    for index, score in enumerate(count_person): # 가장 점수를 많이 받은 수포자의 인덱스를 출력
        if score == max(count_person):
            result.append(index + 1)

    return result

# 출력
print(solution([1, 2, 3, 4, 5]))

