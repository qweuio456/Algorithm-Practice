N = int(input()) # N장의 카드를 입력

card_list = [i for i in range(1, N + 1)] # 1부터 N번까지의 카드 리스트
drop_card = [] # 버린 카드 리스트

while len(card_list) != 1: # 카드 리스트 갯수가 1개가 아닐때까지 반복
    drop_card.append(card_list.pop(0)) # 버린 카드 리스트에 제일 위에 있는 카드를 버림
    card_list.append(card_list.pop(0)) # 버린 뒤 제일 위에 있는 카드를 제일 아래로 옮김(카드 리스트 제일 뒤로 이동)

for i in drop_card: # 버린 카드 차례로 출력
    print(i, end = ' ') 

print(card_list[0]) # 남아 있는 카드 한 개 출력