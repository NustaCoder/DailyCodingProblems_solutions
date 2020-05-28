line = 'abcddddd'
char = []
for i in line:
    if i not in char:
        char.append(i)
char.sort()
l = len(char)
while l <= len(line):
    temp_len = len(line) - l + 1
    for i in range(temp_len):
        temp1 = []
        temp2 = line[i:i+l]
        for j in temp2:
            if j not in temp1:
                temp1.append(j)
        temp1.sort()
        if char == temp1:
            print(l)
            l = len(line)
            break
    l += 1

