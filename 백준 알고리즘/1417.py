N = int(input())
min_count = 0
x = []
for i in range(N):
    x.append(int(input()))

if N == 1:
    print(0)
else:
    dasom = x[0]
    not_dasom = sorted(x[1:], reverse = True)
    for index, num in enumerate(not_dasom):
        if dasom == num:
            print(1)
            break
        while(not_dasom[0] >= dasom):
            min_count += 1
            dasom += 1
            not_dasom[0] -= 1
            not_dasom = sorted(not_dasom, reverse = True)
        print(min_count)
        break

