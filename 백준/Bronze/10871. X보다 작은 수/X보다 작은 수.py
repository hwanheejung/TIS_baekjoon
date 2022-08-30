import sys
N, X = map(int, sys.stdin.readline().split())

a = map(int, sys.stdin.readline().split())
A = list(a)
small = []

for a in A:
    if a < X:
        small.append(a)
    else:
        pass

print(*small)