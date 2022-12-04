def solution(name):
    answer = 0
    min_move = len(name) - 1 # 기본 최소 좌우이동 횟수 길이 - 1

    for idx, char in enumerate(name):
        # 해당 알파벳의 변경 최솟값을 추가함
        answer = answer + min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열을 찾음
        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next = next + 1
        
        # 기존과 연속된 A의 왼쪽 시작 방식, 연속된 A의 오른쪽 시작 방식 비교하여 최솟값을 구함
        min_move = min([min_move, 2 * idx + len(name) - next, idx + 2 * (len(name) - next)])

    answer = answer + min_move
    return answer

print(solution("JEROEN"))
