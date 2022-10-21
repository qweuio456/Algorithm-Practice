N = input()
room = [0] * 10
for i in range(len(N)):
    num = int(N[i])
    if num == 6 or num == 9:
        if room[6] <= room[9]:
            room[6] += 1
        else:
            room[9] += 1
    else:
        room[num] += 1

print(max(room))