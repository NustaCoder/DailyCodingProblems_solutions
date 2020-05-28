def isPrime(a):
    if a == 2:
        return True
    else:
        for i in range(2,a-1):
            if a%i == 0:
                return False
        else:
            return True

def findLargestFactors(a):
    b = 1
    d = 1
    for i in range(1, a):    
        if a%i == 0:
            c = i
            t = int(a / i)
            if i > t:
                break
            b = t
            d = i
    return d, b
num = 10
cnt = 0
while num != 1:
    if(isPrime(num)):
        num -= 1
        cnt += 1
    else:
        num = max(findLargestFactors(num))
        cnt += 1
print(num, cnt)    