import sys
N = int(sys.stdin.readline())
P = sorted(list(map(int, sys.stdin.readline().split())))
sum = 0
sumL = []

for i in P:
    sum += i
    sumL.append(sum)

res = 0
for i in sumL:
    res += i
print(res)