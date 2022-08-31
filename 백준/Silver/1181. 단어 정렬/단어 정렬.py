N = int(input())
li = []
for n in range(N):
    str = input()
    if str not in li:
        li.append(str)

li.sort()
li.sort(key= len)

for i in li:
    print(i)
