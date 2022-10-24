S = list(input())
min_count = 0


for x in range(0, len(S) - 1):
    if int(S[x]) != int(S[x + 1]):
        min_count = min_count + 1

print((min_count + 1) // 2)