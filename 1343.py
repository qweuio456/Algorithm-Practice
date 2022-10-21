pan = input()

pan = pan.replace('XXXX', 'AAAA')
pan = pan.replace('XX', 'BB')

if 'X' in pan:
    print(-1)
else:
    print(pan)