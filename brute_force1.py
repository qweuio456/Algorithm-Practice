def solution(sizes):
    w = []
    h = []
    answer = 0

    for i in range(len(sizes)): # w, h 중 큰 값은 w리스트에 넣고 작은 값은 h리스트에 넣음
        if sizes[i][0] >= sizes[i][1]: 
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    answer = max(w) * max(h) # w와 h리스트에서 가장 큰 값들을 곱한 값

    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

