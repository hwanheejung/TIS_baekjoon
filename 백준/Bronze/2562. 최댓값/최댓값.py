max = 0
i = 0
for n in range(9):
    num = int(input())
    if num > max:
        max = num
        i = n

print(max)
print(i + 1)