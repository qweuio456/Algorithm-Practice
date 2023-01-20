# 이분 탐색 문제
N = int(input()) # 숫자 카드 개수
card = sorted(map(int, input().split())) # 숫자 카드에 적혀있는 정수
M = int(input()) # 숫자 카드인지 아닌지 구별하는 갯수
card_check = list(map(int, input().split())) # 숫자 카드인지 아닌지를 구해야 할 M개의 정수
answer = [] # 답을 저장하는 리스트

def binary(k, card, start, end): # 이분 탐색 
    mid = (start + end) // 2
    if start > end:
        answer.append(str(0))
    elif k == card[mid]:
        answer.append(str(1))
    elif k > card[mid]:
        binary(k, card, mid + 1, end)
    else:
        binary(k, card, start, mid - 1)

for i in card_check:
    start = 0
    end = len(card) - 1
    binary(i, card, start, end)

print(' '.join(answer))
