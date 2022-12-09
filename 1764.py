import sys
input = sys.stdin.readline

n, m = map(int, input().split())

x = set()
y = set()
# 중복을 제거하여 듣도 못한 사람의 수 삽입
for i in range(n):
    x.add(input())

# 중복을 제거하여 보도 못한 사람의 수 삽입
for i in range(m):
    y.add(input())

# 듣도 보도 못한 사람을 리스트에 삽입하여 정렬
result = sorted(list(x & y))

# 듣도 보도 못한 사람 수 출력
print(len(result))

# 듣도 보도 못한 사람 이름 출력
for i in result:
    print(i, end = '')