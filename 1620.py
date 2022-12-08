import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pokemon = []
dic = {}

for i in range(1, n + 1):
    a = input().rstrip()
    pokemon.append(a)
    dic[a] = i

for _ in range(m):
    x = input().rstrip()
    if x.isalpha():
        print(dic[x])
    elif x.isdigit():
        print(pokemon[int(x)])
