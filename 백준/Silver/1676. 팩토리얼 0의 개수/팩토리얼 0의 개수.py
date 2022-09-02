from math import factorial
N = int(input())
fac = [int(n) for n in str(factorial(N))]

idx = 1
num = 0

while idx <= len(fac):
    if fac[-idx] == 0:
        num += 1
        idx += 1
    else:
        break

print(num)