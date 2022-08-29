K = int(input())
res = []

for i in range(1, K+1):
    n = int(input())
    if n != 0:
        res.append(n)
    if n == 0:
        res.pop()

result = 0
for r in res:
    result += r

print(result)