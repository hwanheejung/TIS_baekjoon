import sys
N = map(int, sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

def primeN(X):
    if X == 1:
        return False
    for i in range(2, X):
        if X % i == 0:
            return False
    return True

res = 0
for n in num:
    if primeN(n) == True:
        res += 1
print(res)
