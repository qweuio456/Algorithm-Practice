A, B = map(int, input().split())
N = int(input())
count = 0 # 버튼을 누르는 횟수


choice_N = [] # 즐겨찾기 되어있는 주파수 리스트
m_list = [] # 주파수 차이를 담는 리스트
for i in range(N): # 즐겨찾기 되어있는 주파수를 리스트에 저장
    choice_N.append(int(input()))

m_list.append(abs(B - A)) # B 주파수와 A 주파수의 차이를 리스트에 저장
for i in choice_N: # B 주파수와 즐겨찾기 되어있는 주파수의 차이를 각각 리스트에 저장
    m_list.append(abs(B - i))

min_dif = min(m_list) # 차이가 가장 적게 나는 숫자를 변수에 저장
if min_dif != m_list[0]: 
    count = count + 1
count = count + min_dif

print(count)

    
