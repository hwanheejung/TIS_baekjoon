import sys
A, B = map(int, sys.stdin.readline().split())
import math
GCF = math.gcd(A, B)
a = A // GCF
b = B // GCF
LCM = GCF * a * b
print(GCF)
print(LCM)