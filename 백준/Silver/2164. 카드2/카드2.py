import sys, collections
N = int(sys.stdin.readline())
N_li = collections.deque([i for i in range(1, N+1)])


for i in range(N - 1):
    N_li.popleft()
    N_li.rotate(-1)

print(*N_li)