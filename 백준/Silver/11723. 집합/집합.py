import sys
M = int(sys.stdin.readline())
S = set()

for m in range(M):
    user = sys.stdin.readline().split()

    if len(user) == 1:
        if user[0] == "all":
            S = set(a for a in range(1, 21))
        elif user[0] == "empty":
            S = set()

    elif len(user) == 2:
        first, second = user[0], user[1]
        second = int(second)
        if first == "add":
            S.add(second)
        elif first == "remove":
            if second in S:
                S.remove(second)
        elif first == "check":
            if second in S:
                print(1)
            else:
                print(0)
        elif first == "toggle":
            if second in S:
                S.remove(second)
            else:
                S.add(second)

