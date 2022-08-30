import sys
N = int(sys.stdin.readline())
queue = []

for _ in range(N):
    user = sys.stdin.readline().split()

    if user[0] == "push":
        queue.append(user[1])

    elif user[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))

    elif user[0] == "size":
        print(len(queue))

    elif user[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)

    elif user[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif user[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
