res = []

for i in range(10):
    num = int(input())
    rest = num % 42
    if rest not in res:
        res.append(rest)

print(len(res))