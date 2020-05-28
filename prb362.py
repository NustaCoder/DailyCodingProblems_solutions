# val = "1681"
# temp = ""
# for i in val:
#     if i == "1":
#         temp += i
#     elif i == "6":
#         temp += "9"
#     elif i == "8":
#         temp += "8"
#     elif i == "9":
#         temp += "6"
#     else:
#         temp = "not possible"
# temp = temp[::-1]
# if temp == val:
#     print(temp)
# else:
#     print("not possible")


def strobogrammatic_num(n):

    result = numdef(n, n)
    return result

# definition function


def numdef(n, length):

    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]

    middles = numdef(n - 2, length)
    result = []

    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")

        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result


# Driver Code
if __name__ == '__main__':

    # Print all Strobogrammatic
    # number for n = 3
    print(strobogrammatic_num(4))
