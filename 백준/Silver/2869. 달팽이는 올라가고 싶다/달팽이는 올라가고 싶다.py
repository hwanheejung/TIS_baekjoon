import sys
A, B, V = map(int, sys.stdin.readline().split())
days = (V - B) // (A - B)

if (V - B) % (A - B) > 0:
    days += 1

print(days)