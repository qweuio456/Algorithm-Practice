vowel = {"a", "e", "o", "u", "i"}

while True:
    word = input()
    if word == 'end':
        break
    word_list = list(word)
    v_exist = 0 # 모음이 존재하는지 확인하는 변수
    v_con = 0 # 모음 3개가 연속인지 확인하는 변수
    c_con = 0  # 자음 3개가 연속인지 확인하는 변수
    check = 0 # 같은 문자가 연속인지 확인하는 변수 
    for i in range(len(word_list)):
        if i > 0:
            if word_list[i] == word_list[i - 1]: # 문자가 연속인 경우
                if word_list[i] != "e" and word_list[i] != "o": # 연속된 문자가 e이거나 i가 아닌 경우
                    check = 1
                    break
        if word_list[i] in vowel: # 모음 중 하나가 포함된 경우
            v_exist = 1 
            v_con = v_con + 1
            c_con = 0
            if v_con == 3: # 모음 3개가 연속으로 온 경우
                check = 1
                break
        else: # 자음 중 하나가 포함된 경우
            v_con = 0
            c_con = c_con + 1
            if c_con == 3: # 자음 3개가 연속으로 온 경우
                check = 1
                break
    if (check != 1) and (v_exist == 1): # 모음이 존재하거나 같은 글자가 연속적으로 오지 않는 경우
        print("<" + word + "> is acceptable.")
    else:
        print("<" + word + "> is not acceptable.")