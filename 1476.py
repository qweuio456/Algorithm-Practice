x_E, x_S, x_M, count = 1, 1, 1, 1
E, S, M = map(int, input().split())

while True:
    if x_E == E and x_S == S and x_M == M:
        break
    x_E = x_E + 1
    x_S = x_S + 1
    x_M = x_M + 1
    count = count + 1
    if x_E > 15:
        x_E = x_E - 15
    if x_S > 28:
        x_S = x_S - 28
    if x_M > 19:
        x_M = x_M - 19

print(count)