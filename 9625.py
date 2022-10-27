K = int(input()) # 버튼을 누른 갯수

AB_list = [0] * (K + 1) # A와 B의 갯수를 저장하는 리스트
AB_list[1] = 1

for i in range(2, K + 1): # 피보나치 수열
    AB_list[i] = AB_list[i - 1] + AB_list[i - 2]

print(AB_list[K - 1], AB_list[K]) # 버튼을 K번 눌렀을 때 총 A와 B의 갯수 출력