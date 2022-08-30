import sys
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    user = sys.stdin.readline().split()

    if user[0] == "push":
        stack.append(user[1])

    elif user[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop(-1))
    elif user[0] == "size":
        print(len(stack))
    elif user[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif user[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
