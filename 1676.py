N = int(input())

count = 0

while N >= 5:
    count = count + (N // 5)
    N = N // 5

print(count)