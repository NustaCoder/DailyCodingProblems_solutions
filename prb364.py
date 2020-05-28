# alternate add subtract 1 + 2 - 3 + 4
def add_subtract(*val):
    exp = val[0]
    temp1 = [val[i] for i in range(1, len(val)) if i % 2 == 0]
    temp2 = [val[i] for i in range(1, len(val)) if i % 2 != 0]
    return sum(temp2) - sum(temp1) + val[0]


val = add_subtract(-5, 10, 3, 9)
print(val)
