from collections import Counter

def solution(participant, completion):
    answer = ''
    participant.sort() # 참가자 정렬
    completion.sort() # 완주자 정렬
    answer = Counter(participant) - Counter(completion) # 참가자 명단에서 완주자 명단을 뺌
        
    return list(answer)[0] # 완주하지 못한 사람 반환

# 답 출력
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))