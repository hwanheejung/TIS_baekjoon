N = list(map(int, input()))
roomNum = []
setNum = [1, 2, 3, 4, 5, 6, 6, 7, 8]
need = 1

# 9를 6으로 바꿈
for n in N:
    if n == 9:
        roomNum.append(6)
    else:
        roomNum.append(n)

for n in roomNum:
    if n in setNum:
        setNum.remove(n)
    else:
        need += 1
        setNum.extend([1, 2, 3, 4, 5, 6, 6, 7, 8])
        setNum.remove(n)

print(need)
