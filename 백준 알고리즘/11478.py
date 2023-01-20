import sys
input = sys.stdin.readline

s = input().rstrip()
word = set()
for i in range(len(s) + 1):
    for j in range(i, len(s) + 1):
        # set으로 넣어 중복을 제거
        word.add(s[i:j])

print(len(word) - 1)

