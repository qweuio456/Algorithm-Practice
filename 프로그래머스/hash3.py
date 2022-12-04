def solution(phone_book):

    phone_book.sort() # phone_book을 오름차순으로 정렬
    for i in range(0, len(phone_book) - 1): # phone_book의 리스트 갯수 만큼 순환 
        if phone_book[i] == (phone_book[i + 1])[:len(phone_book[i])]: # 같은 전화번호가 중복해서 들어있는지 여부 확인
            return False

    return True

print(solution(["123","456","789"]))
