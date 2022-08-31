import sys
from collections import Counter
M = sys.stdin.readline()
M_li = list(map(int, sys.stdin.readline().split()))
N = int, sys.stdin.readline()
N_li = list(map(int, sys.stdin.readline().split()))

count = Counter(M_li)

for n in range(len(N_li)):
    if N_li[n] in count:
        print(count[N_li[n]], end = " ")
    else:
        print(0, end = " ")