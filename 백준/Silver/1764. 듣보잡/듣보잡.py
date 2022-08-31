N, M = map(int, input().split())

d = set()
b = set()
for i in range(N):
    d.add(input())
for i in range(M):
    b.add(input())

mutual = list(d & b)
res = sorted(mutual)
print(len(res))

for i in res:
    print(i)