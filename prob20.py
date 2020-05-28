# #take the array input (from east to west)
# arr_temp = input().split()
# #convert in type int
# arr_buildings = [int(i) for i in arr_temp]
# #array to store result buildings
# arr_sunset = []
# #result count
# cnt = 0
# #comparison variable
# m = 0
# #reverse loop (from west to east)
# for i in range(len(arr_buildings)-1,-1,-1):
#     if m < arr_buildings[i]:
#         arr_sunset.append(arr_buildings[i])
#         cnt += 1
#         m = arr_buildings[i]
# print(cnt)
# print(arr_sunset)
a = [1,-1,3]
a.sort()
print(a)
b = [6,5,4]
b = sorted(b,reverse=False)
print(b)
c = {'a' : 10, 'b' : 20}
c['a'] = 100
print(c)
c.update({'a' : 10})
print(c)
c.reverse()
print(c)
d = [a,b,c]
e = 10
d[0].insert(0,e)
print(d)