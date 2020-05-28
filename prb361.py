secret_key = "547312"
# import random
# f = 0
# secret_key = ""
# lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# while f < 6:
#     temp = random.choice(lst)
#     secret_key += str(temp)
#     lst.remove(temp)
#     f += 1
# print(secret_key)
guess = "143286"
cnt = 0
for i in range(6):
    if secret_key[i] == guess[i]:
        cnt += 1
    else:
        pass
print(cnt)
