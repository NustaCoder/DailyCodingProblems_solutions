import math as ml
def isPall(a):
    atemp = a
    occ = int(ml.log10(num) + 1)
    temp = 0
    b = 10
    for i in range(occ,0,-1):
        t1 = a%b
        atemp -= t1
        t1 = int(t1/(b/10))
        b *= 10
        t2 = int(ml.pow(10,i-1))
        temp += t1*t2
    if(a-temp == 0):
        return 1
    else:
        return 0

num = int(input())
if(isPall(num)):
    print("it is pallindrome")
else:
    print("it is not pallindrome")