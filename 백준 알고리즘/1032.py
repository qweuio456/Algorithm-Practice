num = int(input())
file_name = list(input())
file_name_len = len(file_name)

for i in range(num - 1):
    file_name2 = list(input())
    for j in range(file_name_len):
        if file_name[j] != file_name2[j]:
            file_name[j] = '?'

print(''.join(file_name))
