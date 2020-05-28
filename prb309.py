# main list
lst = [1, 1, 0, 1,  0, 1]
# positions where persons are currently sitting
pos = [i+1 for i in range(len(lst)) if lst[i] == 1]
win = len(pos)
cnt = 0
i = 0
left = right = 0
# slide window
while(i+win <= len(lst)):
    temp = 0
    for j in range(i, i+win):
        if(lst[j]) == 1:
            temp += 1
    if temp > cnt:
        cnt, left, right = temp, i, i+win
    i += 1
act = [i+1 for i in range(left, right)]
ans = sum(pos)-sum(act)
if ans < 0:
    ans *= -1
print("answer = ", ans)
