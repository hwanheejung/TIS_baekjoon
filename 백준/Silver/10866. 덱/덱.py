from collections import deque
import sys
N = int(input())
dq = deque()

for _ in range(N):
    user = sys.stdin.readline().split()

    if user[0] == "push_front":
        dq.appendleft(user[1])
    elif user[0] == "push_back":
        dq.append(user[1])
    elif user[0] == "pop_front":
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif user[0] == "pop_back":
        if not dq:
            print(-1)
        else:
            print(dq.pop())
    elif user[0] == "size":
        print(len(dq))
    elif user[0] == "empty":
        if not dq:
            print(1)
        else:
            print(0)
    elif user[0] == "front":
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif user[0] == "back":
        if not dq:
            print(-1)
        else:
            print(dq[-1])
