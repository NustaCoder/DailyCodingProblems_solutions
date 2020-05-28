import math
usr_time = input()
lst = usr_time.split(':')
hr, min = int(lst[0]), int(lst[1])
if hr == 12:
    hr = 0
hr_rot = ((hr*5)*6) + (min/2)
min_rot = min*6

ans = hr_rot - min_rot
if(ans < 0):
    ans *= -1
print(ans)
