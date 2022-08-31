import sys
N = int(input())
L = []

for n in range(N):
    A, B = map(int, sys.stdin.readline().split())
    li = [A, B]
    L.append(li)

L.sort(key=lambda x: (x[0], x[1]))

for i in range(len(L)):
    print(*L[i])