word = input()
N = int(input())
count = 0

for _ in range(N):
    ring_word = input()
    ring_word = ring_word + ring_word # 반지의 시작과 끝이 연결되어 있는 경우가 있음 

    if ring_word.find(word) != -1:
        count = count + 1

print(count)