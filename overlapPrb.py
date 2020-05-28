n = int(input())
box = list()

for i in range(n):
    a, b = map(int,input().split())
    box.append([a,b,0])
for i in range(len(box)):
    for j in range(i+1,len(box)):
        st1 , st2 = box[i][0], box[j][0]
        ed1 , ed2 = box[i][1], box[j][1]
        print(st1,st2,ed1,ed2) 