import random

dict_snakes = {'16' : 6, '48' : 26, '49' : 11, '56' : 53, '62' : 19, '64' : 60, '87' : 24, '93' : 73, '95' : 75, '98' : 78}
dict_ladder = {'1' : 38, '4' : 14, '9' : 31, '21' : 42, '28' : 84, '36' : 44, '51' : 67, '71' : 91, '80' : 100}
lst = [str(i) for i in range(1,101)]
p = '0'
cnt = 0
while p != '100':
    cnt += 1
    dice = random.randint(1,6)
    p = str(int(p) + dice)
    print('p= ',p,' dice= ',dice)
    if p in dict_snakes.keys():
        p = str(dict_snakes[p])
        print('caught by snake : ',p)
    elif p in dict_ladder.keys():
        p = str(dict_ladder[p])
        print('found ladder : ',p)
    elif int(p) > 100:
        p = str(int(p) - dice)
        
print('p= ',p,'cnt= ',cnt)