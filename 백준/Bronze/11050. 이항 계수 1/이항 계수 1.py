from math import factorial
import sys
N, K = map(int, sys.stdin.readline().split())
result = factorial(N) // (factorial(K) * factorial(N - K))
print(result)
