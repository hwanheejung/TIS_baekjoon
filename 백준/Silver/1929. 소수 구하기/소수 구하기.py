def primeNum(x):
    if x > 1:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True
    elif x == 0:
        return False

import sys
M, N = map(int, sys.stdin.readline().split())

for x in range(M, N + 1):
    if primeNum(x):
        print(x)