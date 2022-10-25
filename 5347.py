from math import gcd

N = int(input())  

for _ in range(N): 
    a, b = map(int, input().split()) # 두 수 a와 b입력
    print(a * b // gcd(a, b))  # 두 수를 곱한 후 두 수의 최대공약수를 나눈 몫(최소공배수)