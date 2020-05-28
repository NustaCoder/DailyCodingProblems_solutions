listner = [1, 5, 11, 20]
towers = [4, 8, 15]
record = []
min_dist = []
for i in listner:
    t = []
    for j in towers:
        if i < j:
            c = (i-j)*(-1)
            t.append(c)
        else:
            c = (i-j)
            t.append(c)
    record.append(t)
for i in record:
    min_dist.append(min(i))
print(max(min_dist))
