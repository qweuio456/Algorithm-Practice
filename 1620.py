import sys

input = sys.stdin.readline

n, m = map(int, input().split())
book_list = []
book_dic = {}

for i in range(n):
    pokemon = input().rstrip()
    book_dic[pokemon] = i + 1
    book_list.append(pokemon)

for _ in range(m):
    x = input().rstrip()
    # 숫자면 리스트에 (해당 숫자 - 1)을 출력
    if x.isdigit():
        print(book_list[int(x) - 1])
    else:
        print(book_dic[x])